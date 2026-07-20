import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Loads songs from a CSV file into a list of dicts with numeric fields converted."""
    print(f"Loading songs from {csv_path}...")
    songs = []
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            })
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores a single song against user preferences, returning the total score and reasons."""
    reasons = []
    total = 0.0

    # Mood match: +2.0 (highest weight, categorical)
    mood_points = 2.0 if song["mood"] == user_prefs["favorite_mood"] else 0.0
    if mood_points:
        reasons.append(f"mood match (+{mood_points:.1f})")
    total += mood_points

    # Genre match: +1.0 (categorical)
    genre_points = 1.0 if song["genre"] == user_prefs["favorite_genre"] else 0.0
    if genre_points:
        reasons.append(f"genre match (+{genre_points:.1f})")
    total += genre_points

    # Energy closeness: up to 2.0, distance-based.
    # energy and target_energy are both on a 0-1 scale, so their absolute
    # difference is itself a 0-1 "distance". Subtracting that distance from 1
    # turns "how far apart" into "how close" (1 = identical, 0 = maximally
    # far apart), then scaling by 2.0 rewards proximity to the target rather
    # than rewarding high or low energy on its own.
    energy_distance = abs(song["energy"] - user_prefs["target_energy"])
    energy_points = 2.0 * (1 - energy_distance)
    if energy_points:
        reasons.append(f"energy closeness (+{energy_points:.1f})")
    total += energy_points

    # Acousticness threshold: +0.5 if the song's acousticness falls on the
    # same side of 0.5 as the user's likes_acoustic preference, else -0.5.
    song_is_acoustic = song["acousticness"] > 0.5
    if song_is_acoustic == user_prefs["likes_acoustic"]:
        acoustic_points = 0.5
        reasons.append(f"acousticness match (+{acoustic_points:.1f})")
    else:
        acoustic_points = -0.5
        reasons.append(f"acousticness mismatch ({acoustic_points:.1f})")
    total += acoustic_points

    return total, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Scores every song against user preferences and returns the top k, ranked highest first."""
    scored = [
        (song, *score_song(user_prefs, song))
        for song in songs
    ]

    ranked = sorted(scored, key=lambda entry: entry[1], reverse=True)

    return [
        (song, score, ", ".join(reasons) if reasons else "no matching factors")
        for song, score, reasons in ranked[:k]
    ]

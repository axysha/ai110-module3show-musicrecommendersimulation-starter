"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # --- Starter example profile (commented out for now) ---
    # user_prefs = {
    #     "favorite_genre": "pop",
    #     "favorite_mood": "happy",
    #     "target_energy": 0.8,
    #     "likes_acoustic": False,
    # }
    #
    # recommendations = recommend_songs(user_prefs, songs, k=5)
    #
    # print("\nTop Recommendations")
    # print("=" * 40)
    # for rank, (song, score, explanation) in enumerate(recommendations, start=1):
    #     print(f"{rank}. {song['title']} ({song['artist']}) - Score: {score:.2f}")
    #     print(f"   Because: {explanation}")
    #     print("-" * 40)

    # Distinct "normal" taste profiles, each aligned with a real genre/mood
    # pairing that appears in data/songs.csv.
    profiles = {
        "High-Energy Pop": {
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.9,
            "likes_acoustic": False,
        },
        "Chill Lofi": {
            "favorite_genre": "lofi",
            "favorite_mood": "chill",
            "target_energy": 0.2,
            "likes_acoustic": True,
        },
        "Deep Intense Rock": {
            "favorite_genre": "rock",
            "favorite_mood": "intense",
            "target_energy": 0.75,
            "likes_acoustic": False,
        },

        # --- Adversarial / edge-case profiles ---
        # Conflicting signals: "melancholic" mood pairs with slow blues in the
        # data, but this user wants high energy anyway. Mood match and energy
        # closeness are pulling toward different songs.
        "Conflicting: Sad Mood + High Energy": {
            "favorite_genre": "blues",
            "favorite_mood": "melancholic",
            "target_energy": 0.9,
            "likes_acoustic": False,
        },
        # Contradictory: "angry" metal is naturally high-energy in the data,
        # but this user wants near-zero energy AND acoustic. Tests whether
        # the scorer collapses to genre/mood match alone or gets dragged
        # down by energy/acoustic mismatches.
        "Contradictory: Angry Metal but Wants Quiet Acoustic": {
            "favorite_genre": "metal",
            "favorite_mood": "angry",
            "target_energy": 0.05,
            "likes_acoustic": True,
        },
        # Nonexistent genre/mood: neither value appears anywhere in the CSV,
        # so genre_points and mood_points are always 0. Tests that scoring
        # degrades gracefully to energy + acoustic only, rather than
        # erroring or returning nonsensical results.
        "Edge Case: Unknown Genre/Mood": {
            "favorite_genre": "jazz fusion",
            "favorite_mood": "furious",
            "target_energy": 0.5,
            "likes_acoustic": False,
        },
        # Boundary values: energy exactly at the extremes (0.0 and 1.0 are
        # boundary inputs for the 0-1 scale) plus empty-string preferences,
        # to check for off-by-one or falsy-value bugs.
        "Edge Case: Boundary Energy + Empty Preferences": {
            "favorite_genre": "",
            "favorite_mood": "",
            "target_energy": 1.0,
            "likes_acoustic": False,
        },
    }

    for profile_name, user_prefs in profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\n{'=' * 60}")
        print(f"Profile: {profile_name}")
        print(f"Prefs: {user_prefs}")
        print("=" * 60)
        for rank, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"{rank}. {song['title']} ({song['artist']}) - Score: {score:.2f}")
            print(f"   Because: {explanation}")
            print("-" * 40)


if __name__ == "__main__":
    main()

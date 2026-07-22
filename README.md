# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

This recommender scores each song against a user by combining four independent signals into a single weighted sum: hard categorical matches on genre and mood (all-or-nothing bonuses), a closeness-based score on energy that rewards proximity to the user's target rather than raw magnitude, and a boolean check on whether the song's acousticness falls on the same side of a threshold as the user's stated preference. Because mood is weighted more heavily than the other three, the system prioritizes matching the emotional tone the user wants over strict genre labels or exact energy levels. Basically a song in an unexpected genre can still rank well if its mood is right, but a mood mismatch is hard to compensate for. Scoring stays local and per-song, while a separate ranking step handles sorting, tie-breaking, and top-k selection across the whole catalog, keeping "how good is this match" cleanly separate from "what's the best list to show.

Here are the specific features my 'Song' and 'User Profile' objects will use in this simulation

Song (scored by attributes):
- genre: categorical, matched against favorite_genre
- mood: categorical, matched against favorite_mood (highest weight)
- energy: continuous (0–1 scale), scored by closeness to target_energy
- acousticness: continuous (0–1 scale), thresholded into a boolean and compared to likes_acoustic

User Profile(preferences the score is computed aganist):
- favorite_genre: target value for the genre match
- favorite_mood: target value for the mood match, and the source of the extra weighting
- target_energy: target value for the energy closeness calculation
likes_acoustic — boolean target for the acousticness threshold check

Below is the 'Algorithm Recipe':
- Mood Fit (+2.0)
- Genre (+1.0)
- Energy closeness (weighted equally to mood +2.0)
- Acousticness (threshold check + or - 0.5, based on user preference)

Edge-case risk: because energy closeness + acousticness can together contribute up to 2.5 points, a song with the wrong mood and genre but energy landing exactly on target can occasionally outscore a song that correctly matches mood but misses on energy and acousticness — so strong continuous-signal alignment can, in rare cases, mask a poor categorical fit.


---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

```
# e.g.:
# User profile: favorite_genre: "pop", favorite_mood: "happy", target_energy: 0.8, likes_acoustic: False
#Top Recommendations
#========================================
#1. Sunrise City (Neon Echo) - Score: 5.46
#   Because: mood match (+2.0), genre match (+1.0), energy #closeness (+2.0), acousticness match (+0.5)
#----------------------------------------
#2. Rooftop Lights (Indigo Parade) - Score: 4.42
#   Because: mood match (+2.0), energy closeness (+1.9), #acousticness match (+0.5)
#----------------------------------------
#3. Gym Hero (Max Pulse) - Score: 3.24
#   Because: genre match (+1.0), energy closeness (+1.7), #acousticness match (+0.5)
#----------------------------------------
#4. Concrete Kingdom (MC Ledger) - Score: 2.46
#   Because: energy closeness (+2.0), acousticness match (+0.#5)
#----------------------------------------
#5. Fuego Nights (Mariposa Sol) - Score: 2.40
#   Because: energy closeness (+1.9), acousticness match (+0.#5)
#----------------------------------------
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

When I changed weights like making genre a higher priority, the model would only consider genre match for the top recommendations. Also when my user preferences are vague or empty, the model recommends a stronger mix of different genres and moods. 
---

## Limitations and Risks

You will go deeper on this in your model card.
The model doesn't handle specific contradictory edge cases. For example, if someone likes sad music that high energy. It also doesn't know lyrics or language so that would have to be added in to the overall scoring logic. The dataset also need to have greater diversity and more data overall to understand unique music tastes. 

Also if this was a application like Spotify or Youtube Music, we would also consider user interactions like likes, plays, skips, etc. 

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

What I mainly learned in this recommender project is that logic has a realw way of capturing human taste in personal activities like listening to music. It also made me realize how important human insight is when building a algorithmic framework because I can use to own judgement to see if the logic actually matches what someone is looking for in music recommendations. Biases and unfairness could show up when models don't address unqiue or edges cases. It can also show up in the dataset since that is what the model compares with so data diversity is very important to ensure the model supports different lived expriences. 
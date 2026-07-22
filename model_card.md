# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  
**Mood Matcher1.0**  

---

## 2. Intended Use  

This recommender is designed to suggest songs from a small curated catalog by matching a listener's stated taste (favorite genre, favorite mood, target energy level, and whether they like acoustic music) against each song's own genre, mood, and audio attributes. Then it ranks songs by how well they fit and explaining why each one was picked.

This recommender generates songs recommenders for music listerners based on their specific taste like favorite genre, mood, and how much energy they like in their songs. 

It assumes that listeners value mood above all else when wanting music recommendations from others. This is right now mainly for classroom exploration but later on can be fully built out for actual users

---

## 3. How the Model Works  

This recommender is designed to suggest songs from a small curated catalog by matching a listener's stated taste (favorite genre, favorite mood, target energy level, and whether they like acoustic music) against each song's own genre, mood, and audio attributes. Then, it ranks songs by how well they fit and explaining why each one was picked.

The starter logic placed an emphasis on genre but I chose to make mood the top priority in the scoring logic. Therefore, my scoring logic is set-up as the following:

Each song gets points added up based on how closely it matches what the listener asked for, and the song with the highest total score gets recommended first. Points are awarded like this:
- Mood match: +2 points if the song's mood matches the listener's favorite mood
-Genre match: +1 point if the song's genre matches the listener's favorite genre
-Energy fit: up to +2 points, with more points the closer the song's energy is to the listener's target energy
=Acoustic fit: +0.5 points if the song's acoustic level matches the listener's preference, or −0.5 points if it doesn't

---

## 4. Data  

The datset this model uses a CSV file named 'songs.csv' which contains 22 songs of different genres, moods, energy levels, and acoustic types. Originally the dataset only had 10 songs, so I added some more. The songs cover genres from 'metal' to 'country' and moods from 'chill' to 'intense'. One thing that might be missing as a category could be time period. 

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  
My system does well in capturing a mood and energy when those two are both correlating with one another. This is also helpful because listeners can exprience different genres of that capture the same mood and energy or find songs that are like their new tastes in mood. The model evolves with the listerner's mood which can vary from time to time. 
---

## 6. Limitations and Bias 

A weakness of this model is that categorical matches override energy contradictions. Since mood + genre are worth up to +3.0 points and energy closeness caps at +2.0 points, this creates a gap when a song whose energy doesn't closely match user's stated target. So a song can still show at a top recommendation based on the mood/genre match even though it doesn't match with a user's energy level. 

This means the scorer has no mechanism to let an extreme, explicit continuous-attribute mismatch veto a categorical tag match, which would systematically mislead any user whose energy/acoustic preferences diverge from the stereotype of their favorite genre/mood (e.g., someone who loves metal lyrically/thematically but only in acoustic covers)

---

## 7. Evaluation  

I created a diverse list of user profiles with edge cases to test my model's recommendations. Here are the profiles I added and some observations of the model's output:
1. High-Energy Pop
This profile prefers strong mood match with high energy.
2. Chill Lofi
This profile prefers moods like peacefull and chill moods with very low energy.
3. Deep Intense Rock
This profile prefers higher energy songs with strong intensity in mood and close match for the rock genre
4. Sad Mood + High Energy
This profile prefers high energy songs that are in the blues genre/mood. In this case, the model fails to capture the user's unqiue taste in my opionion since the current scoring logic places mood and genre above energy. Since the mood/genre conflicts with the energy metric, this edge case breaks the current algortihmic receipe
5. Angry Metal but Wants Quiet Acoustic
This profile prefers low energy and acoustic songs that are metal genre/mood inspired. Similar to profile #5, this edge-case shows that the model isn't truely reflective of the listener's specific taste. 
6. Unknown Genre/Mood
This profile prefers a blend of different genres from R&B to Reggae and moods like playful to chill. Here the model captures the user's wide range of preferences by suggesting different songs that align with genre,mood, and energy.
7. Boundary Energy + Empty Preferences
This profile prefers different genres as well that are all high energy and not acoustic. Similar to profile #6, the model is succesful in matching the user's energy and acoustic preference despite not having an input for mood/genre.
---

## 8. Future Work  

For the future, I would like to handle the edge-cases mentioned above that my model fails to capture. Also I would like to add more songs to my dataset to capture a more well-rounded sense of different music tastes. 

---

## 9. Personal Reflection  

What I learned about recommender systems is that you have to understand different user profiles because there is no simple 'math' to curate someone's desired music taste. This was suprising and enlightening because it made me think about how big companies use data and logic to capture the human experience of connecting with art. 

## 10. Fenced Code Blocks During Evaluation Phase
```
============================================================
Profile: High-Energy Pop
Prefs: {'favorite_genre': 'pop', 'favorite_mood': 'happy', 'target_energy': 0.9, 'likes_acoustic': False}
============================================================
1. Sunrise City (Neon Echo) - Score: 5.34
   Because: mood match (+2.0), genre match (+1.0), energy closeness (+1.8), acousticness match (+0.5)
----------------------------------------
2. Rooftop Lights (Indigo Parade) - Score: 4.22
   Because: mood match (+2.0), energy closeness (+1.7), acousticness match (+0.5)
----------------------------------------
3. Gym Hero (Max Pulse) - Score: 3.44
   Because: genre match (+1.0), energy closeness (+1.9), acousticness match (+0.5)
----------------------------------------
4. Bubblegum Rocket (Star Prism) - Score: 2.50
   Because: energy closeness (+2.0), acousticness match (+0.5)
----------------------------------------
5. Storm Runner (Voltline) - Score: 2.48
   Because: energy closeness (+2.0), acousticness match (+0.5)
----------------------------------------

============================================================
Profile: Chill Lofi
Prefs: {'favorite_genre': 'lofi', 'favorite_mood': 'chill', 'target_energy': 0.2, 'likes_acoustic': True}
============================================================
1. Library Rain (Paper Lanterns) - Score: 5.20
   Because: mood match (+2.0), genre match (+1.0), energy closeness (+1.7), acousticness match (+0.5)
----------------------------------------
2. Midnight Coding (LoRoom) - Score: 5.06
   Because: mood match (+2.0), genre match (+1.0), energy closeness (+1.6), acousticness match (+0.5)
----------------------------------------
3. Spacewalk Thoughts (Orbit Bloom) - Score: 4.34
   Because: mood match (+2.0), energy closeness (+1.8), acousticness match (+0.5)
----------------------------------------
4. Focus Flow (LoRoom) - Score: 3.10
   Because: genre match (+1.0), energy closeness (+1.6), acousticness match (+0.5)
----------------------------------------
5. Moonlight Sonata Reprise (Elena Voss) - Score: 2.40
   Because: energy closeness (+1.9), acousticness match (+0.5)
----------------------------------------

============================================================
Profile: Deep Intense Rock
Prefs: {'favorite_genre': 'rock', 'favorite_mood': 'intense', 'target_energy': 0.75, 'likes_acoustic': False}
============================================================
1. Storm Runner (Voltline) - Score: 5.18
   Because: mood match (+2.0), genre match (+1.0), energy closeness (+1.7), acousticness match (+0.5)
----------------------------------------
2. Gym Hero (Max Pulse) - Score: 4.14
   Because: mood match (+2.0), energy closeness (+1.6), acousticness match (+0.5)
----------------------------------------
3. Night Drive Loop (Neon Echo) - Score: 2.50
   Because: energy closeness (+2.0), acousticness match (+0.5)
----------------------------------------
4. Rooftop Lights (Indigo Parade) - Score: 2.48
   Because: energy closeness (+2.0), acousticness match (+0.5)
----------------------------------------
5. Concrete Kingdom (MC Ledger) - Score: 2.44
   Because: energy closeness (+1.9), acousticness match (+0.5)
----------------------------------------

============================================================
Profile: Conflicting: Sad Mood + High Energy
Prefs: {'favorite_genre': 'blues', 'favorite_mood': 'melancholic', 'target_energy': 0.9, 'likes_acoustic': False}
============================================================
1. Whiskey Rain (Delta Moan) - Score: 3.50
   Because: mood match (+2.0), genre match (+1.0), energy closeness (+1.0), acousticness mismatch (-0.5)
----------------------------------------
2. Bubblegum Rocket (Star Prism) - Score: 2.50
   Because: energy closeness (+2.0), acousticness match (+0.5)
----------------------------------------
3. Storm Runner (Voltline) - Score: 2.48
   Because: energy closeness (+2.0), acousticness match (+0.5)
----------------------------------------
4. Neon Pulse (DJ Meridian) - Score: 2.46
   Because: energy closeness (+2.0), acousticness match (+0.5)
----------------------------------------
5. Gym Hero (Max Pulse) - Score: 2.44
   Because: energy closeness (+1.9), acousticness match (+0.5)
----------------------------------------

============================================================
Profile: Contradictory: Angry Metal but Wants Quiet Acoustic
Prefs: {'favorite_genre': 'metal', 'favorite_mood': 'angry', 'target_energy': 0.05, 'likes_acoustic': True}
============================================================
1. Iron Verdict (Deathgrip) - Score: 2.66
   Because: mood match (+2.0), genre match (+1.0), energy closeness (+0.2), acousticness mismatch (-0.5)
----------------------------------------
2. Moonlight Sonata Reprise (Elena Voss) - Score: 2.10
   Because: energy closeness (+1.6), acousticness match (+0.5)
----------------------------------------
3. Spacewalk Thoughts (Orbit Bloom) - Score: 2.04
   Because: energy closeness (+1.5), acousticness match (+0.5)
----------------------------------------
4. Old Porch Stories (Willow Creek) - Score: 1.94
   Because: energy closeness (+1.4), acousticness match (+0.5)
----------------------------------------
5. Library Rain (Paper Lanterns) - Score: 1.90
   Because: energy closeness (+1.4), acousticness match (+0.5)
----------------------------------------

============================================================
Profile: Edge Case: Unknown Genre/Mood
Prefs: {'favorite_genre': 'jazz fusion', 'favorite_mood': 'furious', 'target_energy': 0.5, 'likes_acoustic': False}
============================================================
1. Slow Burn (Velvet Static) - Score: 2.40
   Because: energy closeness (+1.9), acousticness match (+0.5)
----------------------------------------
2. Island Sway (Sunny Roots) - Score: 2.34
   Because: energy closeness (+1.8), acousticness match (+0.5)
----------------------------------------
3. Night Drive Loop (Neon Echo) - Score: 2.00
   Because: energy closeness (+1.5), acousticness match (+0.5)
----------------------------------------
4. Rooftop Lights (Indigo Parade) - Score: 1.98
   Because: energy closeness (+1.5), acousticness match (+0.5)
----------------------------------------
5. Concrete Kingdom (MC Ledger) - Score: 1.94
   Because: energy closeness (+1.4), acousticness match (+0.5)
----------------------------------------

============================================================
Profile: Edge Case: Boundary Energy + Empty Preferences
Prefs: {'favorite_genre': '', 'favorite_mood': '', 'target_energy': 1.0, 'likes_acoustic': False}
============================================================
1. Iron Verdict (Deathgrip) - Score: 2.44
   Because: energy closeness (+1.9), acousticness match (+0.5)
----------------------------------------
2. Broken Glass Anthem (The Discord) - Score: 2.40
   Because: energy closeness (+1.9), acousticness match (+0.5)
----------------------------------------
3. Gym Hero (Max Pulse) - Score: 2.36
   Because: energy closeness (+1.9), acousticness match (+0.5)
----------------------------------------
4. Storm Runner (Voltline) - Score: 2.32
   Because: energy closeness (+1.8), acousticness match (+0.5)
----------------------------------------
5. Bubblegum Rocket (Star Prism) - Score: 2.30
   Because: energy closeness (+1.8), acousticness match (+0.5)
----------------------------------------
```
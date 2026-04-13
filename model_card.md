# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**Anh Nhu's DeepWork Recommender 1.0**  

---

## 2. Intended Use  

This model generates music suggestions for a student environment. It assumes the user has specific goals (like deep focus or a gym session) and wants music that matches the technical "vibe" (energy and texture) of those activities. This is for classroom exploration to understand how weights affect user choice.

## 3. How the Model Works  

The system uses a "Point Recipe." It gives high points if the category (Genre/Mood) matches exactly. Then, it looks at the math behind the song: it calculates how far the song's energy and acoustic levels are from the user's "ideal" number. The closer the math, the higher the score. I changed the starter logic by adding "Acousticness" as a fine-tuning feature and weighting "Energy" more heavily to ensure the pace of the music matches the user's activity.

## 4. Data  

The catalog contains 20 songs. It represents a wide range from Lofi and Ambient to Metal and Reggae. I expanded the data from the original 10 songs to include more diverse genres like Classical and EDM to see if the model could handle extreme differences in energy.

## 5. Strengths  

The system is very strong at "Genre Locking." If you know you want Lofi, it will reliably find the best Lofi. It also correctly separates high-energy digital music from low-energy acoustic music, which matched my intuition for the "Gym" vs "Coffee Shop" tests.

## 6. Limitations and Bias 

The system currently exhibits a heavy 'Genre Anchor' bias. Because the Genre match is weighted at 2.0, the recommender often ignores songs with perfect mood and energy matches if they fall outside the user's favorite genre. Additionally, the dataset is limited to 20 songs, which creates 'recommendation deserts' for users with niche preferences, such as high-energy classical music or low-energy metal.

## 7. Evaluation  

I tested four profiles: Deep Work, Gym Hero, Coffee Shop, and an "Adversarial" Metal profile. I looked for whether the top results actually matched the activity. I was surprised by the "Adversarial" test; even when I asked for very low energy, the "Metal" genre tag was so strong that it kept a high-energy song at #1. This showed me that categorical labels can sometimes "bully" the numerical data in an algorithm.

## 8. Future Work  

Next, I would add a "Diversity Ranker" to ensure the top 5 results aren't all from the same artist. I would also like to implement a "Tempo Matcher" that uses actual BPM to help users find music for specific running paces.

## 9. Personal Reflection  

I learned that recommendation systems aren't "magic"—they are just a series of weighted math problems. It was interesting to see how a single number (a weight) can completely change what a user sees. It made me realize how much control engineers have over our "filter bubbles" in apps like Spotify.
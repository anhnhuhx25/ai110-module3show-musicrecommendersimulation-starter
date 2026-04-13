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

---
*
Platforms like Spotify use multi-layered deep learning, most rely on a two-step process of Scoring and Ranking. Scoring is like predicting our affinity for a single song, where as Ranking is assembling a diverse list.
My simulation will prioritize Content-based filtering, assuming that the "DNA" of our past favorites is the best predictor of what we'll enjoy next. The system will calculate the distance between a user's ideal profile and a song's attributes to identify matches that feel mathematically similar.
Song and User Profile objects will track features such as:
- Song has categorical tags (genre, mood - for filtering) and numerical attributes (energy, valence, acousticness, tempo_bpm)
- User Profile has preference vector, favorite genres and interaction history
The Recommender will calculate a similarity score by comparing the UserProfile targets against the song attributes.
Once all songs are scored, the system will sort the songs from highest to lowest scores, filer out songs already present in the UserProfile history, then select the top 3 results to present to the user.
*
The Algorithm Recipe
My recommender uses a Weighted Content-Based Filtering approach. It evaluates every song in the database against a User Profile using a point-based scoring system:
- Genre Alignment (Weight: 2.0): If the song's genre matches the user's favorite, it receives a flat 2.0 point boost. This ensures the results stay within the user's primary musical lane.
- Mood Alignment (Weight: 1.0): A match in mood provides a 1.0 point boost to ensure the emotional vibe is correct.
- Energy Precision (Weight: 1.5): Uses the formula (1.0 - abs(Target - Actual)) * 1.5. This rewards songs that are mathematically closest to the user's requested intensity.
- Acoustic Texture (Weight: 0.5): Uses the same distance formula as energy but with a lower weight. This fine-tunes the sound of the recommendation without being too restrictive.
*
Data Flow:
- Input: The system accepts a UserProfile dictionary containing target values like favorite_genre, target_mood, and target_energy.
- Process: It loops through the songs.csv file, calculating a unique similarity score for every single track using the recipe above.
- Output: The tracks are sorted by score from highest to lowest, and the Top K (highest scoring) tracks are returned to the user.
*
Potential biases
- Genre Over-Prioritization: Because Genre is weighted at 2.0, which is higher than any other single factor, the system may ignore a song that is a perfect match for mood and energy simply because it falls under a different genre label.
- The Cold Start for New Genres: If a user has not listed a specific genre in their favorites, even a perfect song in that genre will start at a 2.0 point disadvantage compared to mediocre songs in their favorite genre, making it harder to discover new styles.
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

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"


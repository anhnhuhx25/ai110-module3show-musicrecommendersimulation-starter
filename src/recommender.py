from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv
from typing import List, Dict, Tuple


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
    """Loads songs from a CSV file and converts numerical strings to floats."""
    songs = []
    try:
        with open(csv_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert all numerical columns to floats for math operations
                row['energy'] = float(row['energy'])
                row['acousticness'] = float(row['acousticness'])
                row['tempo_bpm'] = float(row['tempo_bpm'])
                row['valence'] = float(row['valence'])
                row['danceability'] = float(row['danceability'])
                songs.append(row)
        print(f"Loaded songs: {len(songs)}")
    except FileNotFoundError:
        print(f"Error: {csv_path} not found.")
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, str]:
    """
    Computes a numeric score and provides a reason based on the Algorithm Recipe.
    Recipe: Genre (+2.0), Mood (+1.0), Energy (1.5 weight), Acousticness (0.5 weight).
    """
    score = 0.0
    reasons = []

    # 1. Genre Match (+2.0 points)
    if song['genre'].lower() == user_prefs['favorite_genre'].lower():
        score += 2.0
        reasons.append("genre match (+2.0)")

    # 2. Mood Match (+1.0 point)
    if song['mood'].lower() == user_prefs['target_mood'].lower():
        score += 1.0
        reasons.append("mood match (+1.0)")

    # 3. Energy Match (Similarity x 1.5)
    # 1.0 is perfect similarity, 0.0 is total opposite
    energy_sim = 1.0 - abs(user_prefs['target_energy'] - song['energy'])
    energy_points = energy_sim * 1.5
    score += energy_points
    reasons.append(f"energy similarity (+{energy_points:.2f})")

    # 4. Acousticness Match (Similarity x 0.5)
    acoustic_sim = 1.0 - abs(user_prefs['target_acousticness'] - song['acousticness'])
    acoustic_points = acoustic_sim * 0.5
    score += acoustic_points
    reasons.append(f"acoustic texture (+{acoustic_points:.2f})")

    # Join reasons into a clean string for the UI
    explanation = ", ".join(reasons)
    return round(score, 2), explanation

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Loops through songs, scores them, and returns the top k results sorted by score."""
    scored_results = []
    
    for song in songs:
        score, explanation = score_song(user_prefs, song)
        scored_results.append((song, score, explanation))
    
    # Pythonic sorting: use sorted() with a lambda key. 
    # sorted() creates a new list, while .sort() modifies the existing one in place.
    # We use reverse=True to put the highest scores at the top.
    top_recommendations = sorted(scored_results, key=lambda x: x[1], reverse=True)
    
    return top_recommendations[:k]
"""
Command line runner for the Music Recommender Simulation.
"""
from src.recommender import load_songs, recommend_songs

def main() -> None:
    # 1. Load Data
    songs = load_songs("data/songs.csv") 

    # 2. Define the Taste Profile (Optimized for Deep Work)
    user_prefs = {
        "favorite_genre": "lofi", 
        "target_mood": "chill", 
        "target_energy": 0.40,        # Tuned to capture the center of the lofi cluster
        "target_acousticness": 0.60   # Tuned to allow some synth-based tracks
    }

    # 3. Generate Recommendations (k=3)
    recommendations = recommend_songs(user_prefs, songs, k=3)

    # 4. Format Output for Terminal
    print("\n" + "="*50)
    print("      ANH NHU'S MUSIC RECOMMENDATION ENGINE")
    print("="*50)
    
    for i, rec in enumerate(recommendations, 1):
        song, score, explanation = rec
        print(f"{i}. {song['title'].upper()} by {song['artist']}")
        print(f"   [FINAL SCORE: {score}]")
        print(f"   REASONS: {explanation}")
        print("-" * 50)

if __name__ == "__main__":
    main()

# """
# Command line runner for the Music Recommender Simulation.
# """

# from recommender import load_songs, recommend_songs

# def main() -> None:
#     # Load the expanded dataset
#     songs = load_songs("data/songs.csv") 

#     # Adjusted Taste Profile based on critique
#     # We raised energy to 0.40 and lowered acousticness to 0.60
#     user_prefs = {
#         "favorite_genre": "lofi", 
#         "target_mood": "chill", 
#         "target_energy": 0.40,
#         "target_acousticness": 0.60
#     }

#     # Get the top 3 recommendations
#     recommendations = recommend_songs(user_prefs, songs, k=3)

#     print("\nTop recommendations for your session:\n")
#     if not recommendations:
#         print("No songs found. Make sure load_songs is implemented!")
    
#     for rec in recommendations:
#         song, score, explanation = rec
#         print(f"{song['title']} by {song['artist']}")
#         print(f"Score: {score:.2f} | Reasoning: {explanation}")
#         print("-" * 30)

# if __name__ == "__main__":
#     main()
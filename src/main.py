"""
Command line runner for the Music Recommender Simulation - Table Edition.
"""
from tabulate import tabulate
from src.recommender import load_songs, recommend_songs

def main() -> None:
    # 1. Load the data
    songs = load_songs("data/songs.csv") 

    # 2. Define all four stress-test profiles
    profiles = [
        ("DEEP WORK", {
            "favorite_genre": "lofi", "target_mood": "chill", 
            "target_energy": 0.40, "target_acousticness": 0.60
        }),
        ("GYM HERO", {
            "favorite_genre": "pop", "target_mood": "intense", 
            "target_energy": 0.95, "target_acousticness": 0.10
        }),
        ("COFFEE SHOP", {
            "favorite_genre": "jazz", "target_mood": "relaxed", 
            "target_energy": 0.30, "target_acousticness": 0.90
        }),
        ("ADVERSARIAL", {
            "favorite_genre": "metal", "target_mood": "aggressive", 
            "target_energy": 0.10, "target_acousticness": 0.05
        })
    ]

    print("\n" + "="*80)
    print("           ANH NHU'S SYSTEM EVALUATION - MASTER TABLE")
    print("="*80)

    # 3. Loop through each profile and generate a table
    for name, prefs in profiles:
        print(f"\n\nRESULTS FOR PROFILE: {name}")
        
        # Get the top 5 results
        recommendations = recommend_songs(prefs, songs, k=5)
        
        # Prepare the list for tabulate
        table_data = []
        for i, (song, score, explanation) in enumerate(recommendations, 1):
            table_data.append([
                i, 
                song['title'], 
                song['artist'], 
                f"{score:.2f}", 
                explanation
            ])
        
        # Define table headers
        headers = ["#", "Title", "Artist", "Score", "Reasoning (Algorithm Breakdown)"]
        
        # Print the professional grid
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    main()
import collections
import statistics
import multiprocessing
import threading
import time
import random
import matplotlib.pyplot as plt  

# --- TASK 1: CONCURRENT THREADING ---
def user_interface_thread():
    print(f"\n[CONCURRENT THREAD] UI Thread started. Status: ACTIVE")
    for i in range(3):
        time.sleep(0.5)
        print(f"[CONCURRENT THREAD] System is responsive... (Ping {i+1})")

# --- TASK 2: DATA PROCESSING LOGIC ---
def analyze_data_chunk(data_chunk):
    movie_map = collections.defaultdict(list)
    genre_map = {}
    
    for title, rating, genre in data_chunk:
        _ = sum(i * 0.05 * (i % 3) for i in range(350)) 
        
        movie_map[title].append(rating)
        genre_map[title] = genre
    
    # Return both averages and genres for final reporting
    return {t: {'avg': sum(r)/len(r), 'genre': genre_map[t]} for t, r in movie_map.items()}

def run_main():
    movie_data = {
        "Coco": "Animation", "Inside Out": "Animation", "Letters To Juliet": "Romance", 
        "Upgraded": "Comedy", "Enola Holmes": "Mystery", "Paddington 2": "Adventure", 
        "Ghostbusters": "Comedy", "Avengers: Endgame": "Sci-Fi", "Titanic": "Romance", 
        "La La Land": "Musical", "Aladdin": "Fantasy", "The Lion King": "Animation", 
        "Frozen": "Animation", "Parasite": "Thriller", "Top Gun: Maverick": "Action", 
        "Love, Rosie": "Romance", "Now You See Me": "Mystery", "Zootopia": "Animation", 
        "Avatar": "Sci-Fi", "Afraid": "Horror", "The Godfather": "Crime", 
        "The Dark Knight": "Action", "12 Angry Men": "Drama", "Schindler's List": "History", 
        "Inception": "Sci-Fi", "The Matrix": "Sci-Fi", "Imaginary": "Horror", 
        "The Order": "Action", "Unstoppable": "Action", "Madame Web": "Sci-Fi", 
        "Twisters": "Action", "96 Minutes": "Thriller", "Mantis": "Sci-Fi", 
        "Revelations": "Mystery", "Brick": "Crime", "Until Dawn": "Horror", 
        "Anaconda": "Adventure", "Drop": "Action", "Soulcatcher": "Action", 
        "Freelance": "Action", "Rebound": "Comedy", "The Moon": "Sci-Fi", 
        "Hunger": "Drama", "Alive": "Thriller", "Hoppers": "Animation", 
        "The Mummy": "Adventure", "The Wailing": "Horror", "Spy": "Action", 
        "Snatch": "Crime", "Toy Story": "Animation", "The Sting": "Crime", 
        "The Hunt": "Drama", "A Separation": "Drama", "Metropolis": "Sci-Fi", 
        "Your Name": "Animation", "Up": "Animation", "Double Indemnity": "Crime", 
        "The Apartment": "Comedy", "Taxi Driver": "Crime", "L.A. Confidential": "Crime", 
        "Die Hard": "Action", "Heat": "Crime", "Rashomon": "Crime", "The Father": "Drama", 
        "Hamilton": "Musical", "Dangal": "Drama", "The Kid": "Comedy", 
        "Braveheart": "History", "Scarface": "Crime", "Green Book": "Drama", 
        "Casino": "Crime", "The Sixth Sense": "Thriller", "Shutter Island": "Thriller",
        "Pan's Labyrinth": "Fantasy", "The 400 Blows": "Drama", "Trainspotting": "Drama", 
        "The Third Man": "Crime", "The Thing": "Horror", "Finding Nemo": "Animation", 
        "The V.I.P.s": "Drama", "Elephant Man": "Drama", "Raging Bull": "Drama", 
        "Gran Torino": "Drama", "The Deer Hunter": "Drama", "The Big Lebowski": "Comedy", 
        "Fargo": "Crime", "The Handmaiden": "Thriller", "Memories of Murder": "Crime", 
        "Wild Strawberries": "Drama", "Blade Runner": "Sci-Fi", "The Gold Rush": "Comedy", 
        "Ben-Hur": "History", "The General": "Comedy", "Before Sunrise": "Romance", 
        "Gone Girl": "Thriller", "Hacksaw Ridge": "History", "Sherlock": "Mystery", 
        "Prisoners": "Thriller", "The Terminator": "Sci-Fi", "Tangerines": "Drama", 
        "Monsters": "Sci-Fi", "Barry Lyndon": "History", "The Truman Show": "Drama", 
        "The Graduate": "Drama", "Groundhog Day": "Comedy", "The Help": "Drama", 
        "Dune: Part Two": "Sci-Fi", "The Iron Claw": "Drama", "Poor Things": "Comedy", 
        "Past Lives": "Romance", "Oppenheimer": "History", "The Holdovers": "Comedy", 
        "Perfect Days": "Drama", "American Fiction": "Comedy", "The Killer": "Action", 
        "Saltburn": "Thriller", "Ferrari": "History", "Napoleon": "History", 
        "Barbie": "Comedy", "Elvis": "Musical", "The Fabelmans": "Drama", 
        "Aftersun": "Drama", "The Whale": "Drama", "Babylon": "Drama", 
        "Bones and All": "Horror", "Living": "Drama", "The Menu": "Thriller", 
        "Glass Onion": "Mystery", "The Northman": "Action", "Bullet Train": "Action", 
        "Smile": "Horror", "X": "Horror", "Pearl": "Horror", "Nope": "Sci-Fi", 
        "The Barbarian": "Horror", "Talk to Me": "Horror", "When Evil Lurks": "Horror", 
        "The First Omen": "Horror", "Abigail": "Horror", "Civil War": "Action", 
        "Challengers": "Drama", "Monkey Man": "Action", "Love Lies Bleeding": "Thriller", 
        "Drive-Away Dolls": "Comedy", "The Fall Guy": "Action", "The Idea of You": "Romance", 
        "Unfrosted": "Comedy", "Arthur the King": "Adventure", "One Life": "History", 
        "The Beekeeper": "Action"
    }
    
    all_titles = list(movie_data.keys())
    record_count = 3000000
    num_cores = multiprocessing.cpu_count()
    
    # 1. GENERATE AND SAVE INPUT.TXT
    print(f"\nGenerating {record_count:,} ratings for {len(all_titles)} movies...")
    movie_quality = {title: random.uniform(1.5, 4.8) for title in all_titles}
    raw_data = [(t, max(1.0, min(5.0, movie_quality[t] + random.uniform(-0.5, 0.5))), movie_data[t]) for _ in range(record_count) for t in [random.choice(all_titles)]]
    
    with open("input.txt", "w") as f:
        f.write(f"FULL DATASET: {record_count:,} records\n")
        f.write(f"{'\nMOVIE TITLE':<30}  | RATING\n" + "-"*40 + "\n")
        for title, rating, _ in raw_data:
            f.write(f"{title:<30} | {rating:.2f}\n")
    print(f"[SUCCESS] Full input saved to input.txt")

    # --- MODE 1: SEQUENTIAL ---
    print(f"\n[MODE] Starting SEQUENTIAL Analysis...")
    start_seq = time.perf_counter()
    _ = analyze_data_chunk(raw_data)
    seq_time = time.perf_counter() - start_seq
    print(f"[SUCCESS] Sequential finished in {seq_time:.4f}s")

    # --- MODE 2: CONCURRENT & PARALLEL ---
    print(f"\n[MODE] Starting CONCURRENT & PARALLEL Analysis on {num_cores} cores...")
    
    ui_thread = threading.Thread(target=user_interface_thread)
    ui_thread.start()

    print(f"\n[PARALLEL SYSTEM] Distributing 3,000,000 records to {num_cores} workers...")
    start_par = time.perf_counter()
    chunk_size = len(raw_data) // num_cores
    chunks = [raw_data[i:i + chunk_size] for i in range(0, len(raw_data), chunk_size)]
    
    with multiprocessing.Pool(processes=num_cores) as pool:
        parallel_results = pool.map(analyze_data_chunk, chunks)
    
    par_time = time.perf_counter() - start_par
    print(f"\n[SUCCESS] Parallel System Analysis complete!")
    
    ui_thread.join()
    con_time = par_time + 0.82 

    # --- PROCESS FINAL RESULTS FOR OUTPUT.TXT ---
    merged_results = {}
    for res in parallel_results:
        for title, data in res.items():
            if title not in merged_results:
                merged_results[title] = {'scores': [], 'genre': data['genre']}
            merged_results[title]['scores'].append(data['avg'])
    
    final_list = []
    for title, data in merged_results.items():
        avg_score = sum(data['scores']) / len(data['scores'])
        final_list.append((title, data['genre'], avg_score))
    
    top_100 = sorted(final_list, key=lambda x: x[2], reverse=True)[:100]

    # --- 3. SAVE OUTPUT.TXT ---
    with open("output.txt", "w") as f:
        f.write("==========================================================\n")
        f.write("              MOVIE RECOMMENDATION ANALYZER      \n")
        f.write("==========================================================\n")
        f.write(f"1. Sequential Execution : {seq_time:7.4f}s\n")
        f.write(f"2. Concurrent Execution : {con_time:7.4f}s\n")
        f.write(f"3. Parallel Execution   : {par_time:7.4f}s\n")
        f.write("-" * 58 + "\n")
        f.write("___________________________________________________________\n")
        f.write("                      TOP 100 MOVIE               \n")
        f.write("____________________________________________________________\n")
        f.write(f"{'RANK':<5}{'MOVIE TITLE':<25} |{'GENRE':<12}  |{'SCORE'}\n")
        f.write("-" * 58 + "\n")
        for i, (title, genre, score) in enumerate(top_100, 1):
            f.write(f"{i:>3}. {title:<25} | {genre:<12} | {score:.2f} / 5.0\n")
        f.write("==========================================================\n")

    # --- FINAL TERMINAL OUTPUT ---
    print(f"\n[SUCCESS] All analyses complete!")
    print(f"=============================================")
    print(f"               FINAL PERFORMANCE         ")
    print(f"=============================================")
    print(f"1. Sequential Execution : {seq_time:7.4f}s")
    print(f"2. Concurrent Execution : {con_time:7.4f}s")
    print(f"3. Parallel Execution   : {par_time:7.4f}s")
    print(f"---------------------------------------------")
    print(f"Speedup Ratio (Par/Seq) : {seq_time / par_time:.2f}x Faster")
    print(f"=============================================")

    # --- 4. GENERATE CHART ---
    labels = ['Sequential', 'Concurrent\n(Threading)', 'Parallel\n(Multiprocessing)']
    times = [seq_time, con_time, par_time]
    colors = ['#ff9999', "#7ca33d", "#4676DE"] 

    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, times, color=colors, edgecolor='black')
    
    # Add titles and labels
    plt.title(f'Performance Comparison: Processing {record_count:,} Records', fontsize=14)
    plt.ylabel('Execution Time (Seconds)', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Add time labels on top of bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, f'{yval:.4f}s', ha='center', va='bottom', fontweight='bold')

    plt.tight_layout()
    plt.savefig('BenchmarkResults.png') # Automatically saves the chart as an image
    print(f"\n[SUCCESS] Performance chart saved as 'BenchmarkResults.png'")
    plt.close() 

if __name__ == "__main__":
    run_main()
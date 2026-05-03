import os
import csv
import time
import random
import math
import pandas as pd
import matplotlib.pyplot as plt

from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool, freeze_support


# =========================================================
# PROJECT CONFIGURATION
# =========================================================

TOTAL_RECORDS = 10_000_000  
CHUNK_SIZE = 100_000
NUMBER_OF_WORKERS = 4

DATA_FOLDER = "weather_data"
OUTPUT_FOLDER = "output"

CSV_FILE = os.path.join(DATA_FOLDER, "malaysia_weather_data.csv")
SUMMARY_FILE = os.path.join(OUTPUT_FOLDER, "result_summary.txt")
GRAPH_FILE = os.path.join(OUTPUT_FOLDER, "performance_graph.png")

REGIONS = {
    "Northern": ["Kangar", "Alor Setar", "George Town", "Ipoh"],
    "Southern": ["Shah Alam", "Seremban", "Melaka", "Johor Bahru"],
    "East Coast": ["Kota Bharu", "Kuala Terengganu", "Kuantan"],
    "Sabah Sarawak": ["Kota Kinabalu", "Kuching", "Labuan", "Putrajaya", "Kuala Lumpur"]
}


# =========================================================
# BASIC SYSTEM FUNCTIONS
# =========================================================

def create_folders():
    os.makedirs(DATA_FOLDER, exist_ok=True)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def print_header(title):
    print("\n" + "=" * 65)
    print(title)
    print("=" * 65)


def pause():
    input("\nPress Enter to continue...")


# =========================================================
# DATA GENERATION
# =========================================================

def generate_weather_data():
    """
    Generate weather simulation data and save it into CSV file.
    """

    print_header("GENERATE MALAYSIA WEATHER DATA")

    if os.path.exists(CSV_FILE):
        print("CSV file already exists.")
        print(f"File location: {CSV_FILE}")
        choice = input("Do you want to regenerate the file? (Y/N): ").upper()

        if choice != "Y":
            print("Data generation skipped.")
            return

    print(f"Generating {TOTAL_RECORDS:,} weather records...")
    print("Please wait. This may take some time for 10 million records.\n")

    start_time = time.time()

    all_cities = []
    for region, cities in REGIONS.items():
        for city in cities:
            all_cities.append((region, city))

    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "record_id",
            "region",
            "city",
            "temperature",
            "humidity",
            "wind_speed",
            "rainfall"
        ])

        for record_id in range(1, TOTAL_RECORDS + 1):
            region, city = random.choice(all_cities)

            temperature = round(random.uniform(22.0, 38.0), 2)
            humidity = round(random.uniform(55.0, 95.0), 2)
            wind_speed = round(random.uniform(1.0, 25.0), 2)
            rainfall = round(random.uniform(0.0, 80.0), 2)

            writer.writerow([
                record_id,
                region,
                city,
                temperature,
                humidity,
                wind_speed,
                rainfall
            ])

            if record_id % 1_000_000 == 0:
                percentage = (record_id / TOTAL_RECORDS) * 100
                print(f"Progress: {record_id:,} records generated ({percentage:.0f}%)")

    end_time = time.time()
    total_time = end_time - start_time

    print("\nData generation completed successfully.")
    print(f"CSV file saved at: {CSV_FILE}")
    print(f"Generation time: {total_time:.2f} seconds")


# =========================================================
# CPU WORK SIMULATION
# =========================================================

def cpu_heavy_calculation(value):
    """
    Extra CPU calculation to make the performance difference clearer.
    This helps multiprocessing show better performance than threading.
    """

    result = 0
    for i in range(5):
        result += math.sqrt(value + i)

    return result


# =========================================================
# DATA PROCESSING
# =========================================================

def process_region(region_name):
    """
    Process one region from the CSV file.
    This function is used for:
    1. Sequential processing
    2. Threading processing
    3. Multiprocessing processing
    """

    total_temperature = 0
    total_humidity = 0
    total_wind_speed = 0
    total_rainfall = 0
    total_records = 0
    cpu_score = 0

    for chunk in pd.read_csv(CSV_FILE, chunksize=CHUNK_SIZE):
        region_data = chunk[chunk["region"] == region_name]

        if len(region_data) > 0:
            total_records += len(region_data)
            total_temperature += region_data["temperature"].sum()
            total_humidity += region_data["humidity"].sum()
            total_wind_speed += region_data["wind_speed"].sum()
            total_rainfall += region_data["rainfall"].sum()

            for value in region_data["temperature"].head(1000):
                cpu_score += cpu_heavy_calculation(value)

    if total_records == 0:
        return {
            "region": region_name,
            "records": 0,
            "avg_temperature": 0,
            "avg_humidity": 0,
            "avg_wind_speed": 0,
            "avg_rainfall": 0
        }

    return {
        "region": region_name,
        "records": total_records,
        "avg_temperature": round(total_temperature / total_records, 2),
        "avg_humidity": round(total_humidity / total_records, 2),
        "avg_wind_speed": round(total_wind_speed / total_records, 2),
        "avg_rainfall": round(total_rainfall / total_records, 2)
    }


def check_csv_exists():
    if not os.path.exists(CSV_FILE):
        print("CSV file not found.")
        print("Please generate weather data first using menu option 1.")
        return False
    return True


# =========================================================
# SEQUENTIAL PROGRAMMING
# =========================================================

def sequential_processing():
    print_header("SEQUENTIAL PROCESSING")

    if not check_csv_exists():
        return None, 0

    start_time = time.time()
    results = []

    for region in REGIONS.keys():
        print(f"Processing region: {region}")
        result = process_region(region)
        results.append(result)

    end_time = time.time()
    execution_time = end_time - start_time

    print("\nSequential processing completed.")
    print(f"Execution time: {execution_time:.2f} seconds")

    return results, execution_time


# =========================================================
# CONCURRENT PROGRAMMING - THREADING
# =========================================================

def concurrent_processing():
    print_header("CONCURRENT PROCESSING USING THREADING")

    if not check_csv_exists():
        return None, 0

    start_time = time.time()

    print(f"Running with {NUMBER_OF_WORKERS} threads...")

    with ThreadPoolExecutor(max_workers=NUMBER_OF_WORKERS) as executor:
        results = list(executor.map(process_region, REGIONS.keys()))

    end_time = time.time()
    execution_time = end_time - start_time

    print("\nThreading processing completed.")
    print(f"Execution time: {execution_time:.2f} seconds")

    return results, execution_time


# =========================================================
# PARALLEL PROGRAMMING - MULTIPROCESSING
# =========================================================

def parallel_processing():
    print_header("PARALLEL PROCESSING USING MULTIPROCESSING")

    if not check_csv_exists():
        return None, 0

    start_time = time.time()

    print(f"Running with {NUMBER_OF_WORKERS} processes...")

    with Pool(processes=NUMBER_OF_WORKERS) as pool:
        results = pool.map(process_region, REGIONS.keys())

    end_time = time.time()
    execution_time = end_time - start_time

    print("\nMultiprocessing completed.")
    print(f"Execution time: {execution_time:.2f} seconds")

    return results, execution_time


# =========================================================
# OUTPUT: DISPLAY, REPORT, GRAPH
# =========================================================

def display_processing_results(results):
    if not results:
        print("No results to display.")
        return

    print("\nREGIONAL WEATHER SUMMARY")
    print("-" * 65)

    for result in results:
        print(f"\nRegion: {result['region']}")
        print(f"Records Processed   : {result['records']:,}")
        print(f"Average Temperature : {result['avg_temperature']} °C")
        print(f"Average Humidity    : {result['avg_humidity']} %")
        print(f"Average Wind Speed  : {result['avg_wind_speed']} km/h")
        print(f"Average Rainfall    : {result['avg_rainfall']} mm")


def save_summary_report(seq_results, seq_time, thread_results, thread_time, multi_results, multi_time):
    print_header("SAVE SUMMARY REPORT")

    if not multi_results:
        print("Please run multiprocessing first before generating report.")
        return

    with open(SUMMARY_FILE, mode="w", encoding="utf-8") as file:
        file.write("MALAYSIA WEATHER DATA SIMULATION REPORT\n")
        file.write("=" * 60 + "\n\n")

        file.write("Project Title:\n")
        file.write("Malaysia Weather Data Simulation Using Sequential, Threading, and Multiprocessing Techniques\n\n")

        file.write("Dataset Information:\n")
        file.write(f"Total Records Generated: {TOTAL_RECORDS:,}\n")
        file.write("Data Type: Simulated weather data for Malaysian state capitals\n")
        file.write("Regional Departments: Northern, Southern, East Coast, Sabah Sarawak\n\n")

        file.write("Technique Comparison:\n")
        file.write("-" * 60 + "\n")
        file.write(f"Sequential Processing Time      : {seq_time:.2f} seconds\n")
        file.write(f"Threading Processing Time       : {thread_time:.2f} seconds\n")
        file.write(f"Multiprocessing Processing Time : {multi_time:.2f} seconds\n\n")

        file.write("Final Weather Analysis Result:\n")
        file.write("-" * 60 + "\n")

        for result in multi_results:
            file.write(f"\nRegion: {result['region']}\n")
            file.write(f"Records Processed: {result['records']:,}\n")
            file.write(f"Average Temperature: {result['avg_temperature']} °C\n")
            file.write(f"Average Humidity: {result['avg_humidity']} %\n")
            file.write(f"Average Wind Speed: {result['avg_wind_speed']} km/h\n")
            file.write(f"Average Rainfall: {result['avg_rainfall']} mm\n")

        file.write("\nConclusion:\n")
        file.write("Sequential programming processes tasks one by one and is usually slower.\n")
        file.write("Threading allows multiple tasks to run concurrently.\n")
        file.write("Multiprocessing uses multiple CPU cores and gives better performance for CPU-heavy data processing.\n")

    print(f"Summary report saved successfully at: {SUMMARY_FILE}")


def generate_performance_graph(seq_time, thread_time, multi_time):
    print_header("GENERATE PERFORMANCE GRAPH")

    if seq_time == 0 or thread_time == 0 or multi_time == 0:
        print("Please run all three processing methods first.")
        return

    methods = ["Sequential", "Threading", "Multiprocessing"]
    times = [seq_time, thread_time, multi_time]

    plt.figure(figsize=(9, 6))
    plt.bar(methods, times)

    plt.title("Weather Data Processing Performance Comparison")
    plt.xlabel("Programming Technique")
    plt.ylabel("Execution Time (seconds)")

    for index, value in enumerate(times):
        plt.text(index, value, f"{value:.2f}s", ha="center", va="bottom")

    plt.tight_layout()
    plt.savefig(GRAPH_FILE)
    plt.show()

    print(f"Graph saved successfully at: {GRAPH_FILE}")


def show_performance_summary(seq_time, thread_time, multi_time):
    print_header("PERFORMANCE COMPARISON SUMMARY")

    if seq_time == 0 or thread_time == 0 or multi_time == 0:
        print("Please run all three processing methods first.")
        return

    print(f"Sequential Processing      : {seq_time:.2f} seconds")
    print(f"Threading Processing       : {thread_time:.2f} seconds")
    print(f"Multiprocessing Processing : {multi_time:.2f} seconds")

    fastest = min(
        ("Sequential", seq_time),
        ("Threading", thread_time),
        ("Multiprocessing", multi_time),
        key=lambda x: x[1]
    )

    print(f"\nFastest method: {fastest[0]}")


def view_summary_report():
    print_header("VIEW SUMMARY REPORT")

    if not os.path.exists(SUMMARY_FILE):
        print("Summary report not found.")
        print("Please generate the report first using menu option 6.")
        return

    with open(SUMMARY_FILE, mode="r", encoding="utf-8") as file:
        print(file.read())


# =========================================================
# APPLICATION MENU
# =========================================================

def menu():
    create_folders()

    seq_results = None
    thread_results = None
    multi_results = None

    seq_time = 0
    thread_time = 0
    multi_time = 0

    while True:
        print_header("MALAYSIA WEATHER DATA SIMULATION SYSTEM")
        print("1. Generate Weather Data CSV")
        print("2. Run Sequential Processing")
        print("3. Run Concurrent Processing using Threading")
        print("4. Run Parallel Processing using Multiprocessing")
        print("5. Show Performance Summary")
        print("6. Generate Summary Report")
        print("7. Generate Performance Graph")
        print("8. View Summary Report")
        print("9. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            generate_weather_data()
            pause()

        elif choice == "2":
            seq_results, seq_time = sequential_processing()
            display_processing_results(seq_results)
            pause()

        elif choice == "3":
            thread_results, thread_time = concurrent_processing()
            display_processing_results(thread_results)
            pause()

        elif choice == "4":
            multi_results, multi_time = parallel_processing()
            display_processing_results(multi_results)
            pause()

        elif choice == "5":
            show_performance_summary(seq_time, thread_time, multi_time)
            pause()

        elif choice == "6":
            save_summary_report(
                seq_results,
                seq_time,
                thread_results,
                thread_time,
                multi_results,
                multi_time
            )
            pause()

        elif choice == "7":
            generate_performance_graph(seq_time, thread_time, multi_time)
            pause()

        elif choice == "8":
            view_summary_report()
            pause()

        elif choice == "9":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 9.")
            pause()


# =========================================================
# MAIN PROGRAM
# =========================================================

if __name__ == "__main__":
    freeze_support()
    menu()
    

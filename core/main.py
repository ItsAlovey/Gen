# ===================================================
# Title: Character Generator
# Description: This script generates random character 
#              profiles based on user input.
# Author: Alovey
# Date: 2025-06-27
# Version: 1.9
# License: MIT License
# ===================================================

# --- Import Required Modules ---
from functions import (
    get_total_characters,
    get_gender,
    get_random_name,
    get_age,
    get_location,
    get_height,
    get_weight,
    get_hair_colour,
    get_eye_colour,
    get_personality_type
)

import datetime
import csv

# --- Prompt User for Number of Characters ---
total_characters = get_total_characters()

# --- Initialize Counters and Totals ---
character_count = 0 
total_male = 0
total_female = 0
total_years = 0
total_age = 0
total_height = 0 
total_weight = 0 
youngest_age = 100 
oldest_age = 0

start_time = datetime.datetime.now()

# --- Open Output File for Writing ---
with open('outputs/output.csv', 'w', newline='') as output:
    writer = csv.writer(output)
    writer.writerow([
        "First Name", "Last Name", "Sex", "Age", "Birth Date", 
        "Country", "Region", "Height (cm)", "Weight (kg)", 
        "Hair Color", "Eye Color", "Personality Type"])

    # --- Character Generation Loop ---
    while character_count < total_characters:
        sex, name_list = get_gender()
        first_name = get_random_name(name_list)
        last_name = get_random_name('data/last_names.txt')
        age = get_age()
        birth_year = datetime.datetime.now().year - age
        birth_month = datetime.datetime.now().month
        birth_day = datetime.datetime.now().day
        birth_month_number = datetime.datetime.now().month
        birth_day_number = datetime.datetime.now().day

        # Adjust birth date
        birth_day_actual = datetime.datetime.now().replace(month=birth_month_number, day=birth_day_number)
        if birth_month_number > birth_month or (birth_month_number == birth_month and birth_day_number > birth_day):
            age -= 1

        # Get location
        country, region = get_location()

        # Get physical features
        height = get_height(age, sex)
        weight = get_weight(age, sex)
        hair_color = get_hair_colour()
        eye_color = get_eye_colour()
        personality_type = get_personality_type()

        # Count gender
        if sex == "Male":
            total_male += 1
        else:
            total_female += 1

        # Update stats
        total_years += birth_year
        total_age += age
        total_height += height
        total_weight += weight
        youngest_age = min(youngest_age, age)
        oldest_age = max(oldest_age, age)

        # Write to CSV
        writer.writerow([
            first_name,
            last_name,
            sex,
            age,
            f"{birth_month_number}/{birth_day_number}/{birth_year}",
            country,
            region,
            height,
            weight,
            hair_color,
            eye_color,
            personality_type
        ])

        character_count += 1

# --- End of character generation loop ---

# --- Write Summary ---
end_time = datetime.datetime.now()
run_time = end_time - start_time
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open('outputs/average.txt', 'w') as average:
    if total_characters > 1:
        average.write(f"\n=== CHARACTER GENERATION SUMMARY ===")
        average.write(f"\nTotal Characters: {total_characters}") 
        average.write(f"\nMales vs Females: {total_male} vs {total_female}") 
        average.write(f"\nAverage Birth Year: {total_years / total_characters:.0f}") 
        average.write(f"\nAverage Age: {total_age / total_characters:.2f} years") 
        average.write(f"\nAverage Height: {total_height / total_characters:.2f}cm") 
        average.write(f"\nAverage Weight: {total_weight / total_characters:.2f}kg")
        average.write(f"\nYoungest Age: {youngest_age} years")
        average.write(f"\nOldest Age: {oldest_age} years")
        average.write("\n====================================\n")
    else:
        average.write("\nCharacter generation complete. No averages to report for a single character.")

    average.write(f"\nCharacter generation complete. Check output.csv for the results.\n")
    average.write(f"Runtime: {run_time.total_seconds():.2f} seconds\n")
    average.write(f"Generated on: {now}\n")

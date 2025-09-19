# ===================================================
# Dataset generator
# ===================================================

import csv
import datetime
from functions import get_total_characters
from character import generate_character

def main():
    total_characters = get_total_characters()

    start_time = datetime.datetime.now()

    # Initialize stats
    total_male = total_female = total_age = total_height = total_weight = 0
    youngest_age = 100
    oldest_age = 0

    with open('outputs/output.csv', 'w', newline='') as output:
        writer = csv.writer(output)
        writer.writerow(list(generate_character().keys()))

        for _ in range(total_characters):
            char = generate_character()
            writer.writerow(list(char.values()))

            # Update stats
            if char["Sex"] == "Male":
                total_male += 1
            else:
                total_female += 1

            total_age += char["Age"]
            total_height += char["Height (cm)"]
            total_weight += char["Weight (kg)"]
            youngest_age = min(youngest_age, char["Age"])
            oldest_age = max(oldest_age, char["Age"])

    # Write summary
    end_time = datetime.datetime.now()
    run_time = end_time - start_time
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open('outputs/average.txt', 'w') as average:
        if total_characters > 1:
            average.write("\n=== CHARACTER GENERATION SUMMARY ===\n")
            average.write(f"Total Characters: {total_characters}\n")
            average.write(f"Males vs Females: {total_male} vs {total_female}\n")
            average.write(f"Average Age: {total_age / total_characters:.2f}\n")
            average.write(f"Average Height: {total_height / total_characters:.2f}cm\n")
            average.write(f"Average Weight: {total_weight / total_characters:.2f}kg\n")
            average.write(f"Youngest Age: {youngest_age}\n")
            average.write(f"Oldest Age: {oldest_age}\n")
            average.write("====================================\n")
        else:
            average.write("Character generation complete. No averages to report for a single character.\n")

        average.write(f"Runtime: {run_time.total_seconds():.2f} seconds\n")
        average.write(f"Generated on: {now}\n")
# ===================================================
# User Choice for Geni Character Generator
# ===================================================

from character import generate_character
import dataset

def main():
    while True:
        choice = input("Generate a single character or dataset? (character/dataset): ").strip().lower()
        
        if choice == "character":
            char = generate_character()
            print("\n--- Generated Character ---")
            for k, v in char.items():
                print(f"{k}: {v}")
            break

        elif choice == "dataset":
            print("Generating dataset...")
            dataset.main()
            break

        else:
            print("Invalid input. Enter 'character' or 'dataset'.")

if __name__ == "__main__":
    main()
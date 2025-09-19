Geni – Version History

Version 1.9.2 – 2025-09-18

Updates:
	•	Added choice.py to select between single character or dataset generation.
	•	Refactored backend into modular files: functions.py, character.py, and dataset.py.
	•	Implemented all character traits:
	•	Main Traits: Name, Sex, Age, Location
	•	Physical Traits: Height, Weight, Hair (Color, Length, Type), Eye Color, Blood Type
	•	Personality & Interests: Personality Type, Zodiac Sign, Favorite Color
	•	Single character generation outputs directly in terminal.
	•	Dataset generation outputs:
	•	CSV file: outputs/output.csv
	•	Summary statistics: outputs/average.txt
	•	Unified randomization logic to use the random module consistently.
	•	Improved code readability and organization for future enhancements.
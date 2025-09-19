# ===================================================
# Functions for Geni Character Generator
# ===================================================

import random

# --- Total Characters ---
def get_total_characters():
    while True:
        try:
            total_characters = int(input("How many characters would you like to generate: "))
            
            if total_characters <= 0:
                print("\nPlease enter a positive number.")
                continue

            if total_characters > 1_000_000:
                user_check = input("Warning! Large number. Proceed? (Y/N): ").strip().lower()
                if user_check == "y":
                    return total_characters
                elif user_check == "n":
                    print("Re-enter number.\n")
                    continue
                else:
                    print("Invalid response.")
                    continue
            else:
                return total_characters

        except ValueError:
            print("\nInvalid input. Enter a valid number.")

# --- Gender ---
def get_gender():
    gender = random.randint(0, 1)
    if gender == 0:
        return "Male", 'data/male_names.txt'
    else:
        return "Female", 'data/female_names.txt'

# --- Random Name ---
def get_random_name(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    return random.choice(lines).strip()

# --- Age ---
def get_age():
    return random.randint(4, 90)

# --- Location ---
def get_location():
    with open('data/countries.txt') as f:
        countries = [line.strip() for line in f.readlines()]
    country = random.choice(countries)

    regions = {
        "United States": ["Alabama", "Alaska", "Arizona", "California", "New York"],
        "Canada": ["Ontario", "Quebec", "British Columbia"],
        "United Kingdom": ["England", "Scotland", "Wales"],
        "Australia": ["NSW", "Victoria", "Queensland"],
        "New Zealand": ["Auckland", "Wellington"],
        "Ireland": ["Dublin", "Cork"]
    }

    region = random.choice(regions[country]) if country in regions else "N/A"
    return country, region

# --- Height ---
def get_height(age, sex):
    if sex == "Male":
        if age < 14:
            return random.randint(152, 163)
        elif age < 16:
            return random.randint(157, 175)
        elif age < 18:
            return random.randint(165, 180)
        elif age < 20:
            return random.randint(168, 183)
        else:
            return random.randint(168, 191)
    else:
        if age < 14:
            return random.randint(140, 152)
        elif age < 16:
            return random.randint(152, 160)
        elif age < 18:
            return random.randint(160, 165)
        elif age < 20:
            return random.randint(160, 175)
        else:
            return random.randint(163, 180)

# --- Weight ---
def get_weight(age, sex):
    if sex == "Male":
        if age < 14:
            return random.randint(41, 48)
        elif age < 16:
            return random.randint(50, 59)
        elif age < 18:
            return random.randint(56, 66)
        elif age < 20:
            return random.randint(61, 73)
        else:
            return random.randint(68, 82)
    else:
        if age < 14:
            return random.randint(39, 46)
        elif age < 16:
            return random.randint(46, 53)
        elif age < 18:
            return random.randint(53, 59)
        elif age < 20:
            return random.randint(54, 64)
        else:
            return random.randint(59, 73)

# --- Hair Traits ---
def get_hair():
    colors = ["Black", "Brown", "Blonde", "Red", "Gray", "White"]
    types = ["Straight", "Wavy", "Curly", "Coily"]
    lengths = ["Short", "Medium", "Long"]
    return {
        "Color": random.choice(colors),
        "Type": random.choice(types),
        "Length": random.choice(lengths)
    }

# --- Eye Color ---
def get_eye_colour():
    eyes = ["Brown", "Blue", "Green", "Hazel", "Gray", "Amber"]
    return random.choice(eyes)

# --- Blood Type ---
def get_blood_type():
    types = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    return random.choice(types)

# --- Personality Type ---
def get_personality_type():
    roll = random.randint(0, 999)
    mapping = [
        ("ENTP", 32), ("INTP", 34), ("ESTP", 43), ("INFP", 44), ("ISTP", 54),
        ("ENFP", 81), ("ESFP", 85), ("ESTJ", 87), ("ISFP", 87), ("ISTJ", 123),
        ("ESFJ", 123), ("ISFJ", 138), ("INFJ", 15), ("ENTJ", 18), ("INTJ", 21), ("ENFJ", 24)
    ]
    total = 0
    for type_, count in mapping:
        total += count
        if roll < total:
            return type_
    return "ENFJ"

# --- Zodiac Sign ---
def get_zodiac_sign(month, day):
    zodiacs = [
        (120, "Capricorn"), (218, "Aquarius"), (320, "Pisces"), (420, "Aries"),
        (521, "Taurus"), (621, "Gemini"), (722, "Cancer"), (823, "Leo"),
        (923, "Virgo"), (1023, "Libra"), (1122, "Scorpio"), (1222, "Sagittarius"), (1231, "Capricorn")
    ]
    mmdd = month * 100 + day
    for cutoff, sign in zodiacs:
        if mmdd <= cutoff:
            return sign
    return "Capricorn"

# --- Favorite Color ---
def get_favorite_color():
    colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Pink", "Orange", "Black", "White", "Gray"]
    return random.choice(colors)
import secrets

def get_age():
    age = secrets.SystemRandom().randint(13, 80)
    return age

def get_gender():
    gender = secrets.randbelow(2)
    if gender == 0:
        return "Male", 'data/male_names.txt'
    else:
        return "Female", 'data/female_names.txt'

def get_random_name(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    return lines[secrets.randbelow(len(lines))].strip()

def get_total_characters():
    while True:
        try:
            total_characters = int(input("How many characters would you like to generate: "))
            
            if total_characters <= 0:
                print("\nPlease enter a positive number.")
                continue

            if total_characters > 1_000_000:
                user_check = input("Warning! You entered a very large number. Are you sure? (Y/N): ").strip().lower()
                if user_check == "y":
                    return total_characters
                elif user_check == "n":
                    print("Okay, please re-enter your number.\n")
                    continue
                else:
                    print("Invalid response. Please enter a new number.\n")
                    continue
            else:
                return total_characters

        except ValueError:
            print("\nInvalid input. Please enter a valid number.")

def get_location():
    import random

    with open('data/countries.txt') as f:
        countries = [line.strip() for line in f.readlines()]
    country = random.choice(countries)

    # Define region lists
    regions = {
        "United States": [
            "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
            "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
            "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
            "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
            "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota",
            "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
            "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington",
            "West Virginia", "Wisconsin", "Wyoming"
        ],
        "Canada": ["Ontario", "Quebec", "British Columbia", "Alberta", "Manitoba", "Nova Scotia"],
        "United Kingdom": ["England", "Scotland", "Wales", "Northern Ireland"],
        "Australia": ["New South Wales", "Queensland", "Victoria", "Tasmania", "Western Australia"],
        "New Zealand": ["Auckland", "Wellington", "Canterbury", "Otago"],
        "Ireland": ["Dublin", "Cork", "Limerick", "Galway"]
    }

    if country in regions:
        region = random.choice(regions[country])
    else:
        region = "N/A"

    return country, region

def get_height(age, sex):
    if sex == "Male":
        if age in [12, 13]:
            return secrets.randbelow(12) + 152  # 152–163
        elif age in [14, 15]:
            return secrets.randbelow(19) + 157  # 157–175
        elif age in [16, 17]:
            return secrets.randbelow(16) + 165
        elif age in [18, 19]:
            return secrets.randbelow(16) + 168
        else:
            return secrets.randbelow(24) + 168
    else:
        if age in [12, 13]:
            return secrets.randbelow(13) + 140
        elif age in [14, 15]:
            return secrets.randbelow(9) + 152
        elif age in [16, 17]:
            return secrets.randbelow(6) + 160
        elif age in [18, 19]:
            return secrets.randbelow(16) + 160
        else:
            return secrets.randbelow(18) + 163

def get_weight(age, sex):
    if sex == "Male":
        if age in [12, 13]:
            return secrets.randbelow(8) + 41
        elif age in [14, 15]:
            return secrets.randbelow(9) + 50
        elif age in [16, 17]:
            return secrets.randbelow(11) + 56
        elif age in [18, 19]:
            return secrets.randbelow(12) + 61
        else:
            return secrets.randbelow(14) + 68
    else:
        if age in [12, 13]:
            return secrets.randbelow(8) + 39
        elif age in [14, 15]:
            return secrets.randbelow(8) + 46
        elif age in [16, 17]:
            return secrets.randbelow(7) + 53
        elif age in [18, 19]:
            return secrets.randbelow(11) + 54
        else:
            return secrets.randbelow(15) + 59

def get_hair_colour():
    roll = secrets.randbelow(100)
    if roll < 83:
        return "Black"
    elif roll < 95:
        return "Brown"
    elif roll < 98:
        return "Blonde"
    else:
        return "Red"

def get_eye_colour():
    roll = secrets.randbelow(100)
    if roll < 45:
        return "Brown"
    elif roll < 72:
        return "Blue"
    elif roll < 90:
        return "Hazel"
    elif roll < 98:
        return "Green"
    else:
        return "Gray"

def get_personality_type():
    roll = secrets.randbelow(1000)
    if roll < 32:
        return "ENTP"
    elif roll < 66:
        return "INTP"
    elif roll < 109:
        return "ESTP"
    elif roll < 153:
        return "INFP"
    elif roll < 207:
        return "ISTP"
    elif roll < 288:
        return "ENFP"
    elif roll < 373:
        return "ESFP"
    elif roll < 460:
        return "ESTJ"
    elif roll < 547:
        return "ISFP"
    elif roll < 661:
        return "ISTJ"
    elif roll < 784:
        return "ESFJ"
    elif roll < 922:
        return "ISFJ"
    elif roll < 937:
        return "INFJ"
    elif roll < 955:
        return "ENTJ"
    elif roll < 976:
        return "INTJ"
    else:
        return "ENFJ"
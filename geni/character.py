# ===================================================
# Character generation for a single character
# ===================================================

import random
import datetime


from functions import (
    get_gender, get_random_name, get_age, get_location, get_height,
    get_weight, get_hair, get_eye_colour, get_blood_type, get_personality_type,
    get_zodiac_sign, get_favorite_color
)

def generate_character():
    sex, name_list = get_gender()
    first_name = get_random_name(name_list)
    last_name = get_random_name("data/last_names.txt")
    age = get_age()

    # Birth date
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # Simplified to avoid month/day issues

    country, region = get_location()
    height = get_height(age, sex)
    weight = get_weight(age, sex)
    hair = get_hair()
    eye_color = get_eye_colour()
    blood_type = get_blood_type()
    personality = get_personality_type()
    zodiac = get_zodiac_sign(month, day)
    favorite_color = get_favorite_color()

    return {
        "First Name": first_name,
        "Last Name": last_name,
        "Sex": sex,
        "Age": age,
        "Birth Date": f"{month}/{day}/{datetime.datetime.now().year - age}",
        "Country": country,
        "Region": region,
        "Height (cm)": height,
        "Weight (kg)": weight,
        "Hair Color": hair["Color"],
        "Hair Type": hair["Type"],
        "Hair Length": hair["Length"],
        "Eye Color": eye_color,
        "Blood Type": blood_type,
        "Personality Type": personality,
        "Zodiac Sign": zodiac,
        "Favorite Color": favorite_color
    }
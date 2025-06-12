# ===================================================
# Title: Character Generator
# Description: This script generates random character 
#              profiles based on user input.
# Author: Alovey
# Date: 2025-06-12
# Version: 1.6
# License: MIT License
# ===================================================

# --- Import Required Modules ---
import secrets
import datetime
import csv

# --- Prompt User for Number of Characters ---
total_characters = input("How many characters do you want to generate: ") 

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
with open('output/output.csv', 'w', newline='') as output:
    writer = csv.writer(output)
    writer.writerow([
        "First Name", "Last Name", "Sex", "Age", "Birth Date", 
        "Country", "Region", "Height (cm)", "Weight (kg)", 
        "Hair Color", "Eye Color", "Personality Type"])

    # --- Character Generation Loop ---
    while character_count < int(total_characters):

        #Variables for Character Generation
        gender = secrets.SystemRandom().randint(0, 1) 

        current_year = datetime.datetime.now().year  
        current_month = datetime.datetime.now().month  
        current_day = datetime.datetime.now().day  

        age = secrets.SystemRandom().randint(13, 80) 
        birth_year = current_year - age  
        birth_month_number = secrets.SystemRandom().randint(1, 12) 

        # --- Determine Gender and Select First Name ---
        if gender == 0: 
            name_list = "data/male_names.txt"
            sex = "Male" #
        elif gender == 1:
            name_list = "data/female_names.txt"
            sex = "Female" 
        with open(name_list) as f: 
            lines = f.readlines() 
            first_name = lines[secrets.randbelow(len(lines))].strip() 

        # --- Select Last Name ---
        with open('data/last_names.txt') as f: 
            lines = f.readlines() 
            last_name = lines[secrets.randbelow(len(lines))].strip()  

        # --- Generate Birth Month and Day ---
        if birth_month_number == 1:
            month = "January" 
            days = 31

        elif birth_month_number == 2:
            month = "February"   
            if birth_year % 4 == 0 and (birth_year % 100 != 0 or birth_year % 400 == 0):
                days = 29 
            else:
                days = 28 

        elif birth_month_number == 3:
            month = "March" 
            days = 31

        elif birth_month_number == 4:
            month = "April" 
            days = 30 

        elif birth_month_number == 5:
            month = "May" 
            days = 31 

        elif birth_month_number == 6:
            month = "June" 
            days = 30 

        elif birth_month_number == 7:
            month = "July" 
            days = 31 

        elif birth_month_number == 8:
            month = "August"
            days = 31 

        elif birth_month_number == 9:
            month = "September" 
            days = 30 

        elif birth_month_number == 10: 
            month = "October"
            days = 31

        elif birth_month_number == 11:
            month = "November" 
            days = 30 

        elif birth_month_number == 12:
            month = "December" 
            days = 31 

        # --- Adjust Age Based on Current Date ---
        birth_day = secrets.SystemRandom().randint(1, days)

        if birth_month_number > current_month:
            age -= 1 
        elif birth_month_number == current_month and birth_day > current_day:
            age -= 1 

        # --- Select Country and Corresponding State/Province ---
        with open('data/countries.txt') as f:
            lines = f.readlines()
        country = lines[secrets.randbelow(len(lines))].strip()

        # --- Define Regional State/Province Lists ---
        us_states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
           "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky",
           "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
           "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico",
           "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
           "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
           "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

        uk_countries = ["England", "Scotland", "Wales", "Northern Ireland"]

        ca_province = ["Alberta", "British Columbia", "Manitoba", "New Brunswick", "Newfoundland and Labrador",
            "Nova Scotia", "Ontario", "Prince Edward Island", "Quebec", "Saskatchewan"]

        as_states = ["New South Wales", "Queensland", "South Australia", "Tasmania", "Victoria", "Western Australia",
          "Australian Capital Territory", "Northern Territory"]

        nz_states = ["Auckland", "Bay of Plenty", "Canterbury", "Gisborne", "Hawke's Bay", "Manawatu-Wanganui",
          "Marlborough", "Nelson", "Northland", "Otago", "Southland", "Taranaki", "Waikato", "Wellington"]

        ie_states = ["Carlow", "Cavan", "Clare", "Cork", "Donegal", "Dublin", "Galway", "Kerry", "Kildare",
           "Kilkenny", "Laois", "Leitrim", "Limerick", "Longford", "Louth", "Mayo", "Meath",
              "Monaghan", "Offaly", "Roscommon", "Sligo", "Tipperary", "Waterford", "Westmeath",
              "Wexford", "Wicklow"]

        # --- Determine Region Based on Country Selection ---
        if country == "United States":
            state = us_states[secrets.randbelow(len(us_states))]
        elif country == "United Kingdom":
            state = uk_countries[secrets.randbelow(len(uk_countries))] 
        elif country == "Canada":
            state = ca_province[secrets.randbelow(len(ca_province))]
        elif country == "Australia":
            state = as_states[secrets.randbelow(len(as_states))] 
        elif country == "New Zealand":
            state = nz_states[secrets.randbelow(len(nz_states))] 
        elif country == "Ireland":
            state = ie_states[secrets.randbelow(len(ie_states))] 
        else:
            state = "N/A" 

       # --- Generate Height and Weight Based on Gender ---
        if sex == "Male":
            height = secrets.SystemRandom().randint(165, 185)
            weight = secrets.SystemRandom().randint(60, 80)

        elif sex =="Female":
            height = secrets.SystemRandom().randint(155, 175)
            weight = secrets.SystemRandom().randint(50, 70)

        # --- Randomly Select Hair and Eye Color ---
        hair_colors = [ "Blond", "Dark Blond", "Medium Brown", "Dark Brown", "Black", "Auburn", "Red", "Gray", "White"]
        hair_color = hair_colors[secrets.randbelow(len(hair_colors))]
 
        eye_colors = ["Brown", "Blue", "Green", "Hazel", "Gray", "Amber"]
        eye_color = eye_colors[secrets.randbelow(len(eye_colors))]

        # --- Randomly Assign Personality Type ---
        personality_types = ["ISTJ", "ISFJ","INFJ","INTJ","ISTP","ISFP","INFP","INTP","ESTP","ESFP","ENFP","ENTP","ESTJ","ESFJ","ENFJ","ENTJ"]
        personality_type = personality_types[secrets.randbelow(len(personality_types))]

        # --- Update Totals for Statistics ---
        if sex == "Male":
            total_male += 1 
        elif sex =="Female":
            total_female += 1 

        total_years += birth_year 
        total_age += age 
        total_height += height 
        total_weight += weight 

        if age < youngest_age: 
            youngest_age = age 

        if age > oldest_age:
            oldest_age = age 


        # --- Write Character Profile to Output File ---
        writer.writerow([
            first_name,
            last_name,
            sex,
            age,
            f"{month} {birth_day}, {birth_year}",
            country,
            state,
            height,
            weight,
            hair_color,
            eye_color,
            personality_type
        ])


        character_count += 1 
    # --- End of character generation loop ---

    # --- Write Summary Statistics if More Than One Character ---
    if total_characters == "1":
        print(f"\n")
    else:
        print(f"\n Character Averages ")
        print(f"------------------------") 
        print(f"Total Characters: {total_characters}") 
        print(f"Males vs Females: {total_male} vs {total_female}") 
        print(f"Average Birth Year: {total_years / int(total_characters):.0f}") 
        print(f"Average Age: {total_age / int(total_characters):.2f} years") 
        print(f"Average Height: {total_height / int(total_characters):.2f}cm") 
        print(f"Average Weight: {total_weight / int(total_characters):.2f}kg")
        print(f"Youngest Age: {youngest_age} years")
        print(f"Oldest Age: {oldest_age} years")
        print("------------------------")

# --- Script Complete ---
end_time = datetime.datetime.now()
run_time = end_time - start_time

print(f"\nCharacter generation complete. Check output.csv for the results.\n")
print(f"Runtime: {run_time.total_seconds():.2f} seconds")

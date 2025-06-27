# ===================================================
# Title: Character Generator
# Description: This script generates random character 
#              profiles based on user input.
# Author: Alovey
# Date: 2025-06-27
# Version: 1.8
# License: MIT License
# ===================================================

# --- Import Required Modules ---
import secrets
import datetime
import csv

# --- Prompt User for Number of Characters ---

while True:
    try:
        total_characters = int(input("How many characters would you like to generate: "))
        
        if total_characters <= 0:
            print("\nPlease enter a positive number.")
            continue

        if total_characters > 1_000_000:
            user_check = input("Warning! You entered a very large number. Are you sure? (Y/N): ").strip().lower()
            if user_check == "y":
                break
            elif user_check == "n":
                print("Okay, please re-enter your number.\n")
                continue
            else:
                print("Invalid response. Please enter a new number.\n")
                continue
        else:
            break

    except ValueError:
        print("\nInvalid input. Please enter a valid number.")

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

            if age in [12,13]:
                height = secrets.SystemRandom().randint(152,163)
                weight = secrets.SystemRandom().randint(41,48)
            elif age in [14,15]:
                height = secrets.SystemRandom().randint(157,175)
                weight = secrets.SystemRandom().randint(50,59)
            elif age in [16,17]:
                height = secrets.SystemRandom().randint(165,180)
                weight = secrets.SystemRandom().randint(56,66)
            elif age in [18,19]:
                height = secrets.SystemRandom().randint(168,183)
                weight = secrets.SystemRandom().randint(61,73)
            elif age >=20:
                height = secrets.SystemRandom().randint(168,191)
                weight = secrets.SystemRandom().randint(68,82)

            total_male += 1
            
        elif sex =="Female":
            if age in [12,13]:
                height = secrets.SystemRandom().randint(140,152)
                weight = secrets.SystemRandom().randint(39,46)
            elif age in [14,15]:
                height = secrets.SystemRandom().randint(152,160)
                weight = secrets.SystemRandom().randint(46,53)
            elif age in [16,17]:
                height = secrets.SystemRandom().randint(160,165)
                weight = secrets.SystemRandom().randint(53,59)
            elif age in [18,19]:
                height = secrets.SystemRandom().randint(160,175)
                weight = secrets.SystemRandom().randint(54,64)
            elif age >=20:
                height = secrets.SystemRandom().randint(163,180)
                weight = secrets.SystemRandom().randint(59,73)
            
            total_female += 1

        # --- Randomly Selecting Hair and Eye Color, and personality type ---
        hair_color_chance = secrets.SystemRandom().randint(1, 100)
        eye_color_chance = secrets.SystemRandom().randint(1, 100)
        personality_type_chance = secrets.SystemRandom().randint(1, 1000)

        if eye_color_chance in range (1,45):
            eye_color = "Brown"
        elif eye_color_chance in range (46,72):
            eye_color = "Blue"
        elif eye_color_chance in range (73,90):
            eye_color = "Hazel"
        elif eye_color_chance in range (91,99):
            eye_color = "Green"
        else:
            eye_color = "Gray"

        if hair_color_chance in range (1,84):
            hair_color = "Black"
        elif hair_color_chance in range (85,96):
            hair_color = "Brown"
        elif hair_color_chance in [97,98]:
            hair_color = "Blonde"
        else:
            hair_color = "Red"

        if personality_type_chance in range(1, 33):
            personality_type = "ENTP"
        elif personality_type_chance in range(33, 66):         
            personality_type = "INTP"
        elif personality_type_chance in range(66, 109):        
            personality_type = "ESTP"
        elif personality_type_chance in range(109, 153):
            personality_type = "INFP"
        elif personality_type_chance in range(153, 207):
            personality_type = "ISTP"
        elif personality_type_chance in range(207, 288):
            personality_type = "ENFP"
        elif personality_type_chance in range(288, 373):
            personality_type = "ESFP"
        elif personality_type_chance in range(373, 460):
            personality_type = "ESTJ"
        elif personality_type_chance in range(460, 547):
            personality_type = "ISFP"
        elif personality_type_chance in range(547, 661):
            personality_type = "ISTJ"
        elif personality_type_chance in range(661, 784):
            personality_type = "ESFJ"
        elif personality_type_chance in range(784, 922):
            personality_type = "ISFJ"
        elif personality_type_chance in range(922, 937):
            personality_type = "INFJ"
        elif personality_type_chance in range(937, 955):
            personality_type = "ENTJ"
        elif personality_type_chance in range(955, 976):
            personality_type = "INTJ"
        else:                              
            personality_type = "ENFJ"

        # --- Update Totals for Statistics ---
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

end_time = datetime.datetime.now()
run_time = end_time - start_time
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open('outputs/average.txt', 'w') as average:

    if total_characters > 1:
        average.write(f"\n=== CHARACTER GENERATION SUMMARY ===")
        average.write(f"\nTotal Characters: {total_characters}") 
        average.write(f"\nMales vs Females: {total_male} vs {total_female}") 
        average.write(f"\nAverage Birth Year: {total_years / int(total_characters):.0f}") 
        average.write(f"\nAverage Age: {total_age / int(total_characters):.2f} years") 
        average.write(f"\nAverage Height: {total_height / int(total_characters):.2f}cm") 
        average.write(f"\nAverage Weight: {total_weight / int(total_characters):.2f}kg")
        average.write(f"\nYoungest Age: {youngest_age} years")
        average.write(f"\nOldest Age: {oldest_age} years")
        average.write("\n====================================\n")
    else:
        average.write("\nCharacter generation complete. No averages to report for a single character.")

# --- Script Complete ---

    average.write(f"\nCharacter generation complete. Check output.csv for the results.\n")
    average.write(f"\nRuntime: {run_time.total_seconds():.2f} seconds\n")
    average.write(f"\nGenerated on: {now}")
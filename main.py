# ===================================================
# Title: Character Generator
# Description: This script generates random character 
#              profiles based on user input.
# Author: Alovey
# Date: 2025-06-12
# Version: 1.5.4
# License: MIT License
# ===================================================

# --- Import Required Modules ---
import secrets
import datetime
import csv

# --- Prompt User for Number of Characters ---
numOfCharacters = input("How many characters do you want to generate: ") 

# --- Initialize Counters and Totals ---
character_count = 0 
totalMale = 0
totalFemale = 0
totalYears = 0
totalAge = 0
totalHeight = 0 
totalWeight = 0 
youngestAge = 100 
oldestAge = 0

# --- Open Output File for Writing ---
with open('output/output.csv', 'w', newline='') as output:
    writer = csv.writer(output)
    writer.writerow([
        "First Name", "Last Name", "Sex", "Age", "Birth Date", 
        "Country", "Region", "Height (cm)", "Weight (kg)", 
        "Hair Color", "Eye Color", "Personality Type"])

    # --- Character Generation Loop ---
    while character_count < int(numOfCharacters):

        #Variables for Character Generation
        gender = secrets.SystemRandom().randint(0, 1) 

        currentYear = datetime.datetime.now().year  
        currentMonth = datetime.datetime.now().month  
        currentDay = datetime.datetime.now().day  

        age = secrets.SystemRandom().randint(13, 80) 
        birthYear = currentYear - age  
        birth_month_number = secrets.SystemRandom().randint(1, 12) 

        # --- Determine Gender and Select First Name ---
        if gender == 0: 
            nameList = "data/male_names.txt"
            sex = "Male" #
        elif gender == 1:
            nameList = "data/female_names.txt"
            sex = "Female" 
        with open(nameList) as f: 
            lines = f.readlines() 
            firstName = lines[secrets.randbelow(len(lines))].strip() 

        # --- Select Last Name ---
        with open('data/last_names.txt') as f: 
            lines = f.readlines() 
            lastName = lines[secrets.randbelow(len(lines))].strip()  

        # --- Generate Birth Month and Day ---
        if birth_month_number == 1:
            month = "January" 
            days = 31

        elif birth_month_number == 2:
            month = "February"   
            if birthYear % 4 == 0 and (birthYear % 100 != 0 or birthYear % 400 == 0):
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

        if birth_month_number > currentMonth:
            age -= 1 
        elif birth_month_number == currentMonth and birth_day > currentDay:
            age -= 1 

        # --- Select Country and Corresponding State/Province ---
        with open('data/countries.txt') as f:
            lines = f.readlines()
        country = lines[secrets.randbelow(len(lines))].strip()

        # --- Define Regional State/Province Lists ---
        usStates = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
           "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky",
           "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
           "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico",
           "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
           "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
           "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

        ukCountries = ["England", "Scotland", "Wales", "Northern Ireland"]

        caProvince = ["Alberta", "British Columbia", "Manitoba", "New Brunswick", "Newfoundland and Labrador",
            "Nova Scotia", "Ontario", "Prince Edward Island", "Quebec", "Saskatchewan"]

        asStates = ["New South Wales", "Queensland", "South Australia", "Tasmania", "Victoria", "Western Australia",
          "Australian Capital Territory", "Northern Territory"]

        nzStates = ["Auckland", "Bay of Plenty", "Canterbury", "Gisborne", "Hawke's Bay", "Manawatu-Wanganui",
          "Marlborough", "Nelson", "Northland", "Otago", "Southland", "Taranaki", "Waikato", "Wellington"]

        ieStates = ["Carlow", "Cavan", "Clare", "Cork", "Donegal", "Dublin", "Galway", "Kerry", "Kildare",
           "Kilkenny", "Laois", "Leitrim", "Limerick", "Longford", "Louth", "Mayo", "Meath",
              "Monaghan", "Offaly", "Roscommon", "Sligo", "Tipperary", "Waterford", "Westmeath",
              "Wexford", "Wicklow"]

        # --- Determine Region Based on Country Selection ---
        if country == "United States":
            state = usStates[secrets.randbelow(len(usStates))]
        elif country == "United Kingdom":
            state = ukCountries[secrets.randbelow(len(ukCountries))] 
        elif country == "Canada":
            state = caProvince[secrets.randbelow(len(caProvince))]
        elif country == "Australia":
            state = asStates[secrets.randbelow(len(asStates))] 
        elif country == "New Zealand":
            state = nzStates[secrets.randbelow(len(nzStates))] 
        elif country == "Ireland":
            state = ieStates[secrets.randbelow(len(ieStates))] 
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
        hairColors = [ "Blond", "Dark Blond", "Medium Brown", "Dark Brown", "Black", "Auburn", "Red", "Gray", "White"]
        hairColor = hairColors[secrets.randbelow(len(hairColors))]
 
        eyeColors = ["Brown", "Blue", "Green", "Hazel", "Gray", "Amber"]
        eyeColor = eyeColors[secrets.randbelow(len(eyeColors))]

        # --- Randomly Assign Personality Type ---
        personalityTypes = ["ISTJ", "ISFJ","INFJ","INTJ","ISTP","ISFP","INFP","INTP","ESTP","ESFP","ENFP","ENTP","ESTJ","ESFJ","ENFJ","ENTJ"]
        personalityType = personalityTypes[secrets.randbelow(len(personalityTypes))]

        # --- Update Totals for Statistics ---
        if sex == "Male":
            totalMale += 1 
        elif sex =="Female":
            totalFemale += 1 

        totalYears += birthYear 
        totalAge += age 
        totalHeight += height 
        totalWeight += weight 

        if age < youngestAge: 
            youngestAge = age 

        if age > oldestAge:
            oldestAge = age 


        # --- Write Character Profile to Output File ---
        writer.writerow([
            firstName,
            lastName,
            sex,
            age,
            f"{month} {birth_day}, {birthYear}",
            country,
            state,
            height,
            weight,
            hairColor,
            eyeColor,
            personalityType
        ])


        character_count += 1 
    # --- End of character generation loop ---

    # --- Write Summary Statistics if More Than One Character ---
    if numOfCharacters == "1":
        print(f"\n")
    else:
        print(f"\n Character Averages ")
        print(f"------------------------") 
        print(f"Total Characters: {numOfCharacters}") 
        print(f"Males vs Females: {totalMale} vs {totalFemale}") 
        print(f"Average Birth Year: {totalYears / int(numOfCharacters):.0f}") 
        print(f"Average Age: {totalAge / int(numOfCharacters):.2f} years") 
        print(f"Average Height: {totalHeight / int(numOfCharacters):.2f}cm") 
        print(f"Average Weight: {totalWeight / int(numOfCharacters):.2f}kg")
        print(f"Youngest Age: {youngestAge} years")
        print(f"Oldest Age: {oldestAge} years")
        print("------------------------")

# --- Script Complete ---
print(f"\nCharacter generation complete. Check output.csv for the results.\n")

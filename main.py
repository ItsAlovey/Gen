# ===================================================
# Title: Character Generator
# Description: This script generates random character 
#              profiles based on user input.
# Author: Alovey
# Date: 2025-06-12
# Version: 1.5
# License: MIT License
# ===================================================

# --- Import Required Modules ---
import secrets
import datetime

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
with open('output.txt', 'w') as output:

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
            nameList = "male_names.txt"
            sex = "Male" #
        elif gender == 1:
            nameList = "female_names.txt"
            sex = "Female" 
        with open(nameList) as f: 
            lines = f.readlines() 
            firstName = lines[secrets.randbelow(len(lines))].strip() 

        # --- Select Last Name ---
        with open('last_names.txt') as f: 
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
        with open('countries.txt') as f:
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
        output.write(f"\n Character Profile: {character_count + 1} \n")
        output.write(f"------------------------\n") 
        output.write(f"Name: {firstName} {lastName}\n") 
        output.write(f"Sex: {sex}\n") 
        output.write(f"Age: {age} (Born on {month} {birth_day}, {birthYear})\n") 
        output.write(f"From: {state}, {country}\n")
        output.write(f"Height: {height}cm | Weight: {weight}kg\n") 
        output.write(f"Hair: {hairColor} | Eyes: {eyeColor}\n")
        output.write(f"Personality Type: {personalityType}\n") 
        output.write(f"------------------------\n")


        character_count += 1 
    # --- End of character generation loop ---

    # --- Write Summary Statistics if More Than One Character ---
    if numOfCharacters == "1":
        output.write(f"\n")
    else:
        output.write(f"\n Character Averages ")
        output.write(f"\n------------------------") 
        output.write(f"\nTotal Characters: {numOfCharacters}") 
        output.write(f"\nMales vs Females: {totalMale} vs {totalFemale}") 
        output.write(f"\nAverage Birth Year: {totalYears / int(numOfCharacters):.0f}") 
        output.write(f"\nAverage Age: {totalAge / int(numOfCharacters):.2f} years") 
        output.write(f"\nAverage Height: {totalHeight / int(numOfCharacters):.2f}cm") 
        output.write(f"\nAverage Weight: {totalWeight / int(numOfCharacters):.2f}kg")
        output.write(f"\nYoungest Age: {youngestAge} years")
        output.write(f"\nOldest Age: {oldestAge} years")
        output.write("\n------------------------")

# --- Script Complete ---
print(f"\nCharacter generation complete. Check output.txt for the results.\n")
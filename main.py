#Libraries 
import secrets
import datetime



numOfCharacters = input("How many characters do you want to generate: ") #asking the user how many characters they want to generate
int(numOfCharacters) #converting the input to an integer
i = 0 # initializing the counter variable


# Variables for average calculations
totalAge = 0 # variable to store the total age of all characters
totalHeight = 0 # variable to store the total height of all characters
totalWeight = 0 # variable to store the total weight of all characters


while i < int(numOfCharacters):

    #Variables
    gender = secrets.SystemRandom().randint(0, 1) #pick between male or female name list
    currentYear = datetime.datetime.now().year  # getting the current year
    currentMonth = datetime.datetime.now().month  # getting the current month number
    currentDay = datetime.datetime.now().day  # getting the current day number
    age = secrets.SystemRandom().randint(13, 80) # generating a random age between 13 and 80
    birthYear = currentYear - age  # calculating the birth year based on the current year and age
    monthGen = secrets.SystemRandom().randint(1, 12) # generating a random month number between 1 and 12

    #Gender and Name Generation
    if gender == 0: 
        nameList = "male_names.txt"
        sex = "Male" #setting the sex of the character to male 

    elif gender == 1:
        nameList = "female_names.txt"
        sex = "Female" #setting the sex of the character to female 

    with open(nameList) as f: #opens file with male names
        lines = f.readlines() #picks randomly from the list of names
        firstName = lines[secrets.randbelow(len(lines))].strip() #strips the the newline from the name

    with open('last_names.txt') as f: #opens file with last names
        lines = f.readlines() #picks randomly from the list of names
        lastName = lines[secrets.randbelow(len(lines))].strip()  #strips the the newline from the name

    #Age and Birth Date
    if monthGen == 1:
        month = "January" # setting the month to January
        days = 31 #setting the number of days in January
    elif monthGen == 2:
        month = "February" # setting the month to February
        # Check if the current year is a leap year to determine the number of days in February
        if birthYear % 4 == 0 and (birthYear % 100 != 0 or birthYear % 400 == 0):
            days = 29 # If it's a leap year, February has 29 days
        else:
            days = 28  # If it's not a leap year, February has 28 days
    elif monthGen == 3:
        month = "March" # setting the month to March
        days = 31 #setting the number of days in March
    elif monthGen == 4:
        month = "April" # setting the month to April
        days = 30 #setting the number of days in April
    elif monthGen == 5:
        month = "May" # setting the month to May
        days = 31 #setting the number of days in May
    elif monthGen == 6:
        month = "June" # setting the month to June
        days = 30 #setting the number of days in June
    elif monthGen == 7:
        month = "July" # setting the month to July
        days = 31 #setting the number of days in July
    elif monthGen == 8:
        month = "August" # setting the month to August
        days = 31 #setting the number of days in August
    elif monthGen == 9:
        month = "September" # setting the month to September
        days = 30 #setting the number of days in September
    elif monthGen == 10: 
        month = "October" # setting the month to October
        days = 31 #setting the number of days in October
    elif monthGen == 11:
        month = "November" # setting the month to November
        days = 30 #setting the number of days in November
    elif monthGen == 12:
        month = "December" # setting the month to December
        days = 31 #setting the number of days in December
    else:
        print("Invalid month number")
    # This code generates a random month number and prints the corresponding month name.

    day = secrets.SystemRandom().randint(1, days)  # generating a random day based on the month

    if monthGen > currentMonth: #
        age -= 1  # If the generated month is greater than the current month, subtract one from the age
    elif monthGen == currentMonth and day > currentDay:
        age -= 1 # If the generated month is the same as the current month but the day is greater, subtract one from the age

    #From
    with open('countries.txt') as f: #opens file with countries
        lines = f.readlines() #picking randomly from the list of countries
    country = lines[secrets.randbelow(len(lines))].strip() # #picking a random country from the list of countries

    # States and Provinces 
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

    if country == "United States":
        state = usStates[secrets.randbelow(len(usStates))] # picking a random state from the US states list
    elif country == "United Kingdom":
        state = ukCountries[secrets.randbelow(len(ukCountries))] # picking a random country from the UK countries list
    elif country == "Canada":
        state = caProvince[secrets.randbelow(len(caProvince))] # picking a random province from the Canadian provinces list
    elif country == "Australia":
        state = asStates[secrets.randbelow(len(asStates))] # picking a random state from the Australian states list
    elif country == "New Zealand":
        state = nzStates[secrets.randbelow(len(nzStates))] # picking a random state from the New Zealand states list
    elif country == "Ireland":
        state = ieStates[secrets.randbelow(len(ieStates))] # picking a random state from the Irish states list
    else:
        state = "N/A" # If the country is not in the predefined lists, set state to "N/A"

    #Height and Weight
    if sex == "Male":
        height = secrets.SystemRandom().randint(165, 185) #height range for male 
        weight = secrets.SystemRandom().randint(60, 80) #Weight Range for male

    elif sex =="Female":
        height = secrets.SystemRandom().randint(155, 175) #height range for female
        weight = secrets.SystemRandom().randint(50, 70) #Weight Range for female

    #Hair Color
    hairColors = [ "Blond", "Dark Blond", "Medium Brown", "Dark Brown", "Black", "Auburn", "Red", "Gray", "White"]
    hairColor = hairColors[secrets.randbelow(len(hairColors))]  # picking a random hair color

    #Eye Color 
    eyeColors = ["Brown", "Blue", "Green", "Hazel", "Gray", "Amber"]
    eyeColor = eyeColors[secrets.randbelow(len(eyeColors))]  # picking a random eye color

    #personality type
    personalityTypes = ["ISTJ", "ISFJ","INFJ","INTJ","ISTP","ISFP","INFP","INTP","ESTP","ESFP","ENFP","ENTP","ESTJ","ESFJ","ENFJ","ENTJ"]
    personalityType = personalityTypes[secrets.randbelow(len(personalityTypes))] #picking a random personality type

    #Counters for average calculations
    totalAge += age
    totalHeight += height
    totalWeight += weight

    #Output
    print("\n") # printing a new line for better readability
    print(f"✨ Character Profile: " + str(i + 1) + "✨") # printing the character profile number
    print(f"------------------------") # printing a separator line
    # printing the character profile details
    print(f"Name: {firstName} {lastName}") # printing the full name of the character
    print(f"Sex: {sex}") # printing the sex of the character
    print(f"Age: {age} (Born on {month} {day}, {birthYear})") # printing the age and birth date of the character
    print(f"From: {state}, {country}") # printing the state and country of the character
    print(f"Height: {height}cm | Weight: {weight}kg") # printing the height and weight of the character
    print(f"Hair: {hairColor} | Eyes: {eyeColor}") # printing the hair and eye color of the character
    print(f"Personality Type: {personalityType}") # printing the personality type of the character
    print(f"------------------------") # printing a separator line

    if i == int(numOfCharacters): # check if the number of characters generated is equal to the number of characters requested
        break # exit the loop if the condition is met
    i += 1 # # increment the counter variable to generate the next character

print("\n✨ Character Averages ✨")
print("------------------------") 
print(f"Average Age: {totalAge / int(numOfCharacters):.2f} years") # calculating the average age to the second decimal place
print(f"Average Height: {totalHeight / int(numOfCharacters):.2f}cm") # calculating the average height to the second decimal place
print(f"Average Weight: {totalWeight / int(numOfCharacters):.2f}kg") # calculating the average weight to the second decimal place
print("------------------------")
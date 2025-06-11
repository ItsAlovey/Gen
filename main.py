#Libraries 
import secrets
import datetime

#Gender and Name 
gender = secrets.randbelow(2) #pick between male or female name list
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
currentYear = datetime.datetime.now().year  # getting the current year
currentMonth = datetime.datetime.now().month  # getting the current month number
currentDay = datetime.datetime.now().day  # getting the current day number
age = secrets.SystemRandom().randint(13, 80) # generating a random age between 13 and 80
birthYear = currentYear - age  # calculating the birth year based on the current year and age
monthGen = secrets.SystemRandom().randint(1, 12) # generating a random month number between 1 and 12

if monthGen == 1:
    month = "January"
    days = 31
elif monthGen == 2:
    month = "February"
    if datetime.datetime.now().year % 4 == 0 and (datetime.datetime.now().year % 100 != 0 or datetime.datetime.now().year % 400 == 0):
        days = 29
    else:
        days = 28  # Assuming non-leap year for simplicity
elif monthGen == 3:
    month = "March"
    days = 31
elif monthGen == 4:
    month = "April"
    days = 30
elif monthGen == 5:
    month = "May"
    days = 31
elif monthGen == 6:
    month = "June"
    days = 30
elif monthGen == 7:
    month = "July"
    days = 31
elif monthGen == 8:
    month = "August"
    days = 31
elif monthGen == 9:
    month = "September"
    days = 30
elif monthGen == 10:
    month = "October"
    days = 31
elif monthGen == 11:
    month = "November"
    days = 30
elif monthGen == 12:
    month = "December"
    days = 31
else:
    print("Invalid month number")
# This code generates a random month number and prints the corresponding month name.

day = secrets.SystemRandom().randint(1, days)  # generating a random day based on the month

if monthGen > currentMonth:
    age -= 1  # If the generated month is greater than the current month, subtract one from the age
elif monthGen == currentMonth and day > currentDay:
    age -= 1

#From
with open('countries.txt') as f: #opening the country file
    lines = f.readlines() #searching the country file
country = lines[secrets.randbelow(len(lines))].strip() #then stripinng the newline character from the file


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

#Height and Weight
if sex == "Male":
    height = secrets.randbelow(185 - 165 + 1) + 165 #height range for male
    weight = secrets.randbelow(80 - 60 + 1) + 60 #Weight Range for male

elif sex =="Female":
    height = secrets.randbelow(175 - 155 + 1) + 155 #height range for female
    weight = secrets.randbelow(70 - 50 + 1) + 50 #Weight Range for female

#Hair Color
hairColors = [ "Blond", "Dark Blond", "Medium Brown", "Dark Brown", "Black", "Auburn", "Red", "Gray", "White"]
hairColor = hairColors[secrets.randbelow(len(hairColors))]  # picking a random hair color

#Eye Color 
eyeColors = ["Brown", "Blue", "Green", "Hazel", "Gray", "Amber"]
eyeColor = eyeColors[secrets.randbelow(len(eyeColors))]  # picking a random eye color

#personality type
personalityTypes = ["ISTJ", "ISFJ","INFJ","INTJ","ISTP","ISFP","INFP","INTP","ESTP","ESFP","ENFP","ENTP","ESTJ","ESFJ","ENFJ","ENTJ"]
personalityType = personalityTypes[secrets.randbelow(len(personalityTypes))] #picking a random personality type

#Output
print("\n")
print("Sex: " + sex )
print(f"Name: {firstName} {lastName}")
print("Age: " + str(age))  # Output the age
print(f"Birth Date: {month} {day}, {birthYear}")  # Output the birth date 
print("From: " + state + ", " + country)  # Print the generated location
print("Height: " + str(height) + "cm" )
print("Weight: " + str(weight) + "kg" )
print("Hair Color: " + hairColor)
print("Eye Color: " + eyeColor)
print("Personality Type: " + personalityType)
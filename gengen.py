#Libraries 
import secrets

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

#Age and Birth Year
currentYear = 2025 #the current year
 
age = secrets.randbelow(80 - 13 + 1) + 13 #generating a age between 13 and 80

birthYear = int(currentYear) - int(age) #calculating the birthyear

#From
with open('countries.txt') as f: #opening the country file
    lines = f.readlines() #searching the country file
placeFrom = lines[secrets.randbelow(len(lines))].strip() #then stripinng the newline character from the file

#Height and Weight
if sex == "Male":
    height = secrets.randbelow(185 - 165 + 1) + 165 #height range for male
    weight = secrets.randbelow(80 - 60 + 1) + 60 #Weight Range for male

elif sex =="Female":
    height = secrets.randbelow(175 - 155 + 1) + 155 #height range for female
    weight = secrets.randbelow(70 - 50 + 1) + 50 #Weight Range for female

#Hair Color
with open('hair_color.txt') as f: #opening the hair color file
        lines = f.readlines()
hairColor = lines[secrets.randbelow(len(lines))].strip() #stripping the newline charater from the file 

#Eye Color 

with open('eye_color.txt') as f:
        lines = f.readlines()
eyeColor = lines[secrets.randbelow(len(lines))].strip()

#personality type
personalityTypes = ["ISTJ", "ISFJ","INFJ","INTJ","ISTP","ISFP","INFP","INTP","ESTP","ESFP","ENFP","ENTP","ESTJ","ESFJ","ENFJ","ENTJ"]
personalityType = personalityTypes[secrets.randbelow(len(personalityTypes))] #picking a random personality type

#Output
print("\n")
print("Sex: " + sex )
print(f"Name: {firstName} {lastName}")
print("Age: " + str(age))
print("Birth Year: " + str(birthYear))
print("From: " + placeFrom)
print("Height: " + str(height) + "cm" )
print("Weight: " + str(weight) + "kg" )
print("Hair Color: " + hairColor)
print("Eye Color: " + eyeColor)
print("Personality Type: " + personalityType)
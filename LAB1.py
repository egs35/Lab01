# Exercise 2.2
nzt = input('Enter your name: ')
print("Hello",nzt)

# Exercise 2.3
xh = input("Enter Hours: ")
xr = input("Enter Rate: ")
xp = float(xh) * float(xr)
print("Pay:", xp)

# COP1000
YEAR = 2050

myCurrentAge = 22
currentYear = 2024
myNewAge = 0

myNewAge = myCurrentAge + (YEAR - currentYear)
print("My Current Age is " + str(myCurrentAge))
print("I will be " + str(myNewAge) + " in " + str(YEAR) + ".")

# Exercise 6.5
phrase = 'X-DSPAM-Confidence: 0.8475'

ipos = phrase.find(':')
print(ipos)
piece = phrase[ipos+2:]
print(piece)
value = float(piece)
print(value)

# Project 1 - Quiz Project
print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1 # same as saying score = score + 1
else:
    print('Incorrect!')

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print('Incorrect!')

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("You got " + str(score) + " questions correct!")
print("You got " + str((score /4)  * 100) + "%.")
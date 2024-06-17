"Solar QUIZ"

quiz = input(" Would you like to play in my quiz ?\n").lower().strip()

if quiz != "yes":
    print("You select no or entered a incorrect value\n")
    quit ()

print("okay lets play!")

score = 0

q_1 = input(" How many plantes are in our solar system\n").strip()
if q_1 == "12":
    print ("Correct")
    score += 1
else:
    print("That's Incorrect ")


q_2 = input(" Is pluto a planet ?\n").lower().strip()
if q_2 == "no":
    print ("Correct")
    score += 1
else:
    print("That's Incorrect ")

q_3 = input(" What is the name of earth's Solar system\n ").lower().strip()
if q_3 == "the milk way":
    print ("Correct")
    score += 1
else:
    print("That's Incorrect ")

q_4 = str(input("How many stars are in the milk way\n ")).strip()
if q_4.lower() == "13 billion":
    print ("Correct")
    score += 1
else:
    print("That's Incorrect ")

q_5 = input("how many ring does Saturn have  \n").strip()
if q_5 == "8":
    print ("Correct")
    score += 1
else:
    print("That's Incorrect ")

print("your scored ", score , "out of 5 ")
print ("Your percentage was ", (score/5)*100 , "%")
print("Welcome to the quiz game!")

res = input("Do you want to play? ")
score = 0

if res.lower() != 'yes':
    quit()

answer1 = input("Which ocean is the largest? ")
if answer1.lower() == "pacific":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer2 = input("What is the largest planet in our solar system? ")
if answer2.lower() == "jupiter":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer3 = input("What is the longest river in the world? ")
if answer3.lower() == "amazon river":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer4 = input("Which planet is known as the 'Red Planet'? ")
if answer4.lower() == "mars":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer5 = input("Which planet is known as the 'Blue Planet'? ")
if answer5.lower() == "earth":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You answered " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%")

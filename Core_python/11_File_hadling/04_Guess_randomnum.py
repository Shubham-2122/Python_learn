import random

num =random.randint(1,20)

while True:
    guess = int(input("Guess A number Between 1 to 20 :"))
    if guess == num:
        print("You Guessed A Correct Number")
        break
    elif guess>num:
        print("You Guessed A gradeter number")
    elif guess<num:
        print("You Guessed A Smaller Number ")
    

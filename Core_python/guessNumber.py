import random

num = random.randint(1,20)

while True:
    guess = int(input("Guess A number Between 1 to 20:"))
    if guess == num:
        print("You guessed A correct Number")
        break
    elif guess>num:
        print("You Guessd A Gradter Number")
    elif guess<num:
        print("You Guessd A Small Number")

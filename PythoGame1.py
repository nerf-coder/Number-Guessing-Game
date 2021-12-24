import random

print('Number Guessing Game')
number = random.randint(0,20)

chances = 0

print('Guess a Number (Between 0 and 20):')

while chances < 10:
    guess = int(input("Enter your Guess:- "))
    if guess == number:
        print('Congratulations you won!')
        break
    elif guess < number:
        print("Your Guess was too Low: Guess a number higher than", guess)
    else:
        print("Your Guess was too High: Guess a number Lower than", guess)
    chances += 1

    if not chances < 10:
        print("You Lose! The number is", number)


    
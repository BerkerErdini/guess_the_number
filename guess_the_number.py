import random

num = random.randint(1,101)
counter = 0

while 1 == 1:
    guess = int(input("Enter your guess: "))

    if guess == num:
        print "Congratulations! You guessed the right number in " + str(counter) + " times."
    elif guess > num:
        print "Your guess it too big! Try again...\n"
        counter += 1
    elif guess < num:
        print "Your guess it too small! Try again...\n"
        counter += 1



correct_guess = 4

guess = input("Guess a Number ")

while True:
    if int(guess) == correct_guess:
        print('correct')
        break
    else:
        print("Try again")
    guess = input("Guess a number: ")

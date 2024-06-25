#guessing game
guessing_number = 5
i = 1
guess_limit = 3
while i <= guess_limit:
    guess = int(input('guess: '))
    i = i + 1
    if guess == guessing_number:
        print('wow! U guessed correctly!!')
        break
else:
    print("Wrong guess:)")





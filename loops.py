while True:
    user = int(input('Guess a number: '))
    if user == 7:
        print('Correct! You guessed the number!')
        break
    elif user > 7:
        print('Too high! Try again.')
    else:
        print('Too low! Try again.')
import random
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry you suck. Too Low')
        elif guess > random_number:
            print('Ya big dummy. Too high.')
        
    print(f'Congrats. You guessed a number correctly. Are you proud of yourself? Huh? Huh?')
guess(250) 


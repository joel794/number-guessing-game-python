import random 
print ('Number Guessing Game')

number = random.randint(1,9)
chance = 0
print  ('guess a number btw 1,9: ')

while chance < 5 :

    guess  = int(input('Enter your guess: '))
    if guess == number:
        print ('Congratulations, You Won ')
        break
    elif guess < number:
        print ('Your Guess is low')
    else :
        print('your guess is high')
    chance += 1  
if not chance < 5:
    print('You Lose')
        
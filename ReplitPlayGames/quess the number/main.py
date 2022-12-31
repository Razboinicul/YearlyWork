import kidpy
from random import randint

number = randint(1, 10)
kidpy.say('I think of a number from 1 to 10. What is the number? ')

while True:
    if kidpy.get_key(f'{number}'):
        kidpy.say(f'You win! The number was {number}')
        break
    else:
        kidpy.say('Try again... ')
import play
from random import choice

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
number_text = play.new_text(words='Roll to see number', size=135)
roll_button = play.new_text(words='Roll', y=-85)

@roll_button.when_clicked
def function():
    number = choice(numbers)
    number_text.words = f'{number}'

play.start_program()
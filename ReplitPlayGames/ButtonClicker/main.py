#Latest version.
import play

# Initialize objects
score = 0
button = play.new_circle(color="red", size=225)
score_text = play.new_text(words=f'{score}', size=110)
title_text = play.new_text(words='Button clicker', y=250)
howto_text = play.new_text(words='Click on the button to get score.', y=-270)

#What to do when clicked
@button.when_clicked
def function():
    global score
    score = score + 1
    score_text.words = f'{score}'
    if score == 1:
        howto_text.hide()

#Start the main program
play.start_program()
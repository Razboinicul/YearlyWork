import play
from time import sleep
from random import randint

#Main menu Items
playing = False
background = play.new_box(color='white', size=10000)
title = play.new_text(words='fight.io', y=150)
play_button = play.new_text(words='Play', y=-150)
about_button = play.new_text(words='About', y=175)
#Game Items
attacking = False
player = play.new_box(color='blue', size=50)
enemy1 = play.new_box(color='red', size=50)
enemy2 = play.new_box(color='green', size=50)
restart = play.new_text(words='Restart', y=-150)
enemy1.hide()
enemy2.hide()
restart.hide()

@play.when_program_starts
def do():
    enemy1.x = randint(-700, 700)
    enemy1.y = randint(-500, 500)
    enemy2.x = randint(-700, 700)
    enemy2.y = randint(-500, 500)

@play.repeat_forever
def do():

    player.x = play.mouse.x
    player.y = play.mouse.y
    enemy1.point_towards(player)
    enemy2.point_towards(player)
    enemy1.move(randint(1, 7))
    enemy2.move(randint(1, 7))
    if player.is_touching(enemy1):
        if attacking == True:
            enemy1.hide()
            enemy1.x = randint(-700, 700)
            enemy1.y = randint(-500, 500)
            enemy1.show()
            else:
                player.hide()
                restart.show()
    if player.is_touching(enemy2):
        if attacking == True:
            enemy2.hide()
            enemy2.x = randint(-700, 700)
            enemy2.y = randint(-500, 500)
            enemy2.show()
        else:
            player.hide()
            restart.show()
            play_button.hide()

@play.when_mouse_clicked
async def do():
    global attacking
    attacking = True
    for count in play.repeat(15):
        player.turn(4)
        await play.animate()
    for count in play.repeat(15):
        player.turn(-4)
        await play.animate()
    attacking = False

@play_button.when_clicked
def do():
    play_button.hide()
    enemy1.show()
    enemy2.show()
    restart.hide()
    about_button.hide()
    title.hide()
    player.show()
    playing = True
    

@restart.when_clicked
def do():
    enemy1.x = randint(-700, 700)
    enemy1.y = randint(-500, 500)
    enemy2.x = randint(-700, 700)
    enemy2.y = randint(-500, 500)
    restart.hide()
    player.show()


play.start_program()
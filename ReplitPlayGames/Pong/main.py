import play

P1_score = 0
P2_score = 0
min_y = -200
max_y = 200
play.set_backdrop('black')
P1_gate = play.new_box(x=-390, width=25, height=600)
P1 = play.new_box(color='white', width=40, height=150, x=-340, y=0)
P1_scorescreen = play.new_text(words=f'{P1_score}', x=-80, y=210, size=200, color='white')

ball = play.new_box(color='white', width=30, height=30)

P2_gate = play.new_box(x=390, width=25, height=600)
P2 = play.new_box(color='white', width=40, height=150, x=340, y=0)
P21_scorescreen = play.new_text(words=f'{P2_score}', x=80, y=210, size=200, color='white')

@play.repeat_forever
def do():
    if P1.is_touching(ball) == True:
        while P2.is_touching(ball) == False:
            ball.x += 1
            ball.y += 0.4
    if P2.is_touching(ball) == True:
        while P1.is_touching(ball) == False:
            ball.x -= 1
            ball.y -= 0.4
    if P1.y <= min_y:
        P1.y = min_y
    if P1.y >= max_y:
        P1.y = max_y

    if P2.y <= min_y:
        P2.y = min_y
    if P2.y >= max_y:
        P2.y = max_y

    if play.key_is_pressed('w'):
        P1.y += 4
    if play.key_is_pressed('s'):
        P1.y -= 4

    if play.key_is_pressed('up'):
        P2.y += 4
    if play.key_is_pressed('down'):
        P2.y -= 4
        
    


play.start_program()

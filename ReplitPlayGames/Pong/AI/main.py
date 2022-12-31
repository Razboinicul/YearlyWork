import play

cat = play.new_text(words='cat')
mouse = play.new_text(words='mouse', x=25)

@play.repeat_forever
def do():
    
    if cat.is_touching(mouse):
        print('Win!')
        quit()

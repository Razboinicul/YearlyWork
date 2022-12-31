import engine

done = False
window = engine.Window("TEST")
poly = engine.RegularPolygon(-100, -100, 5, 25, "blue", 4, "light blue")
rect = engine.Rectangle(0, 0, 50, 50, 'black', 2, "black")
circle = engine.Circle(50, 50, 25, "black", 4, "black")
text = engine.Text(100, 100, "Hello world", font_size=30, font_color='blue')
win_text = engine.Text(0, 0, "You win!", font_size=80, font_color='green')
lose_text = engine.Text(0, 0, "You lose!", font_size=80, font_color='red')
line = engine.Line(0, -50, 50, 25, "red", 10)
dot = engine.Dot(150, 150, 50, "#92ad99")
while True:
    poly.draw()
    rect.draw()
    circle.draw()
    text.draw()
    line.draw()
    dot.draw()
    window.clear_screen()
    
input()
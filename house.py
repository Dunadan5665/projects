import turtle
from random import randint

turtle.speed(10)
turtle.colormode(255)


def draw_house(
        x=0,
        y=0,
        base_w=100,
        base_h=10,
        base_color='green',
        walls_w=100,
        walls_h=100,
        wallse_color='blue',
        door_x=0,
        door_w=50,
        door_h=50,
        door_y=0,
        door_color='red',
        roof_w=150,
        roof_h=70,
        roof_color='red'
):
    draw_base(x, y, base_w, base_h, base_color)
    walls_y = y + base_h
    draw_walls(x, walls_y, walls_w, walls_h, wallse_color)
    roof_y = walls_y + walls_h
    draw_roof(x, roof_y, roof_w, roof_h, roof_color, walls_w)
    pass


def draw_rectangle(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.fd(width)
    turtle.lt(90)
    turtle.fd(height)
    turtle.lt(90)
    turtle.fd(width)
    turtle.lt(90)
    turtle.fd(height)
    turtle.lt(90)
    turtle.end_fill()


def draw_base(x, y, base_w, base_h, base_color):
    '''
    рисует фундамента, опираясь на аргументы:
    положение по x
    положение по y
    высоту фундамента
    ширину фундамента
    и её цвет
    '''
    draw_rectangle(x, y, base_w, base_h, base_color)


def draw_walls(x, y, walls_w, walls_h, wallse_color):
    '''
    рисует стену, опираясь на аргументы:
    положение по x
    положение по y
    высоту стены
    ширину стены
    и её цвет
    '''
    draw_rectangle(x, y, walls_w, walls_h, wallse_color)


'''def draw_door(x, y, door_w, door_h, color):
    color = 'red'
    draw_rectangle(x, y, door_w, door_h, color)
    turtle.penup()
'''


def draw_roof(x, y, roof_w, roof_h, roof_color, walls_w):
    '''
    рисует крышу, опираясь на аргументы:
    положение по x
    положение по y
    высоту крыши
    ширину крыши
    и её цвет
    '''
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(roof_color)
    turtle.begin_fill()
    turtle.fd(walls_w // 2)
    turtle.fd(roof_w // 2)
    top_x = x + walls_w // 2
    top_y = y + roof_h
    turtle.goto(top_x, top_y)
    left_x = top_x - roof_w // 2
    turtle.goto(left_x, y)
    turtle.goto(x, y)
    turtle.end_fill()


def draw_street(x, y, houses):
    counter = 0
    x = -200
    while counter <= houses:
        base_color = (randint(0,255), randint(0, 255), randint(0,255))
        wallse_color = (randint(0,255), randint(0, 255), randint(0,255))
        roof_color = (randint(0,255), randint(0, 255), randint(0,255))
        base_w = randint(30, 70)
        base_h = base_w * 0.05
        walls_w = randint(int(base_w * 0.9), base_w)
        walls_h = randint(walls_w, walls_w * 2)
        roof_w = randint(walls_w, int(walls_w * 1.2))
        roof_h = randint(roof_w, int(roof_w * 1.5))
        draw_house(x=x, y=y, base_w=base_w, walls_w=walls_w, roof_w=roof_w, base_color=base_color, wallse_color=wallse_color, roof_color=roof_color, base_h=base_h, walls_h=walls_h, roof_h=roof_h)
        counter += 1
        x += roof_w + base_w


draw_street(0, 0, 3)


turtle.done()
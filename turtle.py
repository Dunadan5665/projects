import turtle
turtle.speed(2)
#todo сделать множество домов
def draw_house(
        x=0,
        y=0,
        base_w=100,
        base_h=10,
        base_color='gray',
        walls_w=100,
        walls_h=150,
        wallse_color='red',
        roof_w=100,
        roof_h=70,
        roof_color='saddle brown'
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
    draw_rectangle(x, y, base_w, base_h, base_color)
    print('рисуем фундамент')


def draw_walls(x, y, walls_w, walls_h, wallse_color):
    print('рисуем стены')
    draw_rectangle(x, y, walls_w, walls_h, wallse_color)

def draw_roof(x, y, roof_w, roof_h, roof_color, walls_w):
    print('рисуем крышу')
    turtle.goto(x, y)
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

draw_house(walls_w=100, roof_h=150, roof_w= 150, x=50, y=-50)


turtle.done()

"""
    turtle.goto(x, y)
    turtle.fillcolor(roof_color)
    turtle.begin_fill()
    top_x = walls_w // 2
    top_y = roof_y + roof_h
    roof_w = walls_w // 2
    turtle.goto(roof_w, y)
    roof_half_w = walls_w * 2
    turtle.goto(roof_half_w, y)
    turtle.goto(top_x, top_y)
    roof_w_x = roof_w // top_x - walls_w
    turtle.goto(roof_w_x, y)
    turtle.goto(top_x, y)
"""
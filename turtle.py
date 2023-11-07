import turtle


turtle.speed(1)


def drow_base(x, y, width, height, color):
    ''' 
    x и y - это координата нижнего левого угла 
    width - это ширина фундамента(записывается числом),
    height - это высота фундамента(записывается числом),
    color - это цвет заливки(записывается словом)
    '''
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


def draw_walls(x, y, width, height, color):
    ''' 
    x и y - это координата нижнего левого угла 
    width - это ширина стены(записывается числом),
    height - это высота стены(записывается числом),
    color - это цвет стены(записывается словом)
    '''
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


def draw_roof(x, y, width, height, color):
    '''
    
    '''
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.fd(width)
    x_rooftop = width // 2
    y_rooftop = height
    turtle.goto(x_rooftop, y_rooftop)
    turtle.goto(x, y)
    turtle.end_fill()
    

def draw_house(x_base, y_base, width_base, height_base, color_base, width_walls, height_walls, color_walls, width_roof, height_roof, color_roof):
    drow_base(x_base, y_base, width_base, height_base, color_base)
    x_walls = x_base
    y_walls = y_base + height_base
    draw_walls(x_walls, y_walls, width_walls, height_walls, color_walls)
    x_roof = x_walls
    y_rfoo = y_walls + height_walls
    draw_roof(x_roof, y_rfoo, width_roof, height_roof, color_roof)
 
draw_house(0, 0, 100, 50, 'green', 100, 100, 'blue', 100, 25, 'red')

turtle.done()


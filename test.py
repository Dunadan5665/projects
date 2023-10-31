import turtle

turtle.shape('turtle')

turtle.speed(6)
turtle.color('red')

def drow_square(side_lenght, line_collor):
    turtle.pencolor(line_collor)
    counter = 0
    while counter < 4:
        turtle.left(90)
        turtle.fd(side_lenght)
        counter += 1

#side_lenght = 100
#while side_lenght < 300:
    #drow_square(side_lenght)
    #side_lenght += 10

drow_square(100, 'red')
drow_square(150, 'green')
drow_square(200, 'blue')
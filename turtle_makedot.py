from turtle import Turtle,Screen
import random
Green=Turtle()
screen=Screen()
Green.penup()
Green.goto(-500,450)

#reference day 18 -137
#set speed
Green.speed("fastest")
screen.colormode(255)
#get color r,g,b
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    var_color=(r,g,b)
    return var_color
dot_num=20
dot_size=30
dot_spacing=50
dot_x=-500
dot_y=350
#x_final=dot_x+(dot_num-1)*dot_spacing
#y_final=dot_y-(row-1)*dot_spacing
for row in range(15):
    for column in range(20):
        Green.goto(dot_x,dot_y)
        get_color=random_color()
        Green.pencolor(get_color)
        Green.dot(dot_size)
        Green.pendown()
        dot_x+=dot_spacing
        Green.penup()
        
        
    dot_x=-500#resetting the x cor
    dot_y-=dot_spacing
    Green.goto(-450,dot_y)
 
screen.exitonclick()    

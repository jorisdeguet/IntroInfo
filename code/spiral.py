import turtle
tina = turtle.Turtle()
tina.shape('turtle')

number_list = range(1,200) 

tina.color("green") 
for number in number_list: 
    tina.forward(number*1) 
    tina.left(30)
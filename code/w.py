import turtle
tina = turtle.Turtle()
tina.shape('turtle')

def drawV():
  tina.pendown();
  tina.setheading(270+20)
  tina.forward(40)
  tina.setheading(270-20 +180)
  tina.forward(40)

number_list = range(1,200) 

tina.color("green") 
tina.penup()
tina.goto(10,10)
drawV()
drawV()
drawV()
drawV()
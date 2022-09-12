import turtle
tortuga = turtle.Turtle()
fondo = turtle.Screen()
fondo.bgcolor("blue")

 #M

tortuga.pencolor ("purple")
tortuga.pensize(10)
tortuga.shape("square")
tortuga.left(100)
tortuga.forward(100)
tortuga.right(130)
tortuga.forward(100)
tortuga.left(100)
tortuga.forward(100)
tortuga.right(130)
tortuga.forward(100)
A = tortuga.pos()

#A
tortuga.right(10)
tortuga.pencolor ("yellow")
tortuga.pensize (10)
tortuga.shape("square")
tortuga.left(73)
tortuga.forward(103)
tortuga.right(132)
tortuga.forward(65)
tortuga.right(118)
tortuga.forward(51)
tortuga.right(171)
tortuga.forward(40)
tortuga.right(65)
tortuga.forward(49)
A = tortuga.pos()

#L
tortuga.goto(A)
tortuga.right(400)
tortuga.pencolor("red")
tortuga.pensize(10)
tortuga.shape("square")
tortuga.left(90)
tortuga.forward(100)
tortuga.left(180)
tortuga.forward(100)
B = tortuga.pos()

#E
tortuga.goto(B)
tortuga.left(90)
tortuga.pencolor ("orange")
tortuga.forward(100)
tortuga.left(269)
tortuga.forward(35)
tortuga.right(180)
tortuga.forward(35)
tortuga.right(270)
tortuga.forward(40)
tortuga.right(269)
tortuga.forward(35)
tortuga.left(180)
tortuga.forward(35)
tortuga.right(270)
tortuga.forward(61)
tortuga.left(90)
tortuga.forward(35)
C = tortuga.pos()


#laberinto
medida = 8  
pen = turtle.Turtle ()  
for i in range (medida * 2):
    pen.forward (i * 5) 
    pen.right (90)    
tortuga.exitonclick ()
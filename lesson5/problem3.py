from turtle import *
import random 

billycorgan = Turtle()

billycorgan.color('orange', 'blue')
billycorgan.pensize()
billycorgan.speed(3)
billycorgan.shape('turtle')
billycorgan.turtlesize(2,2,2)

def drawTriangle():
	for x in range(6):
		billycorgan.forward(100)
		billycorgan.left(60)

for x in range(6):
	drawTriangle()
	billycorgan.left(60)

	

mainloop()
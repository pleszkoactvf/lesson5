from turtle import *
import random 

billycorgan = Turtle()

billycorgan.color('orange', 'blue')
billycorgan.pensize()
billycorgan.speed(3)
billycorgan.shape('turtle')
billycorgan.turtlesize(2,2,2)

def drawTriangle():
	for x in range(3):
		billycorgan.forward(80)
		billycorgan.left(120)

for x in range(12):
	drawTriangle()
	billycorgan.left(30)

	

mainloop()
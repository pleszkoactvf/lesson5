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

for x in range(12):
	drawTriangle()
	billycorgan.forward(80)
	billycorgan.left(40)
	billycorgan.forward(60)
	billycorgan.left(20)
	billycorgan.forward(40)
	billycorgan.left(10)

	

mainloop()
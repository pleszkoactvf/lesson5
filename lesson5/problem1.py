from turtle import *
color('orange', 'blue')
begin_fill()
while True:
	forward(300)
	left(120)
	if abs(pos()) < 1:
		break
end_fill()
done()

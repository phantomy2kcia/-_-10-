
import random
import time
import turtle
t = turtle.Pen()

w = turtle.Screen()
w.bgcolor("black") # 스크린의 배경색을 black으로 설정
w.title("circle turtle program") # title을 circle turtle program으로 설정



def mycircle(red, green, blue):
	t.color(red, green, blue) 
	t.begin_fill() # 색칠
	x = random.randint(0,200) # x 값을 0부터 50까지 랜덤하게 부여
	t.circle(x) 
	t.end_fill()
	t.up() 
	y = random.randint(0,200)
	t.seth(y) 
	
	if t.xcor() < -300 or t.xcor() > 300: # x의 좌표가 -300보다 작거나 300보다 클때 0,0으로 이동한다
		t.goto(0, 0) 
	elif t.ycor() < -300 or t.ycor() > 300: # y의 좌표가 -300보다 작거나 300보다 클때 0,0으로 이동한다
		t.goto(0, 0) 
	z = random.randint(0,100)
	t.forward(z) 
	t.down() 

for i in range(0, 10):
	a = random.randint(0,10)/10.0
	b = random.randint(0,10)/10.0
	c = random.randint(0,10)/10.0
	mycircle(a, b, c) 



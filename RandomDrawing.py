import turtle as t
import keyboard
import threading

#기초 세팅
s = t.Screen()
t.title("drawgraph")
x0 = []
y0 = []

#초기 위치
t.penup()
t.hideturtle()
t.goto(-250,0)
t.pendown()
t.showturtle()
t.pensize(1)

#이동(그리기)함수
def goto(x,y):
    t.goto(x,y)

#점 인쇄 함수
def dotprod():
    t.dot(12, 'purple')
    x0.append(t.xcor())
    y0.append(t.ycor())
    threading.Timer(0.2, dotprod).start()


#함수 실행 ###########################################################
t.ondrag(goto)
dotprod()
# s.onkeypress(dotprod, 'a')
# s.listen()

t.done()

#리스트 중복 제거를 위한 함수 선언
def getx():
    return x0
def gety():
    return y0

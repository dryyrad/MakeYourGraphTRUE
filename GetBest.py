import RandomDrawing
import DrawAgain as da
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import cv2

#이전 값 가져오기
x=da.getx()
y=da.gety()

poly1=np.polyfit(x,y,1)
poly2=np.polyfit(x,y,2)
poly3=np.polyfit(x,y,3)
poly4=np.polyfit(x,y,4)

#미분계수
def cal1(t):
    return poly1[0]
def cal2(t):
    return (2*poly2[0]*t + poly2[1])
def cal3(t):
    return (3*poly3[0]*t*t + 2*poly3[1]*t + poly3[2])
def cal4(t):
    return (4*poly4[0]*t*t*t + 3*poly4[1]*t*t + 2*poly4[2]*t + poly4[3])

#근사다항식 출력(도함수)
def real(k):
    if k==1:
        print( poly1[0], "x + ", poly1[1] )
    elif k==2:
        print( poly2[0], "x^2 + ", poly2[1], "x + ", poly2[2] )
    elif k==3:
        print( poly3[0], "x^3 + ", poly3[1], "x^2 + ", poly3[2], "x + ", poly3[3] )
    elif k==4:
        print( poly4[0], "x^4 + ", poly4[1], "x^3 + ", poly4[2], "x^2 + ", poly4[3], "x + ", poly4[4] )

#오차 구하기
best1=0
best2=0
best3=0
best4=0

for i in range(0, len(x)-1, 1):
    t = (x[i]+x[i+1])/2
    realav = (y[i+1]-y[i])/(x[i+1]-x[i])
    best1 += (cal1(t) - realav)**2
    best2 += (cal2(t) - realav)**2
    best3 += (cal3(t) - realav)**2
    best4 += (cal4(t) - realav)**2

#최소 오차 구하기
list = [best1, best2, best3, best4]

n=0
min0=list[0]
for i in range(1,4,1):
    if min0>list[i]:
        min0 = list[i]
        n=i

#전체 plotting
da.plotting(1)
da.plotting(2)
da.plotting(3)
da.plotting(4)

#근사다항식 출력
real(n+1)

#최적 근사 다항식 한 번 더 plotting
da.plotting(n+1)

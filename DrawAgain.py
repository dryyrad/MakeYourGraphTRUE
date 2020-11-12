import RandomDrawing as rd
import matplotlib.pyplot as plt
import numpy as np
import cv2
from scipy.optimize import curve_fit

#리스트 중복 제거
x=[]
y=[]
x0=rd.getx()
y0=rd.gety()

#plot 축 범위 지정
plt.axis([-300,300,-300,300])

for a,b in zip(x0,y0):
    if a not in x and b not in y:
        x.append(a)
        y.append(b)

def plotting(n):
    poly0 = np.polyfit(x,y,n)
    polyf = np.poly1d(poly0)
    plt.plot(x,y,'bo')
    plt.plot(x,polyf(x),'c-')
    plt.show()

def getx():
    return x

def gety():
    return y

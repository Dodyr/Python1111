import numpy as np
import matplotlib.pyplot as plt
print("Введите степень интерполяционного многочлена Лагранжа")
n=2
n+=1
print("количество узлов для функции f = 4")
m=4
print("Введите x1, x2, x3, x4 ")
x1=float(input())
x2=float(input())
x3=float(input())
x4=float(input())
print("Введите точку x*")
xx=float(input())
x = [x1, x2, x3, x4]
print("Введите y1, y2, y3, y4 ")
y1=float(input())
y2=float(input())
y3=float(input())
y4=float(input())

def nearest_x(x1, x2, x3, x4, y1, y2, y3, y4, xx):
    xy123 = [1, 2, 3, 4, 5, 6]
    x1234 = [x1, x2, x3, x4]
    y1234 = [y1, y2, y3, y4]
    i=0
    x=x1
    y=y1
    j = 0
    for i in range(0, 3):
        if (abs(xx - x) <= abs(xx - x1234[i+1])):
            xy123[j]=x
            xy123[j+1]=y
            j = j + 2
        else:
            xy123[j]=x1234[i+1]
            xy123[j+1]=y1234[i+1]
            j = j + 2
        x = x1234[i+1]
        y = y1234[i+1]
        print(xy123)
    return xy123  

def omega(x, y, t):
    omega = 1
    for j in range(len(y)):
        omega = omega * (t - x[j])
    return omega

def A(x, y, t, i):
    A = 1
    for j in range(len(y)):
        if not i==j:
            A = A * (t - x[j])
    A = 1/A
    return A

def property(x, y, t):
    pr = 1
    for j in range(len(y)):
        pr = pr + A(x, y, x[j], j) / (t - x[j])
    return pr

def lagranz(x, y, t):
    z = 0
    for j in range(len(y)):
        z = z + y[j] * A(x, y, x[j], j) / (t - x[j])
    z = z*omega(x, y, t)
    z = z/property(x, y, t)
    return z

xy = nearest_x(x1, x2, x3, x4, y1, y2, y3, y4, xx)
x = [1, 2, 3]
y = [1, 2, 3]
j = 0
for i in range(0, 5, 2):
    x[j] = xy[i]
    j = j + 1
j = 0
for i in range(1, 6, 2):
    y[j] = xy[i]
    j = j + 1
print(x)
print(y)
print("значение в х* = ")
print(lagranz(x,y,xx))
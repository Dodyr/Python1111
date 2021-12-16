
def nearest_x(x, y, xx):
    xy123 = [1, 2, 3, 4, 5, 6]
    i=0
    px=x[0]
    py=y[0]
    j = 0
    for i in range(0, 3):
        if (abs(xx - px) <= abs(xx - x[i+1])):
            xy123[j]=px
            xy123[j+1]=py
            j = j + 2
        else:
            xy123[j]=x[i+1]
            xy123[j+1]=y[i+1]
            j = j + 2
        px = x[i+1]
        py = y[i+1]
    print(xy123)
    return xy123  

def omega(x, y, t, n):
    omega = 1
    for j in range(n):
        omega = omega * (t - x[j])
    return omega

def A(x, y, t, i, n):
    A = 1
    for j in range(n):
        if not i==j:
            A = A * (t - x[j])
    A = 1/A
    return A

def property(x, y, t, n):
    pr = 0
    for j in range(n):
        pr = pr + A(x, y, x[j], j, n) / (t - x[j])
    pr = pr*omega(x, y, t, n)
    print(pr)
    return pr

def lagranz(x, y, t, n):
    z = 0
    for j in range(n):
        z = z + y[j] * A(x, y, x[j], j, n) / (t - x[j])
    z = z*omega(x, y, t, n)
    z = z/property(x, y, t, n)
    return z


print("Степень интерполяционного многочлена Лагранжа - 2")
print("количество узлов для функции f = 4")
print("Введите x1, x2, x3, x4 ")
x1=float(input())
x2=float(input())
x3=float(input())
x4=float(input())
ier = 0
x = [x1, x2, x3, x4]

for i in range(1, 4):
    for j in range(1, 4):
        if ((x[i-1]==x[i]) and not i==j):
            ier=1
            break
        
if (ier==0): 
    print("Введите точку x*")
    xx=float(input())
    print("Введите y1, y2, y3, y4 ")
    y1=float(input())
    y2=float(input())
    y3=float(input())
    y4=float(input())
    y = [y1, y2, y3, y4]

    xy = nearest_x(x, y, xx)
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
    print("значение в х* = ")
    yy = lagranz(x,y,xx, 2)
    print(yy)
    yy3 = lagranz(x,y,xx, 3)
    eps_yy = abs(yy3-yy)
    print ("Погрешность равна ", eps_yy)
else:
    print(" Код ошибки ier = 1, среди значений аргумента есть равные")
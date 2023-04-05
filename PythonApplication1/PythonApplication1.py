# -*- coding: windows-1251 -*-

import math
from turtle import color
import matplotlib
import matplotlib.pyplot as plt

#������� ��������
def Lagrang(x, y, point):
    n = len(x)
    s = 0
    for i in range(n):
        p = 1
        for j in range(n):
            if i != j:
                p *= (point - x[j])/(x[i] - x[j])
        s += y[i]*p
    return s

#���� ������� �� ��������� ������
def InputValues():
    x = []
    y = []
    tmp = [] #���.����������
    k = 0 #�������

    #��������� ����
    with open("input.txt", "r") as f:
        for line in f:
           if k == 0: #��� x
               tmp = line.split(" ") #��������� �����������
               x = [float(j) for j in tmp] #��������� �� str � float � ���������� � x
               k += 1
           else: #��� y
               tmp = line.split(" ") #��������� �����������
               y = [float(j) for j in tmp] #��������� �� str � float � ���������� � y
               break
    return x, y

#���� ��������� �� ��������� ������
def InputArgValues():
    x = []
    tmp = [] #���.����������

    #��������� ����
    with open("input2.txt", "r") as f:
        for line in f:
               tmp = line.split(" ") #��������� �����������
               x = [float(j) for j in tmp] #��������� �� str � float � ���������� � x
    return x

#����� ������ � �������
def OutputValues(x, y):

    print("������� ��������")
    print("|     x\t\t:\t  y\t   |")

    for i in range(len(x)):
        print("|  %f\t:  %f   |" %(x[i], y[i]))  

#���������� �������� ���������
def InterArray(n, x):
    Min = min(x)
    Max = max(x)
    step = float(0) #��� ��������
    GraphX = []
    
    step = (Max - Min) / (n - 1)
 
    # ��������� �������� ���������
    GraphX.insert(0, Min)
    for i in range(1, n):
        GraphX.insert(i, GraphX[i - 1] + step)

    for i in range(0, len(x)):
        for j in range(0, n - 1):
            if ((x[i] >= GraphX[j]) and (x[i] < GraphX[j+1])):
                GraphX[j] = x[i]
                        
    return GraphX

#������� ��� ��������
def FuncPolinom(n, x, GraphX):
    y = []
    GraphY = []
    MaxPow = int(input('������������ ������� ��������: '))

    coefficient = [] #������������ ��� x

    for i in range(MaxPow, 0, -1):
        print("����������� ��� X^%d" %(i))
        coefficient.insert(i, float(input()))

    coefficient.insert(i,float(input('C = ')))

    #������� ��� �������� ��������
    for i in range(len(x)):
        y.insert(i, float(0))
        for j in range(MaxPow + 1):
            y[i] += pow(x[i], j) * coefficient[j]

    #������� ��� ����������� ��������
    for i in range(n):
        GraphY.insert(i, float(0))
        for j in range(MaxPow + 1):
            GraphY[i] += pow(GraphX[i], j) * coefficient[j]
    return y, GraphY

#������� ��� log10
def FuncLog(x):
    y = []
    for i in range(len(x)):
        y.insert(i, math.log10(x[i]))

    return y

#������� ��� ������
def FuncModule(x):
    y = []
    for i in range(len(x)):
        y.insert(i, math.fabs(x[i]))
    return y

#������� ��� ����������
def FuncExp(x):
    y = []
    for i in range(len(x)):
        y.insert(i, math.exp(-x[i]))
    return y

#������� ��� sin
def FuncSin(x):
    y = []
    for i in range(len(x)):
        y.insert(i, math.sin(x[i]))
    return y
  
#���������� ����������� ����������
def MaxDeviation(LagrY, GraphY):
    Max = -1
    for i in range(len(LagrY)):
        if math.fabs(LagrY[i] - GraphY[i]) > Max:
            Max = math.fabs(LagrY[i] - GraphY[i])
    return Max




x = [] #������� X
y = [] #���� Y


print("1) ���������� ������������ �������� � �������� �����")
print("2) �� �������� ������� ��������� ������")
switch = input('�������� ������� ������ ���������: ')

#����������� ������������� ��������
if switch == '1':
    print("�� ������� ����������� ������������� ��������!\n")
 
    x, y = InputValues() #���� �� ����� �������
    OutputValues(x, y) #����� �� �����
    
    point = float(input('\n������� ����� ��� ���������� ������������� ��������: '))

    ResultPoint = Lagrang(x, y, point) #���������� ������������� �������� � �����

    print("\n������������ �������� � ����� %f = %f" %(point, ResultPoint))
else: #���������� ������� �� �������� �������
    print("�� ������� ��������� ������ �� �������� �������!\n")

    LagrY = [] #���� ��� �������� ��������
    GraphX = [] #���������� X ��� ���������� �������
    GraphY = [] #���������� Y ��� ���������� �������
    CountPoint = 30 #���������� ����� ��� ���������� �������
    x = InputArgValues() #���� �� �����

    print("1. ���������")
    print("2. y = log10(x) ��� x > 0")
    print("3. y = |x| ��� |x| <=1")
    print("4. y = e^(-x) ��� |x| <= 4")
    print("5. y = sin(x) ��� |x| <= pi")
    switch2 = input('�������� �������: ')
    
    GraphX = InterArray(CountPoint, x) #���������� �������� ���������

    if switch2 == '1':
        y, GraphY = FuncPolinom(CountPoint, x, GraphX) #�������
    elif switch2 == '2':
        y = FuncLog(x) #log10
        GraphY = FuncLog(GraphX)
    elif switch2 == '3': 
        y = FuncModule(x) #������
        GraphY = FuncModule(GraphX) 
    elif switch2 == '4': 
        y = FuncExp(x) #����������
        GraphY = FuncExp(GraphX)
    elif switch2 == '5': 
        y = FuncSin(x) #Sin
        GraphY = FuncSin(GraphX)

    for i in range(30):
	    LagrY.insert(i, Lagrang(x, y, GraphX[i])) 

    #����� ���������� ��������
    print("���� �������:")
    OutputValues(x, y)

    print("���� ���������:")
    OutputValues(GraphX, GraphY)

    print("�������:")
    OutputValues(GraphX, LagrY)


    MaxD = MaxDeviation(LagrY, GraphY)
    print("�������� ������������� ���������� �������� ������� �� ���������������")
    print(MaxD)

    #��������� �������

    plt.title(r'$������$', fontsize=20, fontname='Times New Roman')
    plt.plot(x, y, marker="o", color='k', label=r'$����-������������$', linewidth = 0.0 )
    plt.plot(GraphX, GraphY, ':b', linewidth = 3.0, label=r'$�������$')
    plt.plot(GraphX, LagrY, '--r', linewidth = 1.0, label=r'$�������$')
    plt.xlabel(r'$x$', fontsize=14)
    plt.ylabel(r'$f(x)$', fontsize=14)
    plt.grid(True)
    plt.legend(loc='best', fontsize=12)

    plt.show()

    





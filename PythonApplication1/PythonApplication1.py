# -*- coding: windows-1251 -*-

import math
from turtle import color
import matplotlib
import matplotlib.pyplot as plt

#Полином лагранжа
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

#Ввод таблицы из исходного файала
def InputValues():
    x = []
    y = []
    tmp = [] #Доп.переменная
    k = 0 #Счетчик

    #Открываем файл
    with open("input.txt", "r") as f:
        for line in f:
           if k == 0: #Для x
               tmp = line.split(" ") #Разделяем поэлементно
               x = [float(j) for j in tmp] #Переводим из str в float и записываем в x
               k += 1
           else: #Для y
               tmp = line.split(" ") #Разделяем поэлементно
               y = [float(j) for j in tmp] #Переводим из str в float и записываем в y
               break
    return x, y

#Ввод аргумента из исходного файала
def InputArgValues():
    x = []
    tmp = [] #Доп.переменная

    #Открываем файл
    with open("input2.txt", "r") as f:
        for line in f:
               tmp = line.split(" ") #Разделяем поэлементно
               x = [float(j) for j in tmp] #Переводим из str в float и записываем в x
    return x

#Вывод данных в консоль
def OutputValues(x, y):

    print("Таблица значений")
    print("|     x\t\t:\t  y\t   |")

    for i in range(len(x)):
        print("|  %f\t:  %f   |" %(x[i], y[i]))  

#Расширение значений аргумента
def InterArray(n, x):
    Min = min(x)
    Max = max(x)
    step = float(0) #Шаг значений
    GraphX = []
    
    step = (Max - Min) / (n - 1)
 
    # Расширяем значение аргумента
    GraphX.insert(0, Min)
    for i in range(1, n):
        GraphX.insert(i, GraphX[i - 1] + step)

    for i in range(0, len(x)):
        for j in range(0, n - 1):
            if ((x[i] >= GraphX[j]) and (x[i] < GraphX[j+1])):
                GraphX[j] = x[i]
                        
    return GraphX

#Функция для полинома
def FuncPolinom(n, x, GraphX):
    y = []
    GraphY = []
    MaxPow = int(input('Максимальная степень полинома: '))

    coefficient = [] #Коэффициенты при x

    for i in range(MaxPow, 0, -1):
        print("Коэффициент при X^%d" %(i))
        coefficient.insert(i, float(input()))

    coefficient.insert(i,float(input('C = ')))

    #Подсчет для заданных значений
    for i in range(len(x)):
        y.insert(i, float(0))
        for j in range(MaxPow + 1):
            y[i] += pow(x[i], j) * coefficient[j]

    #Подсчет для расширенных значений
    for i in range(n):
        GraphY.insert(i, float(0))
        for j in range(MaxPow + 1):
            GraphY[i] += pow(GraphX[i], j) * coefficient[j]
    return y, GraphY

#Функция для log10
def FuncLog(x):
    y = []
    for i in range(len(x)):
        y.insert(i, math.log10(x[i]))

    return y

#Функция для модуля
def FuncModule(x):
    y = []
    for i in range(len(x)):
        y.insert(i, math.fabs(x[i]))
    return y

#Функция для экспоненты
def FuncExp(x):
    y = []
    for i in range(len(x)):
        y.insert(i, math.exp(-x[i]))
    return y

#Функция для sin
def FuncSin(x):
    y = []
    for i in range(len(x)):
        y.insert(i, math.sin(x[i]))
    return y
  
#Нахождение наибольшего отклонения
def MaxDeviation(LagrY, GraphY):
    Max = -1
    for i in range(len(LagrY)):
        if math.fabs(LagrY[i] - GraphY[i]) > Max:
            Max = math.fabs(LagrY[i] - GraphY[i])
    return Max




x = [] #Столбец X
y = [] #Лист Y


print("1) Определить приближенное значение в заданной точке")
print("2) По заданной функции построить график")
switch = input('Выберите вариант работы программы: ')

#Определение приближенного значения
if switch == '1':
    print("Вы выбрали определение приближенного значения!\n")
 
    x, y = InputValues() #Ввод из файла таблицы
    OutputValues(x, y) #Вывод на экран
    
    point = float(input('\nВведите точку для нахождения приближенного значения: '))

    ResultPoint = Lagrang(x, y, point) #Нахождение приближенного значения в точке

    print("\nПриближенное значение в точке %f = %f" %(point, ResultPoint))
else: #Построение графика по заданной функции
    print("Вы выбрали построить график по заданной функции!\n")

    LagrY = [] #Лист для значений лагранжа
    GraphX = [] #Координаты X для построения графика
    GraphY = [] #Координаты Y для построения графика
    CountPoint = 30 #Количество точек для построения графика
    x = InputArgValues() #Ввод из файла

    print("1. Многочлен")
    print("2. y = log10(x) при x > 0")
    print("3. y = |x| при |x| <=1")
    print("4. y = e^(-x) при |x| <= 4")
    print("5. y = sin(x) при |x| <= pi")
    switch2 = input('Выберите функцию: ')
    
    GraphX = InterArray(CountPoint, x) #Расширение значений аргумента

    if switch2 == '1':
        y, GraphY = FuncPolinom(CountPoint, x, GraphX) #Полином
    elif switch2 == '2':
        y = FuncLog(x) #log10
        GraphY = FuncLog(GraphX)
    elif switch2 == '3': 
        y = FuncModule(x) #Модуль
        GraphY = FuncModule(GraphX) 
    elif switch2 == '4': 
        y = FuncExp(x) #Экспонента
        GraphY = FuncExp(GraphX)
    elif switch2 == '5': 
        y = FuncSin(x) #Sin
        GraphY = FuncSin(GraphX)

    for i in range(30):
	    LagrY.insert(i, Lagrang(x, y, GraphX[i])) 

    #Вывод полученных значений
    print("Было введено:")
    OutputValues(x, y)

    print("Было достичано:")
    OutputValues(GraphX, GraphY)

    print("Лагранж:")
    OutputValues(GraphX, LagrY)


    MaxD = MaxDeviation(LagrY, GraphY)
    print("Величина максимального отклонения заданной функции от интерполирующей")
    print(MaxD)

    #Рисование графика

    plt.title(r'$График$', fontsize=20, fontname='Times New Roman')
    plt.plot(x, y, marker="o", color='k', label=r'$Узлы-интерполяции$', linewidth = 0.0 )
    plt.plot(GraphX, GraphY, ':b', linewidth = 3.0, label=r'$Функция$')
    plt.plot(GraphX, LagrY, '--r', linewidth = 1.0, label=r'$Лагранж$')
    plt.xlabel(r'$x$', fontsize=14)
    plt.ylabel(r'$f(x)$', fontsize=14)
    plt.grid(True)
    plt.legend(loc='best', fontsize=12)

    plt.show()

    





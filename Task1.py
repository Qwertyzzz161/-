def target1():
    while True:
        try:
            a = int(input("Введите значение стороны квадрата : "))
            P = a*4
            print("Периметр квадрата =", P)
            return a
        except ValueError:
            print("Нужно ввести целое число. Повторите ввод")



def target2():
    while True:
        try:
            a = int(input("Введите значение стороны квадрата : "))
            S = a**2
            print("Площадь квадрата =", S)
            return a
        except ValueError:
            print("Нужно ввести целое число. Повторите ввод")



def target3():
    while True:
        try:
            a = int(input("Введите значение первой стороны прямоугольника : "))
            b = int(input("Введите значение второй стороны прямоугольника : "))
            S = a*b
            P = (a+b)*2
            print("Периметр прямоугольника =", P)
            print("Площадь прямоугольника =", S)
            return a,b
        except ValueError:
            print("Нужно ввести целое число. Повторите ввод")



def target4():
    while True:
        try:
            d = int(input("Введите значение диаметра окружности : "))
            pi = 3.14
            L = pi*d
            print("Длина окружности =", L)
            return d
        except ValueError:
            print("Нужно ввести целое число. Повторите ввод")

def target5():
    while True:
        try:
            a = int(input("Введите значение длины ребра куба : "))
            S = 6*a**2
            V=a**3
            print("Площадь поверхности куба =", S)
            print("Объем куба=", V)
            return a
        except ValueError:
            print("Нужно ввести целое число. Повторите ввод")

def target6():
    while True:
        try:
            a = int(input("Введите значение длины первого ребра параллелепипеда : "))
            b = int(input("Введите значение длины второго ребра параллелепипеда : "))
            c = int(input("Введите значение длины третьего ребра параллелепипеда : "))
            S = 2*(a*b + b*c + a*c)
            V=a*b*c
            print("Площадь поверхности параллелепипеда =", S)
            print("Объем параллелепипеда=", V)
            return a,b,c
        except ValueError:
            print("Нужно ввести целое число. Повторите ввод")


def target7():
    while True:
        try:
            R = int(input("Введите значение радиуса круга : "))
            pi = 3.14
            S = pi*R**2
            L = 2*pi*R
            print("Длина окружности =", L)
            print("Площадь круга =", S)
            return R
        except ValueError:
            print("Нужно ввести целое число. Повторите ввод")


def target8():
    while True:
        try:
            a = int(input("Введите первое число : "))
            b = int(input("Введите второе число : "))
            avg = (a+b)/2
            print("Среднее арифметическое 2 чисел =", avg)
            return a,b
        except ValueError:
            print("Нужно ввести целое число. Повторите ввод")

import math
def target9():
    while True:
        try:
            a = int(input("Введите первое число : "))
            b = int(input("Введите второе число : "))
            avg = math.sqrt(a*b)
            print("Среднее геометрическое 2 чисел =", avg)
            return a,b
        except ValueError:
            print("Нужно ввести целое число. Повторите ввод")


def target10():
    while True:
        try:
            a = int(input("Введите первое число : "))
            b = int(input("Введите второе число : "))
            if a == 0 or b == 0:
                print("Числа не должны быть равны нулю")
                return a,b
            op1 = a+b
            op2 = a-b
            op3 = a*b
            op4 = a/b
            print("Сумма =", op1)
            print("Разница =", op2)
            print("Произведение =", op3)
            print("Частное =", op4)
            return a,b
        except ValueError:
            print("Нужно ввести целое число. Повторите ввод")

#target1()
#target2()
#target3()
#target4()
#target5()
#target6()
#target7()
#target8()
#target9()
#target10()
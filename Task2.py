def target1():
    while True:
        try:
            L = int(input("Введите значение в сантиметрах : "))
            lenght=L//100
            print("Длина =", lenght,"м")
            return L
        except ValueError:
            print("Нужно ввести целое число. Повторите ввод")

def target2():
    while True:
        try:
            M = int(input("Введите значение в килограммах : "))
            weight=M//1000
            print("Масса =", weight,"т")
            return M
        except ValueError:
            print("Нужно ввести целое число. Повторите ввод")


def target3():
    while True:
        try:
            M = int(input("Введите значение в байтах : "))
            weight=M//1024
            print("Вес файла =", weight,"КБ")
            return M
        except ValueError:
            print("Нужно ввести целое число. Повторите ввод")


def target4():
    while True:
        try:
            A = int(input("Введите первое число : "))
            B = int(input("Введите второе число : "))
            if A < B or A==B:
                print("Первое число должно быть больше второго")
                return A,B
            cut= A//B
            print("На отрезке A помещаются ",cut,"отрезка(ов) B")
            return A,B
        except ValueError:
            print("Нужно ввести целое число. Повторите ввод")

def target5():
    while True:
        try:
            A = int(input("Введите первое число : "))
            B = int(input("Введите второе число : "))
            if A < B or A==B:
                print("Первое число должно быть больше второго")
                return A,B
            cut= A%B
            print("Длина незанятой части отрезка A = ",cut)
            return A,B
        except ValueError:
            print("Нужно ввести целое число. Повторите ввод")

def target6():
    while True:
        try:
            A = int(input("Введите двузначное число : "))
            if A < 10 or A > 99:
                print("Число должно быть двузначным")
                return A
            op1= A//10
            op2= A%10
            print("Первая цифра это ",op1)
            print("Вторая цифра это ", op2)
            return A
        except ValueError:
            print("Нужно ввести целое число. Повторите ввод")

def target7():
    while True:
        try:
            A = int(input("Введите двузначное число : "))
            if A < 10 or A > 99:
                print("Число должно быть двузначным")
                return A
            op1= A//10
            op2= A%10
            print("Сумма цифр числа = ",op1+op2)
            print("Произведение цифр числа = ", op1*op2)
            return A
        except ValueError:
            print("Нужно ввести целое число. Повторите ввод")


def target8():
    while True:
        try:
            A = int(input("Введите двузначное число : "))
            if A < 10 or A > 99:
                print("Число должно быть двузначным")
                return A
            op1= A//10
            op2= A%10
            print("Число, обратное введенному, это ", op2,op1)
            return A
        except ValueError:
            print("Нужно ввести целое число. Повторите ввод")

def target9():
    while True:
        try:
            A = int(input("Введите трехзначное число : "))
            if A < 100 or A > 999:
                print("Число должно быть трехначным")
                return A
            op1= A//100
            print("Первая цифра это ",op1)
            return A
        except ValueError:
            print("Нужно ввести целое число. Повторите ввод")

def target10():
    while True:
        try:
            A = int(input("Введите трехзначное число : "))
            if A < 100 or A > 999:
                print("Число должно быть трехначным")
                return A
            op1 = (A%100)//10
            op2 = A%10

            print("Третья цифра это ",op2)
            print("Вторая цифра это ", op1)
            return A
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
def target1():
    while True:
        try:
            A = int(input("Введите значение A : "))
            positive = A > 0
            print("Число положительное?",positive)
            return A
        except ValueError:
            print("Нужно ввести целое число. Повторите ввод")

def target2():
    while True:
        try:
            A = int(input("Введите значение A : "))
            positive = A % 2 == 1
            print("Число нечетное?",positive)
            return A
        except ValueError:
            print("Нужно ввести целое число. Повторите ввод")


def target3():
    while True:
        try:
            A = int(input("Введите значение A : "))
            positive = A % 2 == 0
            print("Число четное?",positive)
            return A
        except ValueError:
            print("Нужно ввести целое число. Повторите ввод")


def target4():
    while True:
        try:
            A = int(input("Введите значение A : "))
            B = int(input("Введите значение B : "))
            if A>2 and B<=3:
                print("Справедливы неравенства A > 2 и B ≤ 3?",True)
            else:
                print("Справедливы неравенства A > 2 и B ≤ 3?", False)
            return A,B
        except ValueError:
            print("Нужно ввести целое число. Повторите ввод")


def target5():
    while True:
        try:
            A = int(input("Введите значение A : "))
            B = int(input("Введите значение B : "))
            if A>=0 or B<-2:
                print("Справедливы неравенства A ≥ 0 или B < −2?",True)
            else:
                print("Справедливы неравенства A ≥ 0 или B < −2?", False)
            return A,B
        except ValueError:
            print("Нужно ввести целое число. Повторите ввод")


def target6():
    while True:
        try:
            A = int(input("Введите значение A : "))
            B = int(input("Введите значение B : "))
            C = int(input("Введите значение C : "))
            if A < B < C:
                print("Справедливо двойное неравенство A < B < C?",True)
            else:
                print("Справедливо двойное неравенство A < B < C?", False)
            return A,B,C
        except ValueError:
            print("Нужно ввести целое число. Повторите ввод")

#target7 и target6 ничем не отличаются, кроме формулировки условия
def target7():
    while True:
        try:
            A = int(input("Введите значение A : "))
            B = int(input("Введите значение B : "))
            C = int(input("Введите значение C : "))
            if A < B < C:
                print("Число B находится между числами A и C?",True)
            else:
                print("Число B находится между числами A и C?", False)
            return A,B,C
        except ValueError:
            print("Нужно ввести целое число. Повторите ввод")

def target8():
    while True:
        try:
            A = int(input("Введите значение A : "))
            B = int(input("Введите значение B : "))
            if A % 2 == 1 and B % 2 == 1:
                print("Каждое из чисел A и B нечетное?",True)
            else:
                print("Каждое из чисел A и B нечетное?", False)
            return A,B
        except ValueError:
            print("Нужно ввести целое число. Повторите ввод")


def target9():
    while True:
        try:
            A = int(input("Введите значение A : "))
            B = int(input("Введите значение B : "))
            if A % 2 == 1 or B % 2 == 1:
                print("Хотя бы одно из чисел A и B нечетное?",True)
            else:
                print("Хотя бы одно из чисел A и B нечетное?", False)
            return A,B
        except ValueError:
            print("Нужно ввести целое число. Повторите ввод")


def target10():
    while True:
        try:
            A = int(input("Введите значение A : "))
            B = int(input("Введите значение B : "))
            if (A % 2 == 1 and B % 2 == 0) or (A % 2 == 0 and B % 2 == 1):
                print("Ровно одно из чисел A и B нечетное?",True)
            else:
                print("Ровно одно из чисел A и B нечетное?", False)
            return A,B
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
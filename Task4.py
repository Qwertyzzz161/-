def target1():
    list1 = [1, 2, 3, 4, 5]

    first = my_list[0]
    print("Первый элемент:", first)

    third = my_list[2]
    print("Третий элемент:", third)

    firstandthird = my_list[:3]
    print("Первые три элемента:", firstandthird)



def target2():
    list2 = ["Ростов", "+", "на", "-", "Дону"]
    list2[1]="-"
    #name= list2[0] + list2[1] + list2[2] + list2[3] + list2[4]
    print("Название города: ",name)



def target3():
    list3 = ['a', 's', '1', 'a', '32', '23']
    numbers = []
    letters = []

    for item in list3:
        if item.isdigit():
            numbers.append(item)
        else:
            letters.append(item)

    print("Цифры:", numbers)
    print("Буквы:", letters)


def target4():
    list4 = ['a', 's', '1', 'a', '32', '23']
    numbers = []
    letters = []

    for item in list4:
        if item.isdigit():
            numbers.append(item)
        else:
            letters.append(item)

    newletters=letters.pop(2)

    print("Удаленный элемент:", newletters)
    print("Новый список:", letters)

def target5():
    list5 = ['a', 's', '1', 'a', '32', '23']
    newlist5 = set(list5)
    print("Множество: ",newlist5)

#target1()
#target2()
#target3()
#target4()
#target5()
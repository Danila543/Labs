
def zad1():
    k = input("выберите число")
    k = int(k)
    a = [1, 32, 134, 468, 781, 2]
    if k in a:
        print("поздравляю вы угадали!")
    else:
        print("нет такого числа")


def zad2():

        list = ["1", "2", "3", "3", "5", "5", "6"]
        for i in range(len(list) - 1):
            if list[i] == list[i + 1]:
                print('Есть совпадение', list[i])


def zad3():
    days = ("monday", 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    a = input('введите день: ')
    print('ваши выходные: ', days[7-int(a):])
    print("оставшие дни: ", days[:7-int(a)])


def zad4():
    k = 0
    lists = ["Батюченко", "Тюрин", "Шапран", "Байдукова", "Иванов", "Бурашников", "Фаттахов", "Чернейкина"]
    list1 = ["Батюченко", "Соболев", "Иванов", "Смирнов", "Харламов", "Зверев", "Галустян", "Кравец"]
    list2 = (lists[4], lists[2], lists[6], lists[2])
    print(lists)
    print(list1)
    print(list2)
    print(len(list2))
    list2 = tuple(sorted(list2))
    print(list2)
    for i in range(len(list2)):
        if list2[i] == "Иванов":
            k += 1

    else:
        print('не встречается')

    print('встречается', k, 'раз')

zad4()

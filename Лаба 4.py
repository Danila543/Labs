def zad1():
    try:
        pass
        a = int(input("Введите число: "))
        b = 3
    except ValueError:
        print ("Введено не число")
    else:
        if a % b == 0:
            print ("Число делится на 3 :)")
        elif a == 0:
            print("На ноль делить нельзя")
        else:
            print("Число не делится на 3 :_(")

def zad2():
    try:
        a = int(input("Введите число:"))
        b = 100
        i = a / b
    except ValueError:
        print ("Введено не число")
    except ZeroDivisionError:
        print ("Введено число 0")
    else:
        print("Деление на число 100: ", i)

def zad3():
    a = int(input("Введите число: "))
    b = int(input("Введите месяц (цифра): "))
    c = int(input("Введите год: "))
    q = c % 100
    if a * b == q:
        print("Это магическая дата!:)")
    else:
        print("No es una cita mágica :_(")

def zad4():
    a = int(input("Введи свой билет(Учти что количество цифр должно быть четным):"))
    b = a % 1000
    c = a // 1000
    f" sum(b.split{1,2,3}"
    print (sum(b.split[1,2,3])




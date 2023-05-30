from random import randint


def zad1():
    pass


word = []
while(word1 := str(input())) !="stop":
    word.append(word1)

print(" ".join(word))


def zad2():
    pass


word = []
while(word := str(input())) !="stop":
    if "ф" in word or "Ф" in word:
        print("Ого, это удивительное слово")
    else:
        print("Ну это не удивительное слово :(")


def zad3():
    count = 0
    while True:
        a = randint(1, 100)
        b = randint(1, 100)
        print(f"{a} + {b} = ", end="")
        num = input()
        while not num.isdigit() and num != "stop":
            print("Вы ввели что-то не то")
            break
        if num == "stop":
            break
        num = int(num)
        if a + b == num:
            print("УРА вы угадали!")
        else:
            count = count + 1
            print("Вы не угадали :(")
        if count == 3:
            print("вы проиграли")
            break
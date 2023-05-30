import os

from PIL import Image, ImageFilter


def zad1():
    os.chdir("C:/Users/USER/PycharmProjects/pythonProject2")
    with Image.open("1.jpg") as img:
        img.load()
        a = "replased"
        img1 = img.filter(ImageFilter.SHARPEN)
        img1.save(f"C:/Users/USER/PycharmProjects/Лаба 9/img1{a}.jpg")
    with Image.open("2.jpg") as img:
        img.load()
        img2 = img.filter(ImageFilter.SHARPEN)
        img2.save(f"C:/Users/USER/PycharmProjects/Лаба 9/img2{a}.jpg")
    with Image.open("3.jpg") as img:
        img.load()
        img3 = img.filter(ImageFilter.SHARPEN)
        img3.save(f"C:/Users/USER/PycharmProjects/Лаба 9/img3{a}.jpg")
    with Image.open("4.jpg") as img:
        img.load()
        img4 = img.filter(ImageFilter.SHARPEN)
        img4.save(f"C:/Users/USER/PycharmProjects/Лаба 9/img4{a}.jpg")
    with Image.open("5.jpg") as img:
        img.load()
        img5 = img.filter(ImageFilter.SHARPEN)
        img5.save(f"C:/Users/USER/PycharmProjects/Лаба 9/img5{a}.jpg")


def zad2():
    a = 0
    os.chdir("C:/Users/USER/PycharmProjects/pythonProject2")
    with Image.open("1.jpg") as img:
        split_tup = os.path.splitext('1.jpg')
        imgform = split_tup[1]
        if imgform := (".jpg"):
            a += 1
            img.load()
            img1 = img.filter(ImageFilter.SHARPEN)
            img1.save(f"C:/Users/USER/PycharmProjects/Лаба 9/img1_{a}.jpg")
    with Image.open("2.jpg") as img:
        split_tup = os.path.splitext('2.jpg')
        imgform = split_tup[1]
        if imgform := (".jpg"):
            a += 1
            img.load()
            img2 = img.filter(ImageFilter.SHARPEN)
            img2.save(f"C:/Users/USER/PycharmProjects/Лаба 9/img2_{a}.jpg")
    with Image.open("3.jpg") as img:
        split_tup = os.path.splitext('3.jpg')
        imgform = split_tup[1]
        if imgform := (".jpg"):
            a += 1
            img.load()
            img3 = img.filter(ImageFilter.SHARPEN)
            img3.save(f"C:/Users/USER/PycharmProjects/Лаба 9/img3_{a}.jpg")
    with Image.open("4.jpg") as img:
        split_tup = os.path.splitext('4.jpg')
        imgform = split_tup[1]
        if imgform := (".jpg"):
            a += 1
        img.load()
        img4 = img.filter(ImageFilter.SHARPEN)
        img4.save(f"C:/Users/USER/PycharmProjects/Лаба 9/img4_{a}.jpg")
    with Image.open("5.jpg") as img:
        split_tup = os.path.splitext('5.jpg')
        imgform = split_tup[1]
        if imgform := (".jpg"):
            a += 1
        img.load()
        img5 = img.filter(ImageFilter.SHARPEN)
        img5.save(f"C:/Users/USER/PycharmProjects/Лаба 9/img5_{a}.jpg")


def zad3():
    os.chdir("C:/Users/USER/PycharmProjects/Лаба 9")
    with open("buy.csv", encoding="utf=8") as c:
        lines = c.readlines()
        s = 0
        print("Нужно купить: ")
        for line in lines[1:]:
            product, kolichestvo, cena = line.strip().split(',')
            s += int(kolichestvo) * int(cena)
            print(f"{product} - {kolichestvo} шт. за {cena} руб.")
        print(f"Итоговая сумма: {s} руб.")


zad1()
zad2()
zad3()

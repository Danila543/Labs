from PIL import Image, ImageDraw, ImageFont


def zad1():
    a = Image.open("im1.jpg")
    a = a.crop((300, 175, 900, 500))
    a.show()
    a.save("cropim1.jpg")


def zad2():
    a = {"День рождения": "im1.jpg", "День защитника отечества": "23.jpg", "Пасха": "pasha.jpg", "Новый год": "ng.jpg"}
    b = input("К какому празднику нужна открытка?: ")
    if b in a:
        img = Image.open(a[b])
        img.show()
    else:
        print("Такой открытки нет :(")


def zad3():
    b = input("Введите именинника: ")
    with Image.open("im1.jpg") as img:
        img.load()
        font = ImageFont.truetype('Montserrat-Bold.ttf', size=18)
        txt = ImageDraw.Draw(img)
        txt.text(
            (28, 23),
            b + ", поздравляю!",
            font=font,
            fill='blue')
        img.show()


zad1()



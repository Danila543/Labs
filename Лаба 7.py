from PIL import Image, ImageOps, ImageFilter


def zad1():
    with Image.open("1.jpg") as img:
        img.show()
        print("Длина, ширина:", img.size)
        print('Формат: ', img.format)
        print('Модель цвета: ', img.mode)


def zad2():
    with Image.open("1.jpg") as img:
        img.load()
        new_img = img.resize((img.height // 3, img.width // 3))
        new_img.save("1_1.jpg")

        new_img = ImageOps.mirror(img)

        new_img.save("1_2.jpg")

        new_img = ImageOps.flip(img)
        new_img.save("1_3.jpg")


def zad3():
    with Image.open("1.jpg") as img:
        img.load()
        img1 = img.filter(ImageFilter.SHARPEN)
        img1.save("filimg1.jpg")
    with Image.open("2.jpg") as img:
        img.load()
        img2 = img.filter(ImageFilter.SHARPEN)
        img2.save("filimg2.jpg")
    with Image.open("3.jpg") as img:
        img.load()
        img3 = img.filter(ImageFilter.SHARPEN)
        img3.save("filimg3.jpg")
    with Image.open("4.jpg") as img:
        img.load()
        img4 = img.filter(ImageFilter.SHARPEN)
        img4.save("filimg4.jpg")
    with Image.open("5.jpg") as img:
        img.load()
        img5 = img.filter(ImageFilter.SHARPEN)
        img5.save("filimg5.jpg")


def zad4():
    a = Image.open("5.jpg")
    b = Image.open("kot.png")
    b = b.resize((150, 150))
    a.paste(b, mask=b)
    a.show()


zad1()
zad2()
zad3()
zad4()

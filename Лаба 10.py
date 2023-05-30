import json


def zad1():
    with open("product.json", encoding="utf=8") as a:
        data = json.load(a)
    for product in data["products"]:
        print("Название:", product['name'])
        print("Цена:", product['price'])
        print("Вес:", product['weight'])
        if product["available"]:
            print("В наличии")
        else:
            print("Нет в наличии!")


def zad2():
    with open('product2.json', encoding='utf=8') as f:
        data = json.load(f)

    for product in data['products']:
        print("Название:", product['name'])
        print("Цена:", product['price'])
        print("Вес:", product['weight'])
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()

    new_product = {}
    new_product['name'] = input("Введите название нового продукта: ")
    new_product['price'] = float(input("Введите цену нового продукта: "))
    new_product['weight'] = float(input("Введите вес нового продукта: "))
    new_product['available'] = bool(input("Есть ли новый продукт в наличии? (True/False): "))

    data['products'].append(new_product)

    with open('products.json', 'w') as f:
        json.dump(data, f)

    print("\nОбновленное содержимое файла products.json:")
    with open('products.json', 'r') as f:
        print(f.read())


def zad3():
    d = {}
    with open("ru-en.txt", "r") as file:
        for line in file:
            eng = line.split("-")[0].strip()
            rus = line.split("-")[1].strip().split(',')
            for i in rus:
                i = i.strip()
                if i in d.keys():
                    d[i] = d[i] + ", " + eng
                else:
                    d[i] = eng
        with open("en-ru.txt", "w") as file:
            for i in sorted(d.keys()):
                file.writelines(f"{i} - {d[i]}\n")

zad1()
zad2()
zad3()


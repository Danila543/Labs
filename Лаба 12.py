
def zad1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"{self.cuisine_type} кухня в ресторане {self.restaurant_name}!")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт!")

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type):
            super().__init__(restaurant_name, cuisine_type)
            self.type = []

        def flavors(self):
            print("Доступные вкусы: ")
            for ice in self.type:
                print(ice.title())

    icecreamstand1 = IceCreamStand("Кафе-Морожное", "Ice Cream")
    icecreamstand1.type = ["Ванильное", "Шоколадное", "Фисташковое", "Клубничное"]
    icecreamstand1.flavors()


def zad2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Ресторан {self.restaurant_name} предлагает кухню {self.cuisine_type}.")

        def open_restaurant(self):
            print(f"Ресторан {self.restaurant_name} открыт!")

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, location, time ):
            super().__init__(restaurant_name, cuisine_type)
            self.type = ["Ванильное", "Шоколадное", "Фисташковое", "Клубничное"]
            self.weed = ["Классическое", "Жаренное", "Мягкое"]
            self.location = location
            self.time = time

        def flavors(self):
            print("Доступные вкусы: ")
            for ice in self.type:
                print(ice.title())

        def add(self):
            ice = input("Введите новый вкус: ")
            self.type.append(ice)

        def remove(self):
            ice = input("Введите вкус который нужно удалить: ")
            if ice in self.type:
                self.type.remove(ice)
            else:
                print("У нас такого вкуса :_(")

        def check(self):
            ice = input("Какой вкус мороженого вы хотите?: ")
            if ice in self.type:
                print("У нас есть " + ice + "!")
            wed = input("Какой вид мороженого вы хотите?: ")
            if wed in self.type:
                print("У нас есть " + wed + "!")
            print("Вот ваше  " + ice + ", " + wed + "  мороженое")

    icecreamstand2 = IceCreamStand("Кафе-Морожное", "Ice Cream", "ул. Большевиков 54 к.1", "с 12:00 до 22:00")
    print(f'Мы находимся на: {icecreamstand2.location}')
    print(f'Режим работы: {icecreamstand2.time}')
    icecreamstand2.add()
    icecreamstand2.remove()
    icecreamstand2.check()


def zad3():
    import tkinter as tk

    class IceCreamStand:
        def __init__(self, root):
            self.root = root
            self.root.title("Магазин мороженного")
            self.root.geometry('250x300')
            self.label1 = tk.Label(self.root, text="Выберете вид мороженного: ")
            self.label1.pack()

            self.var1 = tk.IntVar()
            self.checkbutton1 = tk.Checkbutton(self.root, text="классическое", variable=self.var1)
            self.checkbutton1.pack()

            self.var2 = tk.IntVar()
            self.checkbutton2 = tk.Checkbutton(self.root, text="мягкое", variable=self.var2)
            self.checkbutton2.pack()

            self.var3 = tk.IntVar()
            self.checkbutton3 = tk.Checkbutton(self.root, text="жаренное", variable=self.var3)
            self.checkbutton3.pack()

            self.label2 = tk.Label(self.root, text="Выберите вкус:")
            self.label2.pack()

            self.var5 = tk.StringVar()
            self.radio1 = tk.Radiobutton(self.root, text="ванильное", variable=self.var5,
                                         value="ванильное")
            self.radio1.pack()
            self.radio2 = tk.Radiobutton(self.root, text="шоколадное", variable=self.var5,
                                         value="шоколадное")
            self.radio2.pack()
            self.radio3 = tk.Radiobutton(self.root, text="фисташковое", variable=self.var5,
                                         value="фисташковое")
            self.radio3.pack()
            self.button = tk.Button(self.root, text='Выбрать', command=self.submit)
            self.button.pack()

            self.output_label = tk.Label(self.root, text='')
            self.output_label.pack()

        def submit(self):

            type = []
            if self.var1.get() == 1:
                type.append("Классическое")
            if self.var2.get() == 1:
                type.append("Мягкое")
            if self.var3.get() == 1:
                type.append("Жаренное")

            flavor = self.var5.get()

            if flavor and type:
                self.output_label.configure(text=f'Вы выбрали {", ".join(type)} \n {flavor} мороженое!')
            else:
                self.output_label.configure(text='Пожалуйста выберете вид мороженного и вкус')

    root = tk.Tk()
    app = IceCreamStand(root)
    root.mainloop()



zad3()




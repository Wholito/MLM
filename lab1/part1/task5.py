"""
5. Реализуйте программу «Кондитерская», которая будет включать
в себя шесть пунктов меню. У вас есть словарь, где ключ – название
продукции (торт, пирожное, маффин и т.д.). Значение – список,
который содержит состав, цену (за 100гр) и кол-во (в граммах).
1. Просмотр описания: название – описание
2. Просмотр цены: название – цена.
3. Просмотр количества: название – количество.
4. Всю информацию.
5. Покупка
В пункте «Покупка» необходимо совершить покупку, с
клавиатуры вводите название продукции и его кол-во, n – выход из
программы. Посчитать цену выбранных товаров и сколько товаров
осталось в изначальном списке
6. До свидания – 2 балла
"""
shop = {
    "торт": [["мука", "яйца", "сахар", "сливки"], 45.0, 500],
    "пирожное": [["бисквит", "крем", "шоколад"], 38.0, 300],
    "маффин": [["мука", "масло", "изюм"], 32.0, 200],
    "эклер": [["заварное тесто", "крем"], 40.0, 150],
    "пончик": [["тесто", "глазурь"], 28.0, 250],
}


def show_description(name):
    if name in shop:
        print(name, "-", ", ".join(shop[name][0]))


def show_price(name):
    if name in shop:
        print(name, "-", shop[name][1])


def show_quantity(name):
    if name in shop:
        print(name, "-", shop[name][2])


def show_all():
    for name, info in shop.items():
        print(name, info[0], info[1], info[2])


def purchase():
    total = 0.0
    while True:
        line = input().strip()
        if line.lower() == "n":
            break
        parts = line.split()
        if len(parts) != 2:
            continue
        name, qty_s = parts[0], parts[1]
        try:
            qty = int(qty_s)
        except ValueError:
            continue
        if name not in shop or qty <= 0:
            continue
        available = shop[name][2]
        if qty > available:
            qty = available
        price_per_100 = shop[name][1]
        total += price_per_100 * qty / 100
        shop[name][2] -= qty
    print(total)
    for name, info in shop.items():
        print(name, info[2])


while True:
    choice = input().strip()
    if choice == "1":
        show_description(input().strip())
    elif choice == "2":
        show_price(input().strip())
    elif choice == "3":
        show_quantity(input().strip())
    elif choice == "4":
        show_all()
    elif choice == "5":
        purchase()
    elif choice == "6":
        print("До свидания")
        break

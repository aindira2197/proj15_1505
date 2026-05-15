cart = []

while True:
    print("1 Mahsulot qoshish")
    print("2 Savatni korish")
    print("3 Chiqish")

    choice = input("Tanlang: ")

    if choice == "1":
        product = input("Mahsulot nomi: ")
        cart.append(product)

    elif choice == "2":
        print("Savat:")

        for item in cart:
            print(item)

    elif choice == "3":
        break

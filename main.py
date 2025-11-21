def check_age():
    age = int(input("Введіть свій вік: "))

    if age >= 18:
        print("Ви можете використовувати цей сервіс")
    else:
        print("Вам має бути 18 років або більше")


check_age()

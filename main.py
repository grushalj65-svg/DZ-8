def login():
    correct_user = "admin"
    correct_pass = "12345"

    username = input("Введіть ім'я користувача: ")
    password = input("Введіть пароль: ")

    if username == correct_user and password == correct_pass:
        print("Вхід виконано успішно")
    else:
        print("Невірне ім'я користувача або пароль")

login()


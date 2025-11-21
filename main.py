def process_list():

    data = input("Введіть елементи списку через кому: ")        # Користувач вводить елементи через кому
    input_list = []
    i = 0
    while i < 1000:  # обмежуємо кількість елементів
        try:

            input_list = data.split(",")          # Розділяємо рядок на елементи
            break
        except:
            print("Неправильний формат")
            break


    count = 0
    i = 0
    while i < 10000:
        try:
            _ = input_list[i]
            count = count + 1
            i = i + 1
        except IndexError:
            break

    if count >= 3:
        print("Список містить {} елементів".format(count))
    else:
        print("Список повинен містити принаймні 3 елементи")


process_list()

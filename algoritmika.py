def make_list(number):
    names = []
    for item in range(number):
        names.append(input("Введи имя с заглавной буквы"))
    return names

number = int(input("Сколько имен надо ввести?"))
names = make_list(number)

for name in names:
    if name[0] == "A":
        print("Имя", name, "начинается с буквы A")


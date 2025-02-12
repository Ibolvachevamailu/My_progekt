def user_ID(user_id, user_dict):
    if not user_id.isdigit() and user_id not in user_dict:
        print('введите цифры')
        return None
    return str(user_id).zfill(8)


def validate_name(name):
    if not name.isalpha() or name == '':
        print('ошибка')
        return None
    return name.capitalize()

def validate_surname(surname):
    if not surname.isalpha() or surname == '':
        print('ошибка')
        return None
    return surname.capitalize()


def validate_age():
    while True:
        try:
            age = int(input("Введите ваш возраст (от 18 до 60): "))
            if 18 <= age <= 60:
                return age
            else:
                print("Ошибка: возраст должен быть в диапазоне от 18 до 60. Попробуйте снова.")
        except ValueError:
            print("Ошибка: пожалуйста, введите корректное целое число.")


def main():
    users = {}

    while True:
        user_id = input('введите ID')
        if user_id == '':
            break
        user_id = user_ID(user_id, users)
        if user_ID(user_id, users) is None:
            continue
        print(user_ID(user_id, users))

        if user_id in users:
            print('повтор ID, введите снова')
            continue

        name = input('введите имя или пустую строку для выхода')
        if not name:
            break
        if validate_name(name) is None:
            continue

        # проверка имени
        print(validate_name(name))

        # проверка фамилии
        surname = input('введите фамилию или нажмите пробел для выхода')
        if not surname:
            break
        if validate_surname(surname) is None:
            continue
        print(validate_surname(surname))

        age2 = validate_age()
        print(f'введен возр {age2}')

        # создание словаря с данными
        users[user_id] = (validate_name(name), validate_surname(surname), age2)

    print(f'Данные пользователей:')
    for user_id in users:
        print(f'{users[user_id]}')

if __name__ == "__main__":
    main()


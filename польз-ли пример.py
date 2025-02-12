def is_valid_name(name):
    return name.isalpha() and name[0].isupper()


def is_valid_age(age):
    try:
        age = int(age)
        return 18 <= age <= 60
    except ValueError:
        return False


def is_valid_id(user_id, user_dict):
    return user_id.isdigit() and len(user_id) == 8 and user_id not in user_dict


def main():
    users = {}

    while True:
        first_name = input("Введите имя (или пустую строку для выхода): ")
        if not first_name:
            break

        # Проверка и корректировка имени
        if not is_valid_name(first_name):
            first_name = first_name.capitalize()

        last_name = input("Введите фамилию: ")
        if not is_valid_name(last_name):
            last_name = last_name.capitalize()

        age = input("Введите возраст: ")
        while not is_valid_age(age):
            age = input("Некорректный возраст, введите снова (18-60): ")

        user_id = input("Введите ID (должен состоять из 8 цифр): ")
        while not is_valid_id(user_id, users):
            user_id = input("Некорректный ID, введите снова (должен состоять из 8 уникальных цифр): ")

        users[user_id] = (first_name, last_name, age)  # Сохраняем данные

    print("Данные пользователей:", users)


if __name__ == "__main__":
    main()
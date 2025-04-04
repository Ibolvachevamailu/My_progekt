def user_ID(user_id, user_dict):
    if not user_id.isdigit() or user_id in user_dict or user_id == '':
        print('введите цифры')
        return None  # Возвращаем None в случае ошибки
    return str(user_id).zfill(8)

def validate_name(name):
    if not name.isalpha() or name == '':
        print('ошибка')
        return None  # Возвращаем None в случае ошибки
    return name.capitalize()

def validate_surname(surname):
    if not surname.isalpha() or surname == '':
        print('ошибка')
        return None  # Возвращаем None в случае ошибки
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
        user_id = input('введите ID: ')
        if user_ID(user_id, users) is None:
            continue  # Если возникла ошибка, возвращаемся к вводу ID

        name = input('введите имя или нажмите пробел для выхода: ')
        if not name:
            break

        # Проверка имени
        if validate_name(name) is None:
            continue  # Если имя невалидно, возвращаемся к вводу имени

        # Проверка фамилии
        surname = input('введите фамилию или нажмите пробел для выхода: ')
        if not surname:
            break
        if validate_surname(surname) is None:
            continue  # Если фамилия невалидна, возвращаемся к вводу фамилии

        age2 = validate_age()  # Возраст запрашивается в любом случае
        print(f'введен возрасть: {age2}')

# Запуск основной функции
if __name__ == "__main__":
    main()
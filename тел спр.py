def phonebook_menu():
    # Начальные контакты
    contacts = {
        "Мама": "+79001112233",
        "Папа": "+79002223344"
    }

    while True:
        # Вывод меню
        print("\n📱 Телефонный справочник")
        print("1. Показать все контакты")
        print("2. Добавить контакт")
        print("3. Найти контакт")
        print("4. Удалить контакт")
        print("5. Выйти")

        choice = input("Выберите действие (1-5): ")

        # 1. Показать контакты
        if choice == "1":
            print("\n📒 Все контакты:")
            # for name, phone in contacts.items():
            print(f" {contacts}")

        # 2.Добавить контакт
        if choice == "2":
            new_contact = input('введи контакт для добавления\n')
            new_number = input('введи номер для добавления\n')
            contacts[new_contact] = new_number
            print(f'✅контакт {new_contact} добавлен')

        # 3. Найти контакт
        elif choice == "3":
            name = input("Введите имя для поиска: ")
            if name in contacts:
                print(f"📞 Найден: {name} - {contacts[name]}")
            else:
                print("❌ Контакт не найден")

        # 4. Удалить контакт
        elif choice == "4":
            name = input("Введите имя для удаления: ")
            if name in contacts:
                del contacts[name]
                print(f"❌ Контакт {name} удален")
            else:
                print("❌ Контакт не найден")

        # 5. Выход
        elif choice == "5":
            print("До свидания! 👋")
            break

        # Неправильный ввод
        else:
            print("❌ Ошибка! Введите число от 1 до 5")


# Запускаем меню
phonebook_menu()
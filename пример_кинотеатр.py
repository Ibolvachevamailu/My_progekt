cinema = [[0, 1, 1, 0], [1, 0, 0, 0], [0, 1, 0, 0]]  # матрица мест в кинотеатре
required_tickets = 1  # количество требуемых билетов

# Переменная для хранения индекса найденного ряда
found_row = False

# Цикл по рядам
for row_index in range(len(cinema)):
    count = 0  # Счетчик свободных мест

    # Цикл по местам в ряду
    for seat in cinema[row_index]:
        if seat == 0:  # Проверяем, свободно ли место
            count += 1  # Увеличиваем счетчик свободных мест
            if count == required_tickets:  # Проверяем, достаточно ли мест
                found_row = row_index  # Сохраняем индекс ряда
                break  # Выходим из цикла
        else:
            count = 0  # Сбрасываем счетчик при занятом месте

    if found_row is not False:  # Если ряд найден, выходим из цикла по рядам
        break

# Вывод результата
if found_row is False:
    print(False)  # Подходящих мест нет
else:
    print(found_row)
# Написать упрощенную версию алгоритма сжатия RLE. Алгоритм RLE объединяет подряд идущие одинаковые символы, представляя их как количество повторений и сам символ.
#
# Пример:
#
# aaabbbbccccc → 3a4b5cНаписать упрощенную версию алгоритма сжатия RLE. Алгоритм RLE объединяет подряд

string_1 = input('введите строку ')
if not string_1:
    print("введена пустая строка")
else:
    count = 1
    result = []
    for i in range(1, len(string_1)):
        if string_1[i] == string_1[i - 1]:
            count += 1
        else:
            result.append(f'{count}{string_1[i - 1]}')
            count = 1
    result.append(f'{count}{string_1[-1]}')
    print(''.join(result))





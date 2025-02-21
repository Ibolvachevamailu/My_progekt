def rle_compress(input_string):
    if not input_string:
        return ""

    compressed = []
    count = 1

    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            compressed.append(f"{count}{input_string[i - 1]}")
            count = 1

    compressed.append(f"{count}{input_string[-1]}")  # Добавляем последний набор символов
    return ''.join(compressed)


# Пример использования
input_data = "aaabbbbccccc"
compressed_data = rle_compress(input_data)
print(compressed_data)  # Вывод: 3a4b5c

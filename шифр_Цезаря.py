text = input('введите текст ')
shift = int(input('введите ключ шифрования '))
result = ""
for char in text:
    if char.isalpha():
        start = ord('a') if char.islower() else ord('A')
        shifted_code = (ord(char) - start + shift) % 26 + start
        result += chr(shifted_code)
    else:
        result += char
print(result)



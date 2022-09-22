# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def compression(text):
    count = 1
    result = ''
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            count += 1
        else:
            result += str(count) + text[i]
            count = 1
    if count > 1 or (text[len(text)-2] != text[-1]):
        result += str(count) + text[-1]
    return result

def data_recovery(text):
    number = ''
    result = ''
    for i in range(len(text)):
        if not text[i].isalpha():
            number += text[i]
        else:
            result += text[i] * int(number)
            number = ''
    return result


with open('file.txt', 'r') as data:
    text = data.read()

with open('coding_file.txt', 'w') as data:
    text = data.write(compression(text))

with open('coding_file.txt', 'r') as data:
    cod_text = data.read()


with open('de_coding_file.txt', 'w') as data:
    text = data.write(data_recovery(cod_text))

print("Текст после сжатия в файле 'coding_file.txt'")
print("Текст после восстановления в файле 'de_coding_file.txt'")
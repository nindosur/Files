import os
    # 1
with open('text.txt', 'r') as file:
    text = file.read()
with open('bad_words.txt', 'r') as file:
    bad_words = file.read().split()
for word in bad_words:
    text = text.replace(word, '***')

with open('clean_text.txt', 'w') as file:
    file.write(text)

    # 2
def translit_choice():
    print("Выберите направление перевода:")
    print("1. Русский -> Английский")
    print("2. Английский -> Русский")
    choice = int(input("Введите выбранное число: "))
    return choice

def translit(text, direction):
    translit_dict = {
            'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh',
            'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
            'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts',
            'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu',
            'я': 'ya', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo',
            'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
            'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H',
            'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Sch', 'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E',
            'Ю': 'Yu', 'Я': 'Ya'
        }
    if direction == 1:
        return "".join([translit_dict.get(char, char) for char in text])
    elif direction == 2:
        reverse_translit_dict = {v: k for k, v in translit_dict.items()}
        return "".join([reverse_translit_dict.get(char, char) for char in text])

def translit_file():
    direction = translit_choice()
    with open('text.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    with open('translate_text.txt', 'w', encoding='utf-8') as f:
        f.write(translit(text, direction))
    print("Текст успешно транслитерирован и записан в выходной файл.")
translit_file()

    # 3
with open('result.txt', 'w') as result_file:
    while True:
        filename = input('Введите имя файла или "quit", чтобы закончить: ')
        if filename == 'quit':
            break
        try:
            with open(filename, 'r') as file:
                result_file.write(file.read())
        except FileNotFoundError:
            print(f'Ошибка: файл {filename} не найден, в окончании файла обязательно необходимо дописывать формат (.txt)')

    # 4
files = []
while True:
    filename = input("Введите название файла (или 'quit' для завершения): ")
    if filename == "quit":
        break
    files.append(filename)

characters = []
for filename in files:
    with open(filename, "r", encoding='utf-8') as f:
        file_chars = set(f.read())
        if not characters:
            characters = file_chars
        else:
            characters.intersection_update(file_chars)

with open("result.txt", "w", encoding='utf-8') as f:
    f.write("".join(characters))


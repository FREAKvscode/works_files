def found_and_count(word, text, search_results):
    with open(text, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    counter = 0
    number_line = []
    for number, line in enumerate(lines, 1):
        if word in line:
            counter_in_line = line.count(word)
            counter = counter + counter_in_line
            number_line.append(number)

    if counter > 0:
        found = 'ДА'
    else:
        found = 'НЕТ'

    with open(search_results, 'w', encoding='utf-8') as f:
        f.write(f"Найдено ли слово: {found}\n")
        f.write(f"Сколько раз оно встречается: {counter}\n")
        f.write(f"В каких строках встречается : {number_line}\n")


if __name__ == '__main__':
    string = input("Введите слово для поиска: ")
    found_and_count(string, 'text.txt', 'search_results.txt')




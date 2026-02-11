def sort_words(words, sorted_alphabetically, sorted_by_length, sorted_reverse):
    with open(words, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file]

    lst_alpha = sorted(lines)
    lst_len = sorted(lines, key=len)
    lst_alpha_reverse = sorted(lines, reverse=True)

    with open(sorted_alphabetically, 'w', encoding='utf-8') as file:
        for word in lst_alpha:
            file.write(word + '\n')

    with open(sorted_by_length, 'w', encoding='utf-8') as file:
        for word in lst_len:
            file.write(word + '\n')

    with open(sorted_reverse, 'w', encoding='utf-8') as file:
        for word in lst_alpha_reverse:
            file.write(word + '\n')


if __name__ == '__main__':
    sort_words('words.txt', 'sorted_alphabetically.txt', 'sorted_by_length.txt', 'sorted_reverse.txt')



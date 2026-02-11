def read_and_combined(file1, file2, file3, combined):
    lst_files = [file1, file2, file3]
    contents = []

    for filename in lst_files:
        with open(filename, 'r', encoding='utf-8') as f:
            contents.append(f.read())

    with open(combined, 'w', encoding='utf-8') as f:
        for number, content in enumerate(contents):
            f.write(f'=== Содержимое {lst_files[number]} ===\n')
            f.write(content)
            f.write('\n\n')


if __name__ == '__main__':
    read_and_combined('file1.txt', 'file2.txt', 'file3.txt', 'combined.txt')



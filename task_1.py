def count_lines_and_words(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    line_count = len(lines)
    word_count = 0
    for line in lines:
        words = line.split()
        word_count += len(words)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"Количество строк: {line_count}\n")
        f.write(f"Количество слов: {word_count}\n")

if __name__ == "__main__":
    count_lines_and_words('input.txt', 'statistics.txt')




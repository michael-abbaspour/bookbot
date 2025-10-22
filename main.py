from stats import count_words, char_count, print_report
import sys

def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>");
        sys.exit(1);

    book_filepath = sys.argv[1];
    file_contents = get_book_text(book_filepath)
    num_words = count_words(file_contents)
    count_chars = char_count(file_contents)
    sorted_report = print_report(count_chars)

    # Bookbot Title
    print("============ BOOKBOT ============");
    print(f"Analyzing book found at {book_filepath}");
    # Word Count
    print("----------- Word Count ----------");
    print(f"Found {num_words} total words");
    # Character Count
    print("--------- Character Count -------");
    for item in sorted_report:
        print(f"{item['char']}: {item['num']}");



main()

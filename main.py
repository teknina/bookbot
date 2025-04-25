import sys
from stats import get_book_text, count_words, count_characters, sort_character_counts

def print_usage_and_exit():
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    # 1. Check for exactly one argument (the script name + book path)
    if len(sys.argv) != 2:
        print_usage_and_exit()

    # 2. Use the provided path
    book_path = sys.argv[1]

    # 3. Read the book, count words and characters, then print
    text = get_book_text(book_path)
    count_words(text)

    char_counts = count_characters(text)
    sorted_counts = sort_character_counts(char_counts)

    print("\nSorted character counts:")
    for entry in sorted_counts:
        print(f"{entry['char']}: {entry['num']}")
main()
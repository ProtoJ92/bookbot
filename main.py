import sys
from stats import get_num_words, get_char_counts, sort_char_counts

def get_book_text(filepath):
    """Reads a text file and returns its content as a string."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]  # ✅ Use command-line path
    text = get_book_text(path)  # ✅ This must use the provided path

    num_words = get_num_words(text)
    char_counts = get_char_counts(text)
    sorted_chars = sort_char_counts(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        char = item["char"]
        if char.isalpha():
            print(f"{char}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()

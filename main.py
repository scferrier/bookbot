from stats import get_num_words, char_count, char_dict_sorted
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(fp):
    with open(fp, encoding="utf-8") as f:
        return f.read()

def main():
    #path = "books/frankenstein.txt"
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    
    text = get_book_text(path)

    # Word count
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")

    # Character count (letters only, case-insensitive, incl. accented letters)
    print("--------- Character Count -------")
    letters_only = "".join(ch.lower() for ch in text if ch.isalpha())
    counts = char_count(letters_only)
    sorted_chars = char_dict_sorted(counts)

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()

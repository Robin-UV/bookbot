from stats import get_book_text
from stats import get_word_count
from stats import get_character_occurance
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]

    file_contents = get_book_text(book_path)

    num_words = get_word_count(file_contents)
    character_data = get_character_occurance(file_contents)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for item in character_data:
        print(f"{item['char']}: {item['num']}")


main()
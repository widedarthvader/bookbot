import sys
from stats import get_word_count
from stats import get_character_count
from stats import sort_characters


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    arguments = len(sys.argv)
    if arguments < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
    console = get_book_text(path)
    total = get_word_count(console)
    total_chars = get_character_count(console)
    sorted_chars = sort_characters(total_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f'Found {total} total words')
    print("--------- Character Count -------")

    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        if not char.isalpha():
            continue
        print(f"{char}: {count}")

    print("============= END ===============")
main()

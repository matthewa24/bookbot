from stats import get_num_chars, get_num_words

import sys

def read_file(file_path):
    with open(file_path) as f:
        return(f.read())
    
def run_report(book, num_words, num_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for n in num_chars:
        c = n["char"]
        count = n["count"]
        print(f"{c}: {count}")

    print("============= END ===============")


def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    content = read_file(book)
    num_words = get_num_words(content)
    num_chars = get_num_chars(content)
    run_report(book, num_words, num_chars)

main()
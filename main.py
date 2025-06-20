
from stats import get_num_words, letter_count, sorted_list


book_path = "books/frankenstein.txt"

## takes the file path as an input

def get_book_text(book_path):

    ## opens the file path as f andreads f then returns f
    with open(book_path) as f:
        content = f.read()
    return content


def main():
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    letter_counts = letter_count(book_text)
    sorted_counts = sorted_list(letter_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_counts:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
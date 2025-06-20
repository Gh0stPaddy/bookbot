
from stats import get_num_words, letter_count


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
    print(f"{num_words} words found in the document")
    print(letter_counts)

main()
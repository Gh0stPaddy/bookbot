import sys
from stats import get_num_words, letter_count, sorted_list

## sys.argv prints out a list of location of where the command has run from
## sys.argv[1] will access the 2nd placement in the list (i.e your argument here, the path to the book)
## this merely gives some error handling if someone doesn't correctly add the correct path to the book (books/{name_of_book})

list_length = len(sys.argv)
if list_length != 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path = sys.argv[1]


## takes the file path as an input

def get_book_text(book_path):

    ## opens the file path as f andreads f then returns f
    with open(book_path) as f:
        content = f.read()
    return content


## Main function - calling all other functions and handling the work
## book_text uses the get_book_text function to get all the words into the function
## num_words (imported from stats.py) splits the words and counts them (using len)
## letter_counts (imported from stats.py) sets all letts to lower-case, creates an empty list, loops through the dict and then adds a key pair of char, num
## sorted_counts (imported from stats.py) uses two functions, def sort_on and def_sorted list
## def sort_on, sorts through the "num" part of the dict
## def sorted_list creates an empty list, loops through the dict, appends to the new list char and num, the uses the sort on function to sort in ascending order
## could use lambda for this - just not enough brain to work it out
##finally prints out report - then loops through the sorted_counts, using isalpha() <- creates a check if all characters are alphabet latters, then prints output

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
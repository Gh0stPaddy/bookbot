
## Counts words in input text file

def get_num_words(text):
    words = text.split()
    return len(words)


## Breaks down input from text file and does a count of characters / symbols

def letter_count(text):
    text = text.lower()
    letter_dict = {}
    for letter in text:
        if letter in letter_dict:
            letter_dict[letter] +=1
        else:
            letter_dict[letter] = 1
    return letter_dict


## Sort on num dict

def sort_on(item):
    return item["num"]

## Function that takes a dict input and will sort
def sorted_list(letter_dict):
    my_list = []
    for char, count in letter_dict.items():
        my_list.append({"char": char, "num": count})
    my_list.sort(reverse=True, key=sort_on)
    return my_list




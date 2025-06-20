
def get_num_words(text):
    words = text.split()
    return len(words)

def letter_count(text):
    text = text.lower()
    letter_dict = {}
    for letter in text:
        if letter in letter_dict:
            letter_dict[letter] +=1
        else:
            letter_dict[letter] = 1
    return letter_dict

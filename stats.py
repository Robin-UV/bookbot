import string

def get_book_text(path_to_file): 
    with open(path_to_file) as f:
        return f.read()


def get_word_count(file_contents):
    split_words = file_contents.split()
    num = len(split_words)
    return num

def sort_on(item):
    return item["num"]

def get_character_occurance(file_contents):
    lower_text = file_contents.lower()
    result_list = []

    for letter in string.ascii_lowercase:
        count = lower_text.count(letter)
        result_list.append({"char": letter, "num": count})

    result_list.sort(reverse=True, key=sort_on)

    return result_list


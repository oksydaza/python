TEXTFILE = "input.txt"
WORD_LENGTH = 5
MAX_COUNT = 20

def get_text(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = f.read()
    return(data)

def split_text(input_file):
    input_file_splited = input_file.split()
    return(input_file_splited)

def delete_short_words(input_array, length):
    result_array = []
    for word in input_array:
        if len(word) < length: 
            continue
        else:
            result_array.append(word)
    return(result_array)

def delete_chars(input_text):
    new_text = input_text
    new_text = new_text.replace(':', '')
    new_text = new_text.replace('.', '')
    new_text = new_text.replace(';', '')
    new_text = new_text.replace(',', '')
    new_text = new_text.replace('?', '')
    new_text = new_text.replace('!', '')
    new_text = new_text.replace('«', '')
    new_text = new_text.replace('»', '')
    new_text = new_text.replace('…', '')
    new_text = new_text.replace('(', '')
    new_text = new_text.replace(')', '')
    new_text = new_text.replace('*', '')
    return new_text

def generate_freq_dict(input_text):
    """Function generates frequenc dictionary.

    For each word in input_text is lowecased, then checked if already existing
    in dictionary. If yes, increment counter. If not, insert word and set counter
    for this word to 1.

    Args:
        input_text (array of words): e.g ("word1", "word2")

    Returns:
        dict: With unsorted dictonary with word and counter pairs
      

    """
    result_dict = {}
    for word in input_text:
        word = word.lower()
        if word not in result_dict:
            result_dict[word] = 1
        else:
            result_dict[word] += 1
    return(result_dict)

def get_sorted_decreasing(unsorted, max_count):
    """Function prints sorted elements.

    Args:
        unsorted (dictionary): Dictionary e.g. result_dict['word'] = 1
        max_count (int): Limit result to max count.

    """
    
    for counter, w in enumerate(sorted(unsorted, key=unsorted.get, reverse=True)):
        print(w, unsorted[w])
        if counter >= max_count - 1:
            break

def main():
    text = get_text(TEXTFILE)
    text_without_special_chars = delete_chars(text)
    splited_text = split_text(text_without_special_chars)
    valid_text = delete_short_words(splited_text, WORD_LENGTH)
    freq_dict = generate_freq_dict(valid_text)
    sorted_freq_dict = get_sorted_decreasing(freq_dict, MAX_COUNT)

if __name__== "__main__":
  main()

""" Wynik działania programu:
rzekł 155
tylko 149
rabia 129
sędzia 127
tadeusz 105
przed 102
#jeszcze 101
#przez 97
#gdzie 94
#wszyscy 90
#wojski 89
#potem 86
#teraz 83
#niech 76
#kiedy 74
#jeśli 73
#który 72
#nawet 71
#znowu 71
#wszystko 67"""

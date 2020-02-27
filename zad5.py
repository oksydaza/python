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
    result_dict = {}
    for word in input_text:
        word = word.lower()
        if word not in result_dict:
            result_dict[word] = 1
        else:
            result_dict[word] += 1
    return(result_dict)

def get_sorted_decreasing(unsorted, max_count):
    
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

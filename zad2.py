TEXTFILE = "input.txt"

def get_text(input_file):
    with open(input_file, 'r') as f:
        data = f.read()

    return(data)

def split_text(input_file):
    input_file_splited = input_file.split()

    return(input_file_splited)

def main():
    text = get_text(TEXTFILE)
    splited_text = split_text(text)
    print(splited_text)

if __name__== "__main__":
  main()

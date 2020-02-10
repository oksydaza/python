TEXTFILE = "input.txt"

def get_text(input_file):
    with open(input_file, 'r') as f:
        data = f.read()

    return(data)

def main():
    text = get_text(TEXTFILE)
    print(text)

if __name__== "__main__":
  main()


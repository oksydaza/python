def cipher_groensfeld(key, name_file, action):
    """Function encrypts file. 

    defines the alphabet. capitalize letters from input text.
    getting the key length. Translate key (string) to table of int. Getting key length for each word.
    For each letter in word, get index and add value from table_key, and save the file.
    """
    start_text = ''
    text = read_file(name_file)
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]    
    table_word = text.upper().split()
    lenght_key = len(str(key))    
    table_key = [int(c) for c in str(key)]
    lenght_alphabet = len(alphabet)
    
   
    for word in table_word:        
        lenght_word = len(word)        
        new_word = ''
        
        counter = 0
            
        for letter in word:            
            index_letter = alphabet.index(letter)            
            if action == 'encrypt':
                index_replacement = index_letter + table_key[counter]
            else:
                index_replacement = index_letter - table_key[counter]
            
            if lenght_alphabet > index_replacement:
                new_word += alphabet[index_replacement]            
            else:                
                index_off = index_replacement - lenght_alphabet
                new_word += alphabet[index_off]
            
            counter += 1
            
            if (lenght_key < lenght_word) and (counter > lenght_key - 1):
                counter = 0
        
        if start_text == '':
            start_text += new_word
        else:
            start_text += (" " + new_word)

    
    if action == 'encrypt':
        save_file(start_text, 'EncryptedText')
    else:
        save_file(start_text, 'DecryptedText')

    return start_text

def read_file(name_file):
    p = open(name_file,"r")
    text = p.read()
    p.close()
    return text

def save_file(text, name_file):
    p = open(name_file+'.txt', "w")
    p.write(text)
    p.close()

cipher_groensfeld(31206, 'input_test.txt', 'encrypt')
cipher_groensfeld(31206, 'EncryptedText.txt', 'decrypt')

"""Result:
Encrypted text: JPUPUGBTSZZP SPYRUW SBPIICB QB DMC PB NPVEICLC NPVEICLC
Decrypted text: GOSPODARSTWO POWROT PANICZA NA ALA MA KOTECZKA KOTECZKA


"""
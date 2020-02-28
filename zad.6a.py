def cipher_groensfeld(klucz, nazwa_pliku, akcja):
    start_text = ''
    text = read_file(name_file)
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    #rozbicie tekstu na tablicę słów
    table_word = text.upper().split()
    lenght_key = len(str(key))
    #rozbicie klucza na tablicę składowych cyfr
    table_key = [int(c) for c in str(key)]
    lenght_alphabet = len(alphabet)
    
    #iteracja przez każde słowo w tekście
    for word in table_word:
        #zmienna przechowująca długość słowa
        lenght_word = len(word)
        #zmienna przechowująca nowe słowo
        new_word = ''
        #ustawienie licznika długości klucza
        counter = 0
            
        #iteracja po literach słowa
        for letter in word:
            #znalezienie indeksu litery w alfabecie
            index_letter = alphabet.index(letter)
            #konkatenacja podmienionych liter do slowa
            #flaga 'szyfruj' w wywołaniu funkcji informuje, że odbywa się akcja szyfrowania
            if share == 'szyfruj':
                index_replacement = index_letter + table_key[counter]
            else:
                index_replacement = index_letter - table_key[counter]
            #jesli indeks zastapienia nie wykracza poza indeks tablicy, to zastąp bezpośrednio, bo nie wykroczy poza granicę tablicy
            if lenght_alphabet > index_replacement:
                new_word += alphabet[index_replacement]
            #jesli indeks zastapienia wykracza poza indeks tablicy
            else:
                #odjęcie od większego indeksu długości alfabetu - w ten sposób uzyskujemy indeks liczony o dodatkowe indeksy, które były poza granicą, od początku
                index_off = index_replacement - lenght_alphabet
                new_word += alphabet[index_off]
            #inkrementacja licznika, jeśli klucz jest dłuższy niż 2
            counter += 1
            #jeśli słowo jest dłuższe od klucza i licznik wykracza poza indeks klucza, ustaw licznik na 0 (wtedy liczenie po indeksach klucza zacznie się od nowa)
            if (lenght_key < lenght_word) and (counter > lenght_key - 1):
                licznik = 0

        #konkatenacja zaszyfrowanego słowa pełnym tekstem, który będzie zwracać funkcja
        #nie dodawaj spacji, jeśli to początek tekstu
        if start_text == '':
            start_text += new_word
        else:
            start_text += (" " + new_word)

    #jeśli flaga to 'szyfruj', zapisz plik z zaszyfrowanym tekstem
    if share == 'szyfruj':
        save_file(start_text, 'ZaszyfrowanyTekst')
    else:
        save_file(start_text, 'OdszyfrowanyTekst')

    return start_text

#funkcja wczytująca dany plik .txt i zwraca jego zawartość
def read_file(new_file):
    p = open(name_file,"r")
    text = p.read()
    p.close()
    return text

#funkcja zapisująca plik z rezultatem szyfrowania
def save_file(text, name_file):
    p = open(name_file+'.txt', "w")
    p.write(text)
    p.close()

#wywołanie funkcji szyfrowania (trzeci parametr w funkcji to flaga determinująca czy szyfrowanie lub odszyfrowanie)
cipher_groensfeld(31206, 'DoZaszyfrowania.txt', 'szyfruj')
#DoZaszyfrowania.txt zawiera tekst 'programowanie jest super'
#rezultatem jest zapisany plik 'ZaszyfrowanyTekst.txt'
#zawartość: SSQGXDNQWGQJG MFUT VVREX

#wywołanie funkcji odszyfrowania
cipher_groensfeld(31206, 'ZaszyfrowanyTekst.txt', 'odszyfruj')
#'ZaszyfrowanyTekst.txt' zawiera tekst 'SSQGXDNQWGQJG MFUT VVREX'
#rezultatem wywołania jest nowo powstały plik tekstowy OdszyfrowanyTekst.txt z zawartością:
#PROGRAMOWANIE JEST SUPER

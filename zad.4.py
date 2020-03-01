import numpy as np
import time

def sieve(n, registery):
    for i in range(2, n + 1):
        for j in range(i, n + 1):
            if j > i and j % i == 0 and j in registery:
                if isinstance(registery, list): registery.remove(j)
                elif isinstance(registery, dict): del registery[j]
                elif isinstance(registery, np.ndarray):
                    registery = np.delete(registery, np.where(registery == j))
    """Function generates frequenc dictionary.

    For each word in input_text is lowecased, then checked if already existing
    in dictionary. If yes, increment counter. If not, insert word and set counter
    for this word to 1.

    Args:
        n (int): e.g ("39", "5367")
        registery (int): e.g ("39", "5367")


    Returns:
        dict: With unsorted dictonary with word and counter pairs
      

    """            
    
            
    return registery


n = int(input("Wpisz liczbę naturalną domykającą przedział: "))

if n <= 2: print("Liczba musi być większa niż 2")

else:
    sieve_list = list(range(2, n + 1))
    sieve_dictionary = {i : '' for i in range(2, n + 1)}
    sieve_numpy_array = np.array([i for i in range(2, n + 1)])

    start = time.time()
    sieve(n, sieve_list)
    end = time.time()
    print("Czas wykonania przy użyciu listy wyniósł %d s" % (end - start))

    start = time.time()
    sieve(n, sieve_dictionary)
    end = time.time()
    print("Czas wykonania przy użyciu słownika wyniósł %d s" % (end - start))

    start = time.time()
    sieve(n, sieve_numpy_array)
    end = time.time()
    print("Czas wykonania przy użyciu tablicy ze słownika wyniósł %d s\n" % (end - start))

    print("Liczby pierwsze w zadanym przedziale:")
    print(sieve_list)


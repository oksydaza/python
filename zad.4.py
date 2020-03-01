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
            
    
            
    return registery


n = int(input("Enter the natural number closing the interval: "))

if n <= 2: print("The number must be greater than 2")

else:
    sieve_list = list(range(2, n + 1))
    sieve_dictionary = {i : '' for i in range(2, n + 1)}
    sieve_numpy_array = np.array([i for i in range(2, n + 1)])

    start = time.time()
    sieve(n, sieve_list)
    end = time.time()
    print("The execution time using the list was %d s" % (end - start))

    start = time.time()
    sieve(n, sieve_dictionary)
    end = time.time()
    print("The execution time using the dictionary was %d s" % (end - start))

    start = time.time()
    sieve(n, sieve_numpy_array)
    end = time.time()
    print("The execution time using the table from the dictionary was %d s\n" % (end - start))

    print("Prime numbers in a given range:")
    print(sieve_list)


    """
    The function searches for prime numbers.
    The range of the range is defined by the user.

    Result:

    Enter the natural number closing the interval: 34
    The execution time using the list was 0 s
    The execution time using the dictionary was 0 s
    The execution time using the table from the dictionary was 0 s

    Prime numbers in a given range:
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    """


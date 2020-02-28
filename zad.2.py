def get_armstrong_numbers(max_number):
    """Function prints Armstrong numbers.

    Args:
        max_number (int): e.g ("12457")  

    """
  print('Liczby Armstronga to:')

  for i in range(1, max_number):            
      num_length = len(str(i))          
      power = int(num_length) 
      digit_sum = 0 
      num = i  
      while num > 0: 
        digit = num % 10 
        digit_sum += pow(digit, power) 
        num //= 10

      if i == digit_sum:
        print(i) 
def main():
    get_armstrong_numbers(50000000)


if __name__== "__main__":
  main()



# Wynik działania programu:
#Liczby Armstronga to:
#1
#2
#3
#4
#5
#6
#7
#8
#9
#153
#370
#371
#407
#1634
#8208
#9474
#54748
#92727
#93084
#548834
#1741725
#4210818

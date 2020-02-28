print('Liczby Armstronga to:')

for i in range(1, 5000000):             #Program wypisuje liczby Armstronga zawierające się w określonym przedziale
    num_length = len(str(i))            #Im większy przedział liczbowy, tym program działa wolniej
    power = int(num_length) 
    digit_sum = 0 
    num = i  
    while num > 0: 
      digit = num % 10 
      digit_sum += pow(digit, power) 
      num //= 10

    if i == digit_sum:
      print(i) 



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

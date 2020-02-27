for i in range(1, 10000):
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

print('Liczby Armstronga')

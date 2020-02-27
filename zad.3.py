def szukaj_palindromu(num):
    sum = 0
    sum += int(num)

    # pętla działa tak długo, kiedy sum rzutowane na string nie jest taka sama jak string od tyłu
    while str(sum) != str(sum)[::-1]:
        # przypisanie zmiennej next_num sumy od tyłu
        next_num = int(str(sum)[::-1])
        # sumowanie obu liczb
        sum += next_num
    return sum

# pętla sprawdzająca palindromy dla liczb 0 - 200
for i in range(1, 201):
    # program wpadnie w nieskończoną pętlę przy 200 i 196. Dla tych liczb nie można osiągnąć palindromu
    if(i != 196 and i != 200):
        print('Palindrom dla liczby {}:'.format(i), szukaj_palindromu(i))
    else:
        print('Nie istnieje palindrom dla {}'.format(i))

print('Koniec wyszukiwania')

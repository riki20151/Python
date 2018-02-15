koloda = [6,7,8,9,10,2,3,4,11] * 4
import random
random.shuffle(koloda)
print('Поиграем в очко?')
count = 0
while True:
    choice = input('Будете брать карту? y/n\n')
    if choice == 'y':
        current = koloda.pop()
        print('Вам попалась карта достоинством %d' %current)
        count += current
        if count > 21:
            print('Извините, Вы проиграли')
            break
        elif count == 21:
            print('Поздравляем с победой')
            break
        else:
            print(' У Вас %d очков' %count)
            break
    else:
        print('Ну как хотите')
        break
print('До новых встреч!')

def Count ( desk ):
    random.shuffle(desk)
    count = 0
    while True:
        current = desk.pop()
        print('Вам попалась карта достоинством %d' %current)
        count += current
        if count > 21:
            print('Результат %d' %count)
            return count
        if count == 21:
            print('Вы выиграли')
            return count


MyDesk = [6,7,8,9,10,2,3,4,11,1] * 4
import random
random.shuffle(MyDesk)
print("Первый игрок")
player1 = Count(MyDesk)
print("Второй игрок")                                     
player2 = Count(MyDesk)
if player1 > player2:
    print("Второй игрок победил")
elif player1 < player2:
   print("Первый игрок победил")
else:
   print("Нечья")


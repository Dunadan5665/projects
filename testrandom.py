import random

player = random.randint(2, 12)
computer = random.randint(2, 12)
money_player = 5

while money_player > 0:

    input('Нажмите ENTER чтобы сыграть')
    player = random.randint(2, 12)
    computer = random.randint(2, 12)

    print('Вы выбросили', player)
    print('Компьютер выбросил', computer)

    if player > computer:
        print('Вы победили!')
        money_player += 1

    elif player < computer:
        print('Победил компьютер!')
        money_player -= 1

    else:
        print('Ничья')

    if money_player == 0:
        print('Деньги кончились! Конец игры!')
        break
    print('У вас', money_player, 'монет')



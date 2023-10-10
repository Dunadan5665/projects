from random import randint

player_name = 'Исилдур'
player_hp = 10
player_xp = 0
player_level = 1
player_money = 0

enemy_name = 'Саурон'
enemy_hp = 1
enemy_xp = 0
enemy_level = 1000
enemy_money = 0

print(player_namme, 'Находится на распутье')
print('Если идти направо, то прийдёшь к игре в кости')
print('Если идти налево, то прийдёшь к врагам')
input(path = 'Куда ехать?')

if path == 'налево':
    print('Против', player_name, 'сражается', enemy_name)
    while player_hp > 0 and enemy_hp > 0:
        input('Нажмите ENTER чтобы начать раунд')
        enemy_hit = randint(1, 20)
        if enemy_hit <= 10 :
            print(enemy_name, 'промахнулся!')
        if enemy_hit >= 11:
            enemy_attack = randint(1, 10)
            player_hp -= enemy_attack
            print(enemy_name, 'ударил', player_name, 'на', enemy_attack)
            print('У', player_name, 'стало', player_hp, 'жизней.')
            if player_hp <= 0:
                print(enemy_name, 'убил', player_name, 'бой окочен!')
                break
        player_hit = randint(1, 20)
        if player_hit <= 10 :
            print(player_name, 'промахнулся!')
        if player_hit >= 11:
            player_attack = randint(1, 10)
            enemy_hp -= player_attack
            print(player_name, 'ударил', enemy_name, 'на', player_attack)
            print('У', enemy_name, 'стало', enemy_hp, 'жизней.')
            if enemy_hp <= 0:
                print(player_name, 'убил', enemy_name, 'бой окончен!')
                player_xp += enemy_level
                if player_xp >= 10:
                    print('У', player_name, player_xp, 'xp')
                    level_change = player_xp // 10
                    player_level += level_change
                    player_xp = player_xp % 10
                    print('Уровень', player_name, 'равен', player_level)
                    print('Теперь у', player_name, player_xp, 'xp')

if path == 'направо':
    player = randint(2, 12)
    computer = randint(2, 12)

    while player_money > 0:

        input('Нажмите ENTER чтобы сыграть')
        player = randint(2, 12)
        computer = randint(2, 12)

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



                



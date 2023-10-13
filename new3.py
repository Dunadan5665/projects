from random import randint

player_name = 'Исильдур'
player_hp = 10
player_xp = 0
player_level = 1
money_player = 1000
player_telum = 'меч'
player_armor = 'Комплект мифрильной брони'

enemy_name = 'Саурон'
enemy_xp = 0
enemy_level = 10
enemy_money = 0

while player_hp > 0:

    enemy_hp = 10
    
    print(player_name, 'Находится на распутье.')
    print('Если идти направо, то прийдёшь к игре в кости.')
    print('Если идти налево, то прийдёшь к врагам.')
    print('Если поедешь прямо, то приедешь в магазин.')

    path = input('Куда ехать? ')

    if path == 'налево':
        print('Против', player_name, 'сражается', enemy_name)
        while player_hp > 0:
            input('Нажмите ENTER чтобы начать раунд')
            print('--------------------------------')
            enemy_hit = randint(1, 20)
            if player_armor == 'броня':
                if enemy_hit <= 10:
                    print(enemy_name, 'промахнулся!')
                    print('----------------------------')
                if enemy_hit >= 11:
                    enemy_attack = randint(1, 10)
                    player_hp -= enemy_attack
                    print(enemy_name, 'ударил', player_name, 'на', enemy_attack)
                    print('У', player_name, 'стало', player_hp, 'жизней.')
                    print('----------------------------')
                    if player_hp <= 0:
                        print(enemy_name, 'убил', player_name, 'Игра окончена!')
                        print('----------------------------')
                        break
                    
            if player_armor == 'Комплект мифрильной брони':
                if enemy_hit <= 15:
                    print(enemy_name, 'промахнулся!')
                    print('----------------------------')
                if enemy_hit >= 16:
                    enemy_attack = randint(1, 10)
                    player_hp -= enemy_attack
                    print(enemy_name, 'ударил', player_name, 'на', enemy_attack)
                    print('У', player_name, 'стало', player_hp, 'жизней.')
                    print('----------------------------')
                    if player_hp <= 0:
                        print(enemy_name, 'убил', player_name, 'Игра окончена!')
                        print('----------------------------')
                        break


                
            player_hit = randint(1, 20)
            if player_hit <= 10 :
                print(player_name, 'промахнулся!')
                print('----------------------------')
            if player_hit >= 11:
                if player_telum == 'меч':
                    player_attack = randint(1, 10)
                if player_telum == 'Мифрильный меч':
                    player_attack = randint(21, 30)
                enemy_hp -= player_attack
                print(player_name, 'ударил', enemy_name, 'на', player_attack)
                print('У', enemy_name, 'стало', enemy_hp, 'жизней.')
                print('----------------------------')
                if enemy_hp <= 0:
                    print(player_name, 'убил', enemy_name, 'бой окончен!')
                    print('----------------------------')
                    player_xp += enemy_level
                    if player_xp >= 10:
                        print('У', player_name, player_xp, 'xp')
                        level_change = player_xp // 10
                        player_level += level_change
                        player_xp = player_xp % 10
                        print('Уровень', player_name, 'равен', player_level)
                        print('Теперь у', player_name, player_xp, 'xp')
                        print('--------------------------------------')

                        
    elif path == 'направо':
        print('У вас 5 монет, хотите сыграть?')

        while money_player > 0:

            input('Нажмите ENTER чтобы сыграть')
            player = randint(2, 12)
            computer = randint(2, 12)

            print('Вы выбросили', player)
            print('Компьютер выбросил', computer)

            if player > computer:
                print('Вы победили!')
                money_player += 1
                print('----------------')

            elif player < computer:
                print('Победил компьютер!')
                money_player -= 1
                print('----------------')

            else:
                print('Ничья')
                print('----------------')

            if money_player == 0:
                print('Деньги кончились! Конец игры!')
                break
            print('У вас', money_player, 'монет')

    elif path == 'прямо':
        print('Добро пожаловать в мою скромную лавку!')
        print('Меня зовут Араност и я могу предложить хорошие товары за приемлемою цену!')
        print('Для начала выберите категорию из предложенных')
        print('У вас', money_player, 'монет.')
        genus = input('оружие,   защита,   вылечить ')

        if genus == 'оружие':
            print('Мифрильный меч - 100м (измняет урон с 1-20 до 21-30)')
            resp = input('Покупаете? ')
            if resp == 'да':
                money_player -= 100
                player_telum = 'Мифрильный меч'
                print('Теперь ваше оружие - это', player_telum)
                print('А так же у вас теперь', money_player, 'монет.')
            if resp == 'нет':
                print('Очень жаль.')

        if genus == 'защита':
            print('Комплект мифрильной брони - 100м (изменяет сложность попадания по вам с 11 на 15)')
            resp = input('Покупаете?')
            if resp == 'да':
                money_player -= 100
                player_armor = 'Комплект мифрильной брони'
                print('Теперь ваше оружие - это', player_telum)
                print('А так же у вас теперь', money_player, 'монет.')
            if resp == 'нет':
                print('чень жаль.')

        if genus == 'вылечить':
            treatment = 10 - player_hp
            print('Я могу вылечить тебя за', treatment, 'монет.')
            resp = iput('Вы хотите этого?')
            if resp == 'да':
                money_player -= treatment
                player_hp = 10
                print('Теперь вы совершенно здоровы!')
            if resp == 'нет':
                print('Очень жаль.')
                       






    else:
        print('Такой дороги нет!')

        
print('Конец игры')



                



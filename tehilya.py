import os # для очистки экрана
from random import randint

'''
Игрок умеет сражаться 
играть в кости
покупать вещи в лавке

у игрока есть:
              имя
              здоровье
              деньги
              опыт
              уровень
'''


def start_game():
    '''
    создаёт игрока и отправляет его к камню
    '''
    player_name = input('Введите имя игрока: ') # имя игрока
    player_hp = 100 # здоровье игрока
    player_money = 1000 # деньги игрока
    player_xp = 0 # опыт игрока
    player_level = 1 # уровень игрока
    player_telum = 'обычный меч' # оружие игрока
    player_armor = 'обычная броня' # броня игрока

    enemy_name = 'Грышнак'
    enemy_hp = 100
    enemy_level = 1
    enemy_xp = 0
    enemy_money = 0
    enemy_telum = ''
    enemy_armor = ''

    damage = 0
    show_hero(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor)
    visit_rock(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor,
enemy_name, enemy_hp, enemy_level, enemy_xp, enemy_money, enemy_telum, enemy_armor, damage)
    

def show_hero(name, hp, money, xp, level, telum, armor):
    '''
    Выводит на экран инфо о персонаже
    '''
    print('имя:', name) # выводит имя героя
    print('здоровье:', hp) # выводит здоровье героя
    print('деньги:', money) # выводит деньги героя
    print('опыт:', xp) # выводит опыт героя
    print('уровень:', level) # выводит уровень героя
    print('Оружие', telum) # выводит оружие героя
    print('Оружие', armor) # выводит броню героя
    print('-' * 20)


def visit_rock(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor,
enemy_name, enemy_hp, enemy_level, enemy_xp, enemy_money, enemy_telum, enemy_armor, damage):
    '''
    Камень: выбор дороги
    '''
    show_hero(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor)
    os.system('cls') # очищает экран
    print(player_name, 'приехал к камню')
    print('1 - поехать на сражение')
    print('2 - поехать в таверну')
    print('3 - поехать заглянуть в лавку')
    print('0 - выйти из игры')
    option = input('введите номер варианта: ') # узнаёт у игрока, вариант ответа и записывает его в option
    if option == '1':
        visit_fight(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor,
    enemy_name, enemy_hp, enemy_level, enemy_xp, enemy_money, enemy_telum, enemy_armor, damage) 
    elif option == '2':
        print('Уехал в таверну')
        visit_tavern(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor)
    elif option == '3':
        visit_shop(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor)
    elif option == '0':
        print('Вышел из игры')
    else:
        visit_rock(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor,
enemy_name, enemy_hp, enemy_level, enemy_xp, enemy_money)


def pause():
    input('Нажмите ENTER чтобы продолжить')


def visit_tavern(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor):
    '''
    Можно играть в кости или вернуться к камню
    '''
    show_hero(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor)
    os.system('cls') # очищает экран
    print(player_name, 'приехал в таверну')
    print('1 - Сыграть в кости')
    print('2 - Вернуться к камню')
    print('0 - Выйти из игры')
    option = input('введите номер варианта: ') # узнаёт у игрока, вариант ответа и записывает его в option
    if option == '1':
        play_dice(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor)
    elif option == '2':
        visit_rock(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor)
    elif option == '0':
        print('вышел из игры')
    else:
        visit_tavern(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor)


def play_dice(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor):
    os.system('cls') # очищает экран
    show_hero(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor)
    bet = int(input('Введите ставку  '))
    if not player_money:
       print('У игрока НЕТ денег!')
       pause()
       visit_tavern(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor)
    elif bet < 1:
        print('ставка должна быть больше нуля!')
        pause()
        play_dice(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor)
    elif bet > player_money:
        print('У', player_name, 'нет столько денег')
        pause()
        play_dice(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor)
    
    player_score = randint(2, 12)
    tavern_score = randint(2, 12)
    print('Игрок выбросил', player_score)
    print('Трактирщик выбросил', tavern_score)
    if player_score > tavern_score:
        player_money += bet
        print(player_name, 'выйграл', bet, 'монет')
        pause()
    elif player_score < tavern_score:
        player_money -= bet
        print(player_name, 'выйграл', bet, 'монет')
        pause()
    else:
        print('Ничья!')

    visit_tavern(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor)


def visit_shop(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor):
    '''
    Приводит игрока в лавку. Можно делать покупки и лечиться до 10 hp за деньги.
    '''
    os.system('cls') # очищает экран
    show_hero(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor)
    print(player_name, 'приехал в лавку и с ним говорит лавочник.')
    print('Меня зовут Араност и я могу предложить хорошие товары за приемлемою цену!')
    print('Для начала выберите категорию из предложенных')
    print('оружие - 1,   защита - 2,   вылечить игрока - 3, вернуться к камню - 4, выход из игры - 0')
    print('У вас', player_money, 'монет.')
    category = input('Введите номер категории ')
    if category == '1': # выберается при выборе игроком категории 'оружие'
        print('Мифрильный меч - 100м (измняет урон с 1-20 до 21-30)')
        resp = input('Покупаете?(да - 1 или нет - 2) ')
        if resp == '1':
            player_money -= 100
            player_telum = 'Мифрильный меч'
            print('Теперь ваше оружие - это', player_telum)
            print('А так же у вас теперь', player_money, 'монет.')
            visit_shop(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor)
            if player_money < 100:
                print('Увас недостаточно денег!')
                pause()
                visit_shop(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor)
        if resp == '2': # выберается при выборе игроком категории 'защита'
            print('Очень жаль.')
            pause()
            visit_shop(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor)


    elif category == '2':
        print('Комплект мифрильной брони - 100м (изменяет сложность попадания по вам с 11 на 15)')
        resp = input('Покупаете?(да - 1 или нет -2) ')
        if resp == '1':
            player_money -= 100
            player_armor = 'мифрильная броня'
            print('Теперь ваше оружие - это', player_armor)
            print('А так же у вас теперь', player_money, 'монет.')
            pause()
            visit_shop(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor)
            if player_money < 100:
                print('Увас недостаточно денег!')
                pause()
                visit_shop(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor)
        if resp == '2':
            print('очень жаль.')
            pause()
            visit_shop(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor)

    elif category == '3':
        treatment = 10 - player_hp
        if player_hp == 10:
                print('Вы здоровы!')
                pause()
                visit_shop(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor)
        print('Я могу вылечить тебя за', treatment, 'монет.')
        resp = input('Вы хотите этого?(да - 1 или нет - 2) ')
        if resp == '1':
            player_money -= treatment
            player_hp = 10
            print('Теперь вы совершенно здоровы!')
            visit_shop(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor)
            if player_money < treatment:
                print('Увас недостаточно денег!')
                pause()
                visit_shop(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor)
        if resp == '2':
            print('Очень жаль.')
            pause()
            visit_shop(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor)

    elif category == '4':
        print('Досвидания')
        pause()
        visit_rock(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor)

    else:
        print('Введите числа 1, 2, 3, 4 или 0')
        pause()
        visit_rock(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor)

 
def fight(player_name, player_hp, player_xp, player_level, player_telum, player_armor, enemy_name,
enemy_hp, enemy_level, damage):
    print('Против', player_name, 'сражается', enemy_name)
        
    while True:

        pause()
        print('-' * 20)
        enemy_hit = randint(1, 20)
        if player_armor == 'броня':
            if enemy_hit <= 10:
                print(enemy_name, 'промахнулся!')
                print('-' * 20)
            if enemy_hit >= 11:
                enemy_attack = randint(1, 10)
                player_hp -= enemy_attack
                print(enemy_name, 'ударил', player_name, 'на', enemy_attack)
                print('У', player_name, 'стало', player_hp, 'жизней.')
                print('-' * 20)
                if player_hp <= 0:
                    print(enemy_name, 'убил', player_name, 'Игра окончена!')
                    print('-' * 20)
                    break
                        
                    
        if player_armor == 'мифрильная броня':
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
                damage = randint(1, 10)
            if player_telum == 'Мифрильный меч':
                damage = randint(10, 20)
            enemy_hp -= damage
            print(player_name, 'ударил', enemy_name, 'на', damage)
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
                    player_hp = player_xp % 10
                    print('Уровень', player_name, 'равен', player_level)
                    print('Теперь у', player_name, player_xp, 'xp')
                    print('--------------------------------------')
                    break


            


def visit_fight(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor, enemy_name,
enemy_hp, enemy_level, enemy_xp, enemy_money, enemy_telum, enemy_armor, damage):

    show_hero(player_name, player_hp, player_money, player_xp, player_level, player_telum, player_armor)
    show_hero(enemy_name, enemy_hp, enemy_level, enemy_xp, enemy_money, enemy_telum, enemy_armor)
    print('Вы на поле битвы!')
    print(f'Против {player_name} сражается {enemy_name}')
    option_vf = input('Выберете вариант: 1 - сражаться, 2 - убежать, 0 - выйти из игры.')
    if option_vf == '1':
        fight(player_name, player_hp, player_xp, player_level, player_telum, player_armor, enemy_name,
enemy_hp, enemy_level, damage)


start_game()


'''
    enemy_hit = randint(1, 20)
    if player_armor == 'обычная броня':
        if enemy_hit <= 10:
            print(enemy_name, 'промахнулся!')
            print('-' * 20)
        if enemy_hit >= 11:
            enemy_attack = randint(1, 10)
            player_hp -= enemy_attack
            print(enemy_name, 'ударил', player_name, 'на', enemy_attack)
            print('У', player_name, 'стало', player_hp, 'жизней.')
            print('-' * 20)
            if player_hp <= 0:
                print(enemy_name, 'убил', player_name, 'Игра окончена!')
                print('-' * 20)

    if player_armor == 'мифрильная броня':
        if enemy_hit <= 15:
            print(enemy_name, 'промахнулся!')
            print('-' * 20)
        if enemy_hit >= 16:
            enemy_attack = randint(1, 10)
            player_hp -= enemy_attack
            print(enemy_name, 'ударил', player_name, 'на', enemy_attack)
            print('У', player_name, 'стало', player_hp, 'жизней.')
            print('-' * 20)
            if player_hp <= 0:
                print(enemy_name, 'убил', player_name, 'Игра окончена!')
                print('-' * 20)

    player_hit = randint(1, 20)
    if player_hit <= 10:
        print(player_name, 'промахнулся!')
        print('-' * 20)
    if player_hit >= 11:
        if player_telum == 'обычный меч':
            player_attack = randint(1, 10)
        if player_telum == 'Мифрильный меч':
            player_attack = randint(10, 20)
        enemy_hp -= player_attack
        print(player_name, 'ударил', enemy_name, 'на', player_attack)
        print('У', enemy_name, 'стало', enemy_hp, 'жизней.')
        print('-' * 20)
        if enemy_hp <= 0:
            print(player_name, 'убил', enemy_name, 'бой окончен!')
            print('-' * 20)
            player_xp += enemy_level
            if player_xp >= 10:
                print('У', player_name, player_xp, 'xp')
                level_change = player_xp // 10
                player_level += level_change
                player_xp = player_xp % 10
                player_hp = player_xp % 10
                print('Уровень', player_name, 'равен', player_level)
                print('Теперь у', player_name, player_xp, 'xp')
                print('-' * 20)
'''
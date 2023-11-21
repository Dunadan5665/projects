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
    player_money = 10 # деньги игрока
    player_xp = 0 # опыт игрока
    player_level = 1 # уровень игрока
    show_hero(player_name, player_hp, player_money, player_xp, player_level)
    visit_rock(player_name, player_hp, player_money, player_xp, player_level)
    

def show_hero(name, hp, money, xp, level):
    '''
    Выводит на экран инфо о персонаже
    '''
    print('имя:', name) # выводит имя героя
    print('здоровье:', hp) # выводит здоровье героя
    print('деньги:', money) # выводит деньги героя
    print('опыт:', xp) # выводит опыт героя
    print('уровень:', level) # выводит уровень героя
    print('-' * 20)


def visit_rock(player_name, player_hp, player_money, player_xp, player_level):
    '''
    Камень: выбор дороги
    '''
    show_hero(player_name, player_hp, player_money, player_xp, player_level)
    os.system('cls') # очищает экран
    print(player_name, 'приехал к камню')
    print('1 - поехать на сражение')
    print('2 - поехать в таверну')
    print('3 - поехать заглянуть в лавку')
    print('0 - выйти из игры')
    option = input('введите номер варианта: ') # узнаёт у игрока, вариант ответа и записывает его в option
    if option == '1':
        print('Уехал на сражение') 
    elif option == '2':
        print('Уехал в таверну')
        visit_tavern(player_name, player_hp, player_money, player_xp, player_level)
    elif option == '3':
        print('Уехал в лавку')
    elif option == '0':
        print('Вышел из игры')
    else:
        visit_rock(player_name, player_hp, player_money, player_xp, player_level)


def visit_tavern(player_name, player_hp, player_money, player_xp, player_level):
    '''
    Можно играть в кости или вернуться к камню
    '''
    show_hero(player_name, player_hp, player_money, player_xp, player_level)
    os.system('cls') # очищает экран
    print(player_name, 'приехал в таверну')
    print('1 - Сыграть в кости')
    print('2 - Вернуться к камню')
    print('0 - Выйти из игры')
    option = input('введите номер варианта: ') # узнаёт у игрока, вариант ответа и записывает его в option
    if option == '1':
        play_dice(player_name, player_hp, player_money, player_xp, player_level)
    elif option == '2':
        visit_rock(player_name, player_hp, player_money, player_xp, player_level)
    elif option == '0':
        print('вышел из игры')
    else:
        visit_tavern(player_name, player_hp, player_money, player_xp, player_level)


def play_dice(player_name, player_hp, player_money, player_xp, player_level):
    os.system('cls') # очищает экран
    show_hero(player_name, player_hp, player_money, player_xp, player_level)
    bet = int(input('Введите ставку  '))
    if not player_money:
       print('У игрока НЕТ денег!')
       input('Нажмите ENTER чтобы продолжить')
       visit_tavern(player_name, player_hp, player_money, player_xp, player_level)
    elif bet < 1:
        print('ставка должна быть больше нуля!')
        input('Нажмите ENTER чтобы продолжить')
        play_dice(player_name, player_hp, player_money, player_xp, player_level)
    elif bet > player_money:
        print('У', player_name, 'нет столько денег')
        input('Нажмите ENTER чтобы продолжить')
        play_dice(player_name, player_hp, player_money, player_xp, player_level)
    
    player_score = randint(2, 12)
    tavern_score = randint(2, 12)
    print('Игрок выбросил', player_score)
    print('Трактирщик выбросил', tavern_score)
    if player_score > tavern_score:
        player_money += bet
        print(player_name, 'выйграл', bet, 'монет')
        input('Нажмите ENTER чтобы продолжить')
    elif player_score < tavern_score:
        player_money -= bet
        print(player_name, 'выйграл', bet, 'монет')
        input('Нажмите ENTER чтобы продолжить')
    else:
        print('Ничья!')

    visit_tavern(player_name, player_hp, player_money, player_xp, player_level)

start_game()
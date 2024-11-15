from random import shuffle
from os import system

'''
Карта
{
    'цена': 10,
    'масть': 'пик'
    'название': '10'
}

масти:
    черви, пики, бубны, крести

колода:
    четыре масти и на каждую масть карты от 6 до туза = 36 карт

игроки
    от 2 до ...

Перетасовать колоду

Каждому игроку даём по 2 карты

Можно смотреть только свои карты

Ход
    беру ещё одну карту (сколько угодно, не больше, чем осталось в колоде)
    или закончить ход

каждый игрок делает только один ход за партию

Если сумма цен всех карт игрока больше 21, то он проиграл

Еси все игроки проиграли, то это ничья

Победитель - тот, кто набрал большую сумму цен своих карт
'''


def get_deck() -> list[dict]:
    ''' Взврвщает колоду кард '''
    suits = ('черви', 'пики', 'бубны', 'крести')

    cards = {
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'валет': 2,
        'дама': 3,
        'король': 4,
        'туз': 11,

    }
    deck = []
    for suit in suits:
        for item in cards:
            card = {
                'цена': cards[item],
                'масть': suit,
                'название': item
            }
            deck.append(card)
    return deck


def get_players() -> list[dict]:
    ''' Создаёт игроков '''
    player_1 = {
        'имя': 'Вася',
        'карты': [],
        'человек': True,
        'сумма': 0
    }

    player_2 = {
        'имя': 'Ася',
        'карты': [],
        'человек': False,
        'сумма': 0
    }
    return [player_1, player_2]


def deal_cards(num: int) -> None:
    ''' Раздаёт игрокам карты '''
    for player in players:
        for i in range(num):
            player['карты'].append(deck.pop())


deck = get_deck()
shuffle(deck)
players = get_players()
cards_per_turn = len(deck) // len(players)
deal_cards(2)


def show_cards() -> None:
    for card in player['карты']:
        print(card['название'], card['масть'])


system('cls')
        

def get_total_values(player: dict) -> None:
    total = 0
    for card in player['карты']:
        total += card['цена']
    player['сумма'] = total


for player in players:
    while True:
        system('cls')
        show_cards()
        get_total_values(player)
        print('сумма очков:', player['сумма'])
        if player['человек']:
            player_option = input('Взять карту из колоды (y/n)? ')
        if player_option.lower() == 'y':
            if cards_per_turn > len(player['карты']):
                player['карты'].append(deck.pop())
            else:
                print('Невозмижно взять ещё карту!')
                break
        else:
            break
    input('ENTER - следующий игрок')


system('cls')

players_total_value = [player['сумма'] for player in players if player['сумма'] < 22]

if players_total_value:
    max_value = max(players_total_value)

for player in players:
    print(player['сумма'], player['имя'])

    if player['сумма'] > 21:
        print('У игрока', player['имя'], 'перебор!')

    elif player['сумма'] == max_value:
        print('Игрок', player['имя'], 'победил!')

    else:
        print(player['имя'], player['сумма'])
    

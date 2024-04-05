'''
Уровень и опыт
Награды в бою
Деньги игрока
Зелья
Инвентарь (возможно ограниченный)
Магазин
'''


class Weapon:
    ''' Оружие '''
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power
    def __str__(self) -> str:
        return self.name


class Player:  # определяем класс
    '''Игрок'''
    def __init__(self, name: str, hp: int, weapon=None) -> None:
        '''
        Конструктор класса
        Вызывается автоматически сразу после создания экземпляра
        self - ссылка на экземпляр
        Все атрибуты определяются в конструкторе (в __init__)!
        '''
        self.name = name  # Атрибут
        self.hp = hp  # Атрибут
        self.weapon_defold = Weapon('Кулаки', 1)
        if weapon:
            self.weapon = weapon
        else:
            self.weapon = self.weapon_defold
        self.power = 1

    def __str__(self) -> str:
        return f'Игрок: {self.name}, Жизни: {self.hp}, оружие: {self.weapon}'

    def attack(self, enemy):
        ''' Игрок атакует противника '''
        if self.hp <= 0:
            return
        damage = self.weapon.power + self.power
        enemy.hp -= damage
        print(self.name, 'атаковал', enemy.name)


class Game:
    ''' Игра '''
    def __init__(self) -> None:
        self.player = Player('Вася', 100, Weapon('Бластер', 100))
        self.enemy = Player('Упырь', 99)
        self.is_fighting = False
        self.fight()

    def fight(self) -> None:
        ''' Бой - обмен ударами '''
        self.is_fighting = True
        while self.is_fighting:
            self.player.attack(self.enemy)
            print(self.player)
            self.enemy.attack(self.player)
            print(self.enemy)
            self.check_winner()

    def check_winner(self) -> None:
        if self.player.hp <= 0:
            print(self.enemy.name, 'победил')
            self.is_fighting = False
        elif self.enemy.hp <= 0:
            print(self.player.name, 'победил')
            self.is_fighting = False


Game()

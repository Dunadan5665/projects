'''
ООП - стиль программирования
Класс - идея объекта, фабрика экземпляров
Экземпляр - конкретная реализация объекта
Переменные и функции внутри класс - атрибуты и методы
'''


class Player:  # определяем класс
    '''Игрок'''
    def __init__(self, name: str, hp: int) -> None:
        '''
        Конструктор класса
        Вызывается автоматически сразу после создания экземпляра
        self - ссылка на экземпляр
        Все атрибуты определяются в конструкторе (в __init__)!
        '''
        self.name = name  # Атрибут
        self.hp = hp  # Атрибут
        self.power = 1

    def __str__(self) -> str:
        return f'Игрок: {self.name}, Жизни: {self.hp}'

    def attack(self, enemy):
        enemy.hp -= self.power
        print(self.name, 'атаковал', enemy.name)


class Game:
    def __init__(self) -> None:
        self.player = Player('Вася', 100)
        self.enemy = Player('Упырь', 100)
        self.fight()

    def fight(self) -> None:
        while True:
            self.player.attack(self.enemy)
            print(self.player)
            self.player.attack(self.player)
            print(self.enemy)
            # TODO: завершить бой и определить победителя


Game()

import tkinter as tk
from random import randint


class Game:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.combat_messanges = tk.Listbox(self.window)

        self.player_stats = tk.Listbox(self.window)
        self.player_stats.insert(0, 'ИГРОК')
        self.player_stats.insert(tk.END, 'имя: Вася')
        self.player_stats.insert(tk.END, 'HP: 100')
        self.player_stats.insert(tk.END, 'деньги: 10')
        self.player_stats.insert(tk.END, 'XP: 0')
        self.player_stats.insert(tk.END, 'LEVEL: 1')
        self.player_stats.pack(side='left')
        self.player_hp = 100

        self.start()

        self.window.mainloop()

    def buttons_actions(self):
        self.button_combat = tk.Button(
            text='Идти на сражение',
            command=lambda: self.combat()
            ).pack()
        self.button_shop = tk.Button(
            text='Идти в магазин',
            command=lambda: print('в магазине')
            ).pack()
        self.button_dice = tk.Button(
            text='Идти играть в кости',
            command=lambda: print('играет')
            ).pack()

    def combat(self):
        enemy_stats = tk.Listbox(self.window)
        enemy_stats.insert(0, 'ПРОТИВНИК')
        enemy_stats.insert(tk.END, 'имя: Гоблин')
        enemy_stats.insert(tk.END, 'HP: 100')
        enemy_stats.insert(tk.END, 'LEVEL: 2')
        enemy_stats.insert(tk.END, 'Даст опыта: 10')
        enemy_stats.pack(side='right')
        enemy_hp = 100

        self.combat_messanges.insert(0, 'СРАЖЕНИЕ!')
        while self.player_hp > 0 or enemy_hp > 0:
            button_attack = tk.Button(master=self.window, text='Атаковать', command=self.attack())

        self.combat_messanges.pack()

    def attack(self)

    def print_hero(self):
        pass

    def start(self):
        tk.Label(master=self.window, text='Инфо об игроке выведено слева').pack()
        tk.Label(master=self.window, text='Выберете один из вариантов, куда можно пойти').pack()
        self.buttons_actions()


'''
tk.Button(self.window, text='OK', command=self.print_selected).pack()
    def print_selected(self) -> None:
        if self.combat_messanges.curselection():
            print(self.combat_messanges.selection_get())
'''

Game()

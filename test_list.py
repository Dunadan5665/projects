inventory = []
money = 100

while True:
    print('1 - Купить зелье лечения за 10')
    print('2 - Купить зелье копчения за 20')
    print('3 - Продать предмет')
    print(f'деньги = {money}')

    option = input('Введите номер опции: ')

    if option == '1':
        money -= 10
        inventory.append('зелье лечения')
        print(inventory)

    elif option == '2':
        money -= 20
        inventory.append('зелье копчения')
        print(inventory)

    elif option == '3':
        print('Что вы хотите продать?')
        ix = 0
        for item in inventory:
            print(ix, item)
            ix += 1
        option = input('Введите номер предмета для продажи: ')
        # проверить вменяемость опции
        inventory.pop(option)

    else:
        print('неверная опция')
        continue
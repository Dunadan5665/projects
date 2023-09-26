name = 'Илья Муромец'

way_1 = False
way_2 = False
way_3 = False

while way_1 == False or way_2 == False or way_3 == False:

    print(name, 'приехал к камню, на камне написанно:')
    print('налево поедешь - убит будешь,')
    print('прямо поедешь - женат будешь,')
    print('направо поедешь - богат будешь,')

    way = input('Куда ехать? ')


    if way == 'налево':
        if way_1 == False:
            print(name, 'Убит!')
            way_1 = True
        else:
            print(name, 'уже ездил туда!')
        
    elif way == 'прямо':
        if way_2 == False:
            print(name, 'Женат!')
            way_2 = True
        else:
            print(name, 'уже ездил туда!')
    
    elif way == 'направо':
        if way_3 == False:
            print(name, 'Богат!')
            way_3 = True
        else:
            print(name, 'уже ездил туда!')

    else:
        print('Нет такой дороги')
              
    if way_1 == True:
        print('прямо поедешь - женат будешь,')
        print('направо поедешь - богат будешь,')
    

print('Сказке конец.')

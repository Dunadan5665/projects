i = 0
while i < 102:
    i += 1

    if i % 3 == 0 and i % 5 == 0:
        print('физбаз')
    
    elif i % 3 == 0:
        print('физ')

    elif i % 5 == 0:
        print('баз')

    else:
        print(i)

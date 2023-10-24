rows = int(input('Введите число '))
current_row = 1

while current_row <= rows:
    print(int((current_row + 1)  * '1'))
    #print('1' * current_row)
    current_row += 1

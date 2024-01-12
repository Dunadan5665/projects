

def check_password(password):
    # проверяем длину
    if len(password) > 9:
        # создаём переменные
        is_upper = False
        is_lower = False
        is_digit = False
        # проверяем каждый символ
        for char in password:
            if char.islower():
                is_lower = True
            elif char.isupper():
                is_upper = True
            elif char.isdigit():
                is_digit = True
            # Проверяем, что условия выполнены
            if is_lower and is_upper and is_digit:
                return True
    return False


print(check_password('Abc1234567'))
print(check_password('..........'))
print(check_password('abc1234567'))
print(check_password('Abcdefghjk'))
print(check_password('Abcdefgh'))
print(check_password('1234567890'))
print(check_password('Afbv837n5f'))

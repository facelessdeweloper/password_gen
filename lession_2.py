# Импорт модуля random
import random

# Создаем функцию для генерации пароля
def generate_password(length):
    digits = '1234567890'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    symbols = '!@#$%^&*()-+'

    password = ''
    var = [digits, uppercase_letters, lowercase_letters, symbols]

    # Генерация пароля
    if length < 12:
        print('Ошибка! Пароль должен иметь не менее 12 символов')
    else:
        password += random.choice(digits)
        password += random.choice(uppercase_letters)
        password += random.choice(lowercase_letters)
        password += random.choice(symbols)

        while len(password) < length:
            password += random.choice(var[random.randint(0, 3)])

        print(password)

# Пример вызова функции с длиной пароля 12
generate_password(12)

def generate_nicknames():
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    nick = int(input('Длинна никнейма?'))
    log = (random.choice(uppercase_letters))
    for i in range(nick - 1):
        log += random.choice(lowercase_letters)
    print(log)
generate_nicknames()


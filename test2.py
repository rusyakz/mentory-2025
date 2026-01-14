from test import start


def count_letters(text: str, value: str | int) -> int:
    counter = 0
    if type(value) == int:
        value = str(value)
    for latter in text:
        if latter == value:
            counter += 1
    return counter


def main(text: str, number: int | str, latter: str) -> str:
    num_counter = count_letters(text, number)
    latter_counter = count_letters(text.lower(), latter.lower())
    result = f"Количество цифр {number}: {num_counter}\n"
    result += f"Количество букв {latter}: {latter_counter}"
    return result


# text_input = input('Введите текст: ')
# num_search = input('Какую цифру ищем? ')
# latter_search = input('Какую букву ищем? ')
# result = main(text_input, num_search, latter_search)
# print(result)


import random


def rock_paper_scissors() -> str:
    '''Здесь будет игра «Камень, ножницы, бумага»'''
    player_score = 0
    computer_score = 0
    print('\nКамень, ножницы, бумага. Для выхода из игры отправьте слово ВЫХОД')
    while True:
        value = input('Введите слово камень, ножницы, либо бумага: ').lower().strip()
        possible_value = [['камень', 'ножницы', 'бумага'], 'выход']
        prog_choice = random.choice(possible_value)
        result = ''
        if value not in possible_value:
            result = "Нет такого выбора"
        elif value == possible_value[1]:
            break
        elif value == prog_choice:
            result = f'Мы оба выбрали {value}. Счет {player_score}:{computer_score}'
        elif prog_choice == possible_value[0][0] and value == possible_value[1]:
            computer_score += 1
            result = f'Камень бьёт ножницы. Вы проиграли. Счет {player_score}:{computer_score}'
        elif prog_choice == possible_value[0][1] and value == possible_value[2]:
            computer_score += 1
            result = f'Ножницы режут бумагу. Вы проиграли. Счет {player_score}:{computer_score}'
        elif prog_choice == possible_value[0][2] and value == possible_value[0]:
            computer_score += 1
            result = f'Бумага кроет камень. Вы проиграли. Счет {player_score}:{computer_score}'
        elif prog_choice == possible_value[0][1] and value == possible_value[0]:
            player_score += 1
            result = f'Камень бьёт ножницы. Вы выиграли. Счет {player_score}:{computer_score}'
        elif prog_choice == possible_value[0][2] and value == possible_value[1]:
            player_score += 1
            result = f'Ножницы режут бумагу. Вы проиграли. Счет {player_score}:{computer_score}'
        else:
            player_score += 1
            result = f'Бумага кроет камень. Вы проиграли. Счет {player_score}:{computer_score}'
        print(result + '\n')
    return f'\nИгра завершена.\nСчет {player_score}:{computer_score}'


def guess_the_number(start: int = 1, end: int = 10) -> str:
    '''игра «Угадай число»'''
    print('\nДля выхода из игры отправь слово ВЫХОД\n')
    while True:
        result = ''
        counter = 0
        prog_choice = random.randint(start, end)
        welcome_text = f"Я загадал число от {start} до {end}: "
        value = input(welcome_text)
        while not value:
            value = input('Попробуйте ещё. Для выхода отправьте слово ВЫХОД')
        while value:
            if type(value) == str and value.isalpha():
                if value.lower() == 'выход':
                    break
                else:
                    value = input('Нет такой команды, попробуйте ещё. ')
            elif int(value) == prog_choice:
                counter += 1
                result = f"\n{'Конец игры':*^45}\nВы угадали загаданное число {prog_choice} с {counter} попытки\n"
                break
            else:
                text = f"Загаданное число не {value}, попробуйте ещё раз. "
                counter += 1
                value = input(text)
                if not value:  ## Что бы игра не останавливалсь, если была отправлена пустая строка
                    value = 1  ##
        return result


def main_menu():
    while True:
        welcome_text = (f"\n{'-_' * 25}\n{'Главное меню':*^50}\n\nДля выбора игры отправьте:"
                        "\n1 - Камень, ножницы, бумага\n2 - Угадай число\n\nВаш выбор? ")
        choice_game = int(input(welcome_text))
        if choice_game == 1:
            print(rock_paper_scissors())
        elif choice_game == 2:
            while True:
                start_value = input("Что бы я загадал число, введи начальное значение или пропусти: ")
                if start_value.isalpha() and start_value.lower() == 'выход':
                    break
                end_value = input("Что бы я загадал число, введи последнее значение или пропусти: ")
                if end_value.isalpha() and end_value.lower() == 'выход':
                    break

                start_value = int(start_value) if start_value.isdigit() else 1
                end_value = int(end_value) if end_value.isdigit() else 10

                if start_value > end_value:
                    print("Стартовое значение не может быть больше последнего. Попробуй еще раз")
                    continue

                print(guess_the_number(start_value, end_value))
                break
        else:
            print('Такой игры нет')


# main_menu()


download_size = 123
download_speed = 0

if download_size <= 0 or download_speed <= 0:
    print('Размер обновления и скорость соединения не могут быть меньше нуля.')
else:
    iter_count_sek = int(download_size / download_speed + 1)

    for size in range(1, iter_count_sek + 1):
        downloaded_size = size * download_speed
        if downloaded_size > download_size:
            downloaded_size = download_size
        print(
            f"Прошло {size} сек. Скачано {downloaded_size} из {download_size} - {round(downloaded_size / download_size * 100)} %")

aa = -1.2

import math

print(math.floor(aa))

MATH = '''
1. Имя
2. Город
'''

print(MATH)


def max_devider(num1, num2):
    min_num = min(num1, num2)
    for i in range(min_num, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i
    return 1


print(max_devider(30, 18))
print()

num = 4.5e-99999
num2 = 4.5e-999999999

print(num)
print(num2)
print(id(num), id(num2))

# x = 1
# num = float(input('Число: '))
# # print(num)
# count = 0
# while x < 2:
#     x += num
#     count += 1
#     # print(x)
# print(count)


#
# num9 = int(input('Введи число: '))
# num8 = num9
# mantissa = 0
#
# while num8 >= 10:
#     num8 //= 10
#     mantissa += 1
# print(f"{num9 * 10 ** (-mantissa)}")
# print(mantissa)
#

print()

n = 1e-14
m = 1e-14
l = 2e-14

print(n + m == l)

if n + m - l > 1e-14:
    print('Равно')

result = 2 ** 3 ** 4
print(result)


def delitel(a: int, b: int) -> int:
    ''' Нахождение максимума из двух чисел '''
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


print(delitel(10, 20))



def maximum_of_two(a: int, b: int):
    ''' Нахождение максимума из двух чисел '''
    return abs(a - b) + ((a +b ) / 4)




print()
#
# start = 1
# end = 100
#
# n = (start + end) // 2
#
# while True:
#     print('Твое число равно, больше или меньше числа', n)
#     answer = int(input('Ответ 1 - равно, 2 - меньше, 3 - больше: '))
#     if answer == 1:
#         print('Угадал!')
#         break
#     elif answer == 2:
#         end = n - 1
#     else:  # answer == 3
#         start = n + 1
#     n = (start + end) // 2















# Функция для вычисления среднего значения глубины и уровня опасности на этой глубине
def danger(d_min, d_max):
    # Вычисляем среднее значение между минимальной и максимальной глубинами
    d_middle = (d_min + d_max) / 2
    # Вычисляем уровень опасности по заданной формуле, используя среднее значение глубины
    middle_danger = d_middle ** 3 - 3 * d_middle ** 2 - 12 * d_middle + 10
    # Возвращаем среднее значение глубины и рассчитанный уровень опасности
    return d_middle, middle_danger

# Основная функция для поиска безопасной глубины
def depth_calculation(user_danger_level):
    # Задаём начальные границы глубины: от 0 до 4 метров
    lower_bound = 0
    upper_bound = 4

    # Запускаем бесконечный цикл, который будет завершён при достижении нужного уровня опасности
    while True:
        # Вычисляем среднюю глубину и уровень опасности на этой глубине
        mid, danger_level = danger(lower_bound, upper_bound)

        # Если уровень опасности больше 0, значит, глубина слишком мала — изменяем нижнюю границу
        if danger_level > 0:
            lower_bound = mid
        # Иначе уровень опасности меньше или равен 0, значит, глубина слишком велика — изменяем верхнюю границу
        else:
            upper_bound = mid

        # Проверяем, достигнут ли допустимый уровень опасности (модуль разницы меньше допустимого значения)
        if abs(danger_level) < user_danger_level:
            # Если да, возвращаем найденную глубину
            return mid

# Запрашиваем у пользователя максимально допустимый уровень опасности
max_danger = float(input("Введите максимально допустимый уровень опасности: "))

# Выполняем расчёт безопасной глубины
result = depth_calculation(max_danger)

# Выводим результат — глубину, на которой уровень опасности минимален и безопасен
print("Приблизительная глубина безопасной кладки: ", result)


print()
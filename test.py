# summ = 0
# number = int(input('Введите число: '))
# while number != 0:
#     summ += number
#     number = int(input('Введите число: '))
# print(summ)


# number = 0
#
# while number < 98:
#     number += 7
#     print(number, end=' ')
# print()


# temp = int(input('Enter a temperature: '))
# distance = 0
#
# while temp > 15:
#     distance += temp
#     temp -= 2
#     if temp < 15:
#         break
#     distance += 10
#
# print(distance)



# number = int(input('Enter a number: '))
# summ = 0
#
# while number:
#     last_num = number % 10
#     if last_num == 5:
#         breaka
#     summ += last_num
#     number //= 10
# print(summ)


# book_quantity = int(input('Enter book quantity: '))
# damaged_book = 0
#
# while book_quantity > 0 and damaged_book < 5:
#     print('Book quantity:', book_quantity)
#     checked_book_quantity = int(input('Enter checked book quantity: '))
#     book_quantity -= checked_book_quantity
#     damaged_book_quantity = int(input('Enter damaged book quantity: '))
#     damaged_book += damaged_book_quantity
# print('Today end')
# if damaged_book >= 5:
#     print('You won!')
# else:
#     print('You lost!')



# money_quantity = int(input('How much money do you have?: '))
#
# while money_quantity < 10000:
#     qubik = int(input('How qubik?: '))
#     if qubik == 3:
#         money_quantity = 0
#         print('Вы проиграли')
#         break
#     money_quantity += 500
#
# print(money_quantity)


# count = 10
# while count + 1:
#     print(count)
#     count -= 1
# print('Время вышло!')


# while True:
#     input_word = int(input('Enter a number 1/0: '))
#     print(input_word)
#     if not input_word:
#         print('End')
#         break

# while True:
#     print('Верни скейт, тогда скажу пароль')
#     psw = int(input('Введите пароль'))
#     if psw == 10101:
#         print('Паоль подошел')
#         break


# number = int(input('Введите число: '))
# start_step = 0
#
# while number:
#     start_step += 1
#     print(start_step, '** 3 =', start_step ** 3)
#     number -= 1



# quantity = int(input('Enter a number: '))
#
# while quantity:
#     print('Я — программист!')
#     quantity -= 1



# print('Программа для отслеживания температуры')
# counter = 0
# stop_prog = True
# last_data = -9999
#
# while stop_prog:
#     iter_temp = int(input('Какая температура на датчике? '))
#     if iter_temp == last_data:
#         counter += 1
#         print('Внимание: дублирующее значение температуры', last_data)
#         print('Зафиксировано сбоев датчика:', counter)
#         stop_prog = bool(input('Хотите продолжить сбор данных? 1 — да, 0 — нет: 0 '))
#     last_data = iter_temp
#
# print(counter)



# deposit = int(input('Вклад в банке: '))
# percent = int(input('Проценты: '))
# threshold = int(input('Порог вклада: '))
# years_count = 0
#
# while deposit < threshold:
#   profit = int(deposit * percent / 100)
#   years_count += 1
#   print(f"{years_count} год. {deposit} + {percent}% = {deposit + profit}")
#   deposit += profit
# print('Кол-во лет для достижения порога:', years_count)




# low = 1
# high = 100
#
# print('Угадай число. 1 равно, 2 больше, 3 меньше')
#
# while low <= high:
#     mid = (low + high) // 2
#     answer = int(input(f"Ваше число {mid}: "))
#     if answer == 1:
#         break
#     elif answer == 2:
#         low = mid + 1
#     else:
#         high = mid - 1


nums = 3, 7, 5, 6, 4
degs = 2, 3, 4

for num in nums:
    for deg in degs:
        print(num ** deg, end=' ')
    print()
print()



tickets = 345, 19, 87, 1020, 421, 125

for ticket in tickets:
    if (10 > ticket // 100 >= 1) and (ticket % 5 == 0):
        print(ticket, end=' ')





print()

res = 0
for i in range(5, 11):
    print(i, end=' ')
    res += i


print(res)


import time


def is_prime(value):
    for i in range(2, int(value ** .5) + 1):
        if value % i == 0:
            return False
    return True

def check_prime(*args):
    result = []
    for arg in args:
        if is_prime(arg):
            result.append(arg)
    return result



print('***********************')

boys = 10
girls = 5

res = ''

if boys > 2 * girls or girls > 2 * boys:
    print('Нет решения')
elif boys >= girls:
    k = boys - girls
    for bgb in range(k):
        res += 'BGB '
    for bg in range(girls - k):
        res += 'BG '
else:
    k = girls - boys
    for gbg in range(k):
        res += 'GBG '
    for GB in range(boys - k):
        res += 'GB '
print(res)



# name = input('Как тебя зову? ')
# print(name + ', купи слона!')
# # answer = ''
# while True:
#     answer = input('')
#     print('Все говорят ' + answer + ', купи слона')


for i in 'Rustem':
    print(i * 3)


print('Rustem', 'gsgsd', sep='')


n = 5
res = ''

for i in range(n):
    if i == 0:
        res += '----------'
    elif i < n - 1:
        print('|OOOOOOOO|')
    else:
        print('----------')



na = 1.6887
print(f"{na:.2f}")

n = 50
print('-=-', end=' ')
for i in range(0, n + 1, 10):
    print(i, end=' -=- ')

print()
a = ['f', 2, 3, 4, 'fg', 6, 7, 8, 9, 10]
for i, e in enumerate(a, start=1):
    print(i, e)



dd = 'dfg'

for i in dd:
    print(dd.index(i))




boys = 10
girls = 5

res = ''

if boys > girls * 2 or girls > boys * 2:
    pass
elif boys >= girls:
    k = boys - girls
    for bgb in range(k):
        res += 'BGB '
    for bg in range(girls - k):
        res += 'BG '

print(res)



word = 'RuR'

res = ''

for i in word:
    res = i + res

print(res == word)



word = 'shacnidw'
fist_word = ''
second_word = ''
count = 1

for letter in word:
    if count % 2 != 0:
        fist_word += letter
    else:
        second_word = letter + second_word
    count += 1
print(fist_word + second_word)


odd_letters = ''
even_letters = ''
count = 1
for letter in word:
    if count % 2 != 0:
        odd_letters += letter
    else:
        even_letters = letter + even_letters
    count += 1
print('Расшифрованное слово: ', odd_letters + even_letters)



# count = 1
# for i in range(6):
#     for j in range(-1, 5):
#         print((j + count) * 2, end='\t')
#     count += 1
#     print()

n = 10 # int(input('Введите число для высоты таблицы: '))
count = 0
line = ''
for i in range(n):
    for j in range(n):
        # print(j + count, end='\t')
        line += str(j + count) + '\t'
        count += 1
    # print(line)
    line += '\n'
    count -= n - 1
print(line)


n = 5 # int(input('Введите число для высоты елки: '))
for i in range(1, n + 1):
    for j in range(i):
        print(i, end='\t')
    print()



height = 6 # int(input('Введите высоту: '))
width = 6 # int(input('Введите ширину: '))

print('|' + '-' * (width - 2) + '|')
for i in range(height - 2):
    print('|' + ' ' * (width - 2) + '|')
print('|' + '-' * (width - 2) + '|')



height = 6 # int(input('Введите высоту: '))
width = 6 # int(input('Введите ширину: '))
result = ''

for i in range(height):
    if i == 0 or i == height - 1:
        result += '|' + '-' * (width - 2) + '|\n'
    else:
        result += '|' + ' ' * (width - 2) + '|\n'
print(result)


# n = 6
# counter = 0
#
# for _ in range(n):
#     num = int(input('Введите число: '))
#     for i in range(2, num ** .5 + 1):
#
#
# print('Количество простых чисел в последовательности:', counter)



# n = 19
# flag = False
#
# for i in range(2, int(n ** 0.5) + 1):
#     for j in range(2, i + 1):
#         if n % j == 0:
#             flag = True
#             break
# if not flag:
#     print(n)



# numbers_quantity = int(input('ведите количество чисел: '))
# counter = 0
# for _ in range(numbers_quantity):
#     n = int(input('Введите число: '))
#     flag = False
#
#     for i in range(2, int(n ** 0.5) + 1):
#         for j in range(2, i + 1):
#             if n % j == 0:
#                 flag = True
#                 break
#     if not flag:
#         counter += 1
# print('Количество простых чисел в последовательности:', counter)



# max_value = 0
# max_num = 0
#
# num_quantity = int(input('Введите количество чисел: '))
# for _ in range(num_quantity):
#     n = int(input('Введите число: '))
#     temp = 0
#     for i in str(n):
#         temp += int(i)
#     if temp > max_value:
#         max_value = temp
#         max_num = n
#
# print(f"Число {max_num} имеет максимальную сумму цифр: {max_value}")



# n = int(input('Введите высоту пирамиды: '))
# result = ''
#
# for i in range(1, n * 2, 2):
#     for k in range(n * 2, i, -2):
#         result += ' '
#     for j in range(i):
#         result += '#'
#     result += '\n'
# print(result)



    #
   ###
  #####
 #######
#########




n = 6
k = 0

for i in range(n):
    for j in range(n):
        print(j + k, end='\t')
        k += 1
    print()
    k -= n - 1


print()

n = 5

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end='\t')
    print()

print()

n = -10

for i in range(n, 0,):
    for j in range(n, 0):
        print(i - j, end='\t')
    print()

print()

n = 5


for row in range(1, n + 1):
    for col in range(1, n):
        if row % 2 == 0:
            print(row, end='\t')
        else:
            print(col + row, end='\t')
    # k += 1
    print()



rows  = 50
cols = 50

for row in range(rows):
    for col in range(cols):
        if row == rows // 2:
            print('-', end=' ')
        elif col == cols // 2:
            print('|', end=' ')
        else:
            print(' ', end='')
    print()


n = 5

for row in range(1, n + 1):
    for col in range(1, n + 1):
        if row % 2 == 0:
            print(row, end='\t')
        else:
            print(col, end='\t')
    print()


print()

rows = 6
cols = 6

for row in range(1, rows):
    for col in range(1, cols):
        if col == 3:
            print(col, end='\t')
        else:
            print(row, end='\t')
    print()

print()

for row in range(1, rows + 1):
    for col in range(1, cols + 1):
        if col == 3:
            print(col, end='\t')
        elif col == 6:
            print(col, end='\t')
        else:
            print(row, end='\t')
    print()


rows = 6
cols = 6
res = []

for row in range(1, rows + 1):
    temp = []
    for col in range(1, cols + 1):
        temp.append(row * col)
    res.append(temp)
print(res)



print()

n = 20

for row in range(0, n):
    for col in range(0, n):
        if col > row:
            print(0, end='\t')
        elif row > col:
            print(2, end='\t')
        else:
            print(1, end='\t')
    print()


print()

rows = 20
cols = 50


for row in range(0, rows):
    for col in range(0, cols):
        if row == 9:
            print('-', end='')
        elif col == row + 35:
            print('\\', end='')
        elif col == -row + 15:
            print('/', end='')
        elif col == 25:
            print('|', end='')
        else:
            print(' ', end='')
    print()


print()

rows = 10
cols = 40

for row in range(0, rows):
    for col in range(0, cols):
        if row == 0 or row == rows - 1:
            print('-', end='')
        elif (col == 0) or (col == cols - 1):
            print('|', end='')
        else:
            print(' ', end='')
    print()


n = 6

for row in range(n):
    for col in range(n):
        if col > row:
            print(0, end='\t')
        elif row > col:
            print(2, end='\t')
        else:
            print(1, end='\t')
    print()


print()

# human_count = int(input("Введите количество людей в очередь: "))
# for human_start in range(human_count + 1):
#     print("Час:", human_start)
#     for human_number in range(human_start, human_count):
#         print(human_number, end='\t')
#     print()


print()

# n = 4
# count = 0
#
# for _ in range(n):
#     num = int(input())
#     if num > 5 == 0:
#         count += 1
#
# print()


# n = 5 # Количнство
# counter = 0
#
# for _ in range(n):
#     new_num = int(input('Введи число: '))
#
#     while new_num:
#         if new_num % 10 > 5:
#             counter += 1
#             print('============')
#         new_num = new_num // 10
# print(counter)


n = 5

for start in range(1, n + 1):
    for number in range(start, n + 1):
        print(number, end='\t')
    print()


n = 5

for human in range(n + 1):
    print('Час', human)
    for number in range(human, n):
        print(number, end='\t')
    print()
print('Очередь обслужена')



# n = 5
# counter = 0
# for _ in range(n):
#     new_num = int(input('Число: '))
#     while new_num:
#         if new_num % 10 == 1:
#             counter += 1
#         new_num //= 10
# print(counter)




# attempt = 3
# pin = 8446
#
# while attempt:
#     pin_input = int(input('Введите ПИН код: '))
#     if pin_input != pin:
#         attempt -= 1
#         if not attempt:
#             print('Попытки закончились, заберите вашу карту')
#             break
#         print('Не верный пинкод. Осталось попыток', attempt)
#     else:
#         print('Пинкод верный. Держите вашу зарплату')
#         break

from functools import wraps

def decor(value):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal value
            res = func(*args, **kwargs)
            if value:
                print('start')
                value -= 1
            else:
                print('поптокнет')
            return res
        return wrapper
    return decorator



def test():
    '''Описание функции'''
    return True

test = decor(2)(test)

test()
test()
test()



# print(test.__doc__)
#
# a = []
#
# print(a.__dir__())




rows = 8
new_num = 1


for line in range(rows):
    space_count = rows - line - 1
    print('   ' * space_count, end='')
    for number in range(line + 1):
        print(new_num, end='    ')
        new_num += 2
    print()


print()

depth = 10
for line in range(depth):
    for left_number in range(depth, depth - line - 1, - 1):
        print(left_number, end=' ')
    # dots = (depth - line - 1) * 2
    # print('.' * dots, end='')
    for dot in range(line, depth - 1):
        print('.', '.', end=' ')
    for right_number in range(depth-line, depth + 1):
        print(right_number, end=' ')
    print()

print(int(2e100))

print()

# chatls = int(input('Сколько чатлов? '))
# cr_money = chatls / 2200
# print('Это', cr_money, 'CR')
# buy_ship = int(cr_money / .5)
# print('Можно купить кораблей:', buy_ship)


import math

a = math.acos(0)
print(a)

a = 6.486565
print(math.sqrt(9))
print(a)



def summ(value: int) -> int:
    result = 0
    while value:
        result += value % 10
        value //= 10
        continue
    return result

print(summ(9999))


def max_number(value: int) -> int:
    max_num = 0
    while value:
        number = value % 10
        if number > max_num:
            max_num = number
        value //= 10
        continue
    return max_num

print(max_number(35813))

def min_number(value: int) -> int:
    min_num = 9
    while value:
        number = value % 10
        if number < min_num:
            min_num = number
        value //= 10
        continue
    return min_num

print(min_number(3581))

print('Введите номер действия: \n1 - сумма цифр \n'
      '2 - максимальная цифра \n3 - минимальная цифра')




# Давыдова Лидия Викторовна
#  Python 225
# Задание №"1

# import random as r

# a = 1
# b = 2
# a = a + b
# b = a - b
# a = a - b
# print("a:", a)
# print("b:", b)
#
# a = 1
# b = 2
# a, b = b, a
# print("a:", a)
# print("b:", b)
#
# # Задание №"2
#
# a = 9
# b = 6
# c = 7
# d = 5
# r1 = a + b
# r2 = c + d
# print(r1 / r2)
#
# # a = int(input("Введите число:"))
# # print(type(a))
# # print(a + 6)
# # a = int(input("Введите число:"))
# # print(type(a))
# # print(a + 5)
# # a = int(input("Введите число:"))
# # print(type(a))
# # print(a / 12 )
#
#
# #  Задание №3
#
# a = int(input())
# b = (a // 10000) * ((a // 1000) % 10) * ((a // 100) % 10) * ((a // 10) % 10) * (a % 10)
# c = (a // 10000) * (a % 10) / 18
# print(str(b))
# print(str(c))
#
# # x = str(input())
# # A = 0
# # for i in x:
# #     A *= int(i)
# # print(a)
# # C = 0
# # for i in x:
# #     c += int(i)
# # print(c/len(x))
#
# # Задание 4
#
#
# n = int(input("Введите число от 1 до 99: "))
# if 1 <= n <= 99:
#
#     if 11 <= n <= 14:
#         print(n, "копеек")
#     else:
#         a = (n % 10)
#         if a == 1:
#             print(n, "копейка")
#         if 2 <= a <= 4:
#             print(n, "копейки")
#         if 5 <= a <= 9 or a == 0:
#             print(n, "копеек")
#
# else:
#     print("Ошибка")
#
# # другой вариант
# n = int(input("Введите число копеек:"))
# if 0 <= n <= 99:
#     if n <= 1 or n % 10 == 1 and n != 11:
#         print(n, "копейка")
#     elif 2 <= n <= 4 or 2 <= n % 10 <= 4 \
#             and n != 12 and n != 13 and n != 14:
#         print(n, "копейки")
#     # if 5 <= n <= 9:
#     #     print(n, "копеек")
#     else:
#         print(n, "копеек")
# else:
#     print("Ошибка")
#
# #  Задание 5
#
# user = input('1. "r"' '\n2. "+"'
#              '\n3. "-"' '\n4. "/"' '\n5. "*"'
#              '\n6. "%"' '\n7. "<"' '\n8. ">"'
#              "\nВведите знак: ")
# if user == 'r':
#     try:
#         operator = int(input("Введите цифру:"))
#         f_num = int(input("Введите первое число:"))
#         s_num = int(input("Введите второе число:"))
#         if operator == 2:
#             print(f_num + s_num)
#         if operator == 3:
#             print(f_num - s_num)
#         if operator == 4:
#             if s_num != 0:
#                 print(f_num / s_num)
#             else:
#                 print("На 0 делить нельзя")
#         if operator == 5:
#             print(f_num * s_num)
#         if operator == 6:
#             print(f_num % s_num)
#         if operator == 7:
#             print(f_num < s_num)
#         if operator == 8:
#             print(f_num < s_num)
#         f_num = -f_num
#         s_num = -s_num
#     except ValueError:
#         print("ввели не правильно")
# else:
#     print("Вы вели не верный знак")
#
# # operation = input('1)"r" - применяет унарный минус к операнду '
# #                   '\n2)"+" - сложение'
# #                   '\n3)"-" - вычитание'
# #                   '\n4)"/" - деление'
# #                   '\n5)"*" - умножение'
# #                   '\n6)"%" - деление по модулю (остаток то деление'
# #                   '\n7)"<" - минимальное из двух чисел'
# #                   '\n8)">" - максимальное из двух чисел'
# #                   '\nВведите знак:')
#
# #  Задание 6
#
# # from random import randint
# #
# # rnd = randint(1, 100)
# # print(rnd)
# # user_num = 0
# # while user_num < 10:
# #     user_num2 = int(input("Введите число от 1 до 100: "))
# #     user_num += 1
# #     if user_num2 == rnd:
# #         print("Вы угадали загаданное число c", user_num, end="-ой попытки")
# #         break
# #     if user_num2 <= rnd:
# #         print("Загаданное число больше!")
# #     if user_num2 >= rnd:
# #         print("Загаданное число меньше!")
# #     if user_num2 != rnd and user_num == 10:
# #         print("много было попыток, загаданное число:", rnd)
# #     if user_num2 == 0:
# #         print("прекратили пытаться, загаданное число:", rnd)
# #         break
#
# #  другой вариант
# # n = 12
# # i = 0
# # while True:
# #     a = int(input("Введите число:"))
# #     if a == 0:
# #         print("Вы прекратили пытаться")
# #         print("Количество попыток:", i)
# #         break
# #     if a < n:
# #         print("число меньше:")
# #     elif a == n:
# #         print("вы угадали!", "\nколичество попыток:", i)
# #         break
# #     else:
# #         print("число больше")
# #    i += 1
#
# # Задание 7
#
# # n = [int(input("-> ")) for i in range(int(input("n = ")))]
# # a = len(n)
# # for i in range(0, a, 2):
# #     print(n[i], end=" ")
#
# # Задание 8
#
# # n = [int(input("-> ")) for i in range(int(input("n = ")))]
# # a = len(n)
# # n.sort(reverse=True)
# # for i in range(a):
# #     print(n[i], end=" ")
#
# # n = [int(input("-> ")) for i in range(int(input("n = ")))]
# # for i in range(1, len(n)):
# #     if n[1] > n[i - 1]:
# #         print(n[i], end=" ")
#
#
# n = [int(input("-> ")) for i in range(int(input("n = ")))]
# a = len(n)
# for i in range(0, a, 2):
#     print(n[i], end=" ")
# # Задание 8
#
# w = [int(input("-> ")) for i in range(int(input("n = ")))]
# for i in range(1, len(w)):
#     if w[1] > w[i - 1]:
#         print(w[i], end=" ")
#
# # другой вариант
#
# w = [int(input("-> ")) for i in range(int(input("n = ")))]
# a = len(w)
# w.sort(reverse=True)
# for i in range(a):
#     print(w[i], end=" ")
#
# # Дополнительно
#
# w = int(input("Ширина треугольника: "))
# h = int(input("Высота треугольника: "))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i <= h + 1 or j == 0 or j == w + 1:
#             print("*", end="")
#     w += 2
#
# # 6 Урок
#
# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# for i in range(len(a)):
#     print(a)
#     break
# c = []
# for k in a:
#     b = 0
#     for j in a:
#         if k == j:
#             b += 1
#     if b == 1:
#         c.append(k)
# print(c)
#
# a = [1, 2, 3]
# b = [11, 22, 33, 4, 2]
# c = []
# i = 0
# while i < len(a):
#     c.append(a[i])
#     c.append(b[i])
#     i += 1
# print(c + b[3:5])
#
# # другой вариант
# a = [1, 2, 3]
# b = [11, 12, 13, 4, 2]
# c = []
# print("a =", a)
# print("b =", b)
#
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# print("c =", c)
#
# # 7 Урок
#
#
#
# n = [[r.randint(-20, 10) for a in range(3)]
#      for b in range(4)]
# m = 0
# for s in n:
#     for a in s:
#         if a < 0:
#             m += 1
#         print(a, end="\t\t")
#     print()
# print(f'Количество отрицательных элементов: {m}')
# # #2
#
# n = [[r.randint(0, 4) for i in range(3)]
#      for j in range(4)]
# m = 1
# for k in n:
#     for i in k:
#         if i > 0:
#             m *= i
#         print(i, end="\t\t")
#     print()
# print(f'Произведение ненулевых элементов: {m}')
# # 3
# main_list = [[r.randint(0, 10) for i in range(6)] for j in range(6)]
# sub_list = [r.randint(0, 10) for k in range(6)]
#
# # print(main_list)
# for row in range(len(main_list)):
#     for i in range(len(main_list[row])):
#         print(main_list[row][i], end='\t\t')
#     print()
# print(sub_list)
# for row in range(len(main_list)):
#     for i in range(len(main_list[row])):
#         if row % 2 == 0:
#             main_list[row] = sub_list
#         print(main_list[row][i], end='\t\t')
#     print()
# # 8 Урок
#
# # def change(lst):
# #     lst[0], lst[-1] = lst[-1], lst[0]
# #     return lst
# #
# #
# # print(change([1, 2, 3]))
# # print(change([9, 12, 33, 54, 105]))
# # print(change(["с", "л", "о", "н"]))
#
#
# def change(lst):
#     s = lst.pop()
#     k = lst.pop(0)
#     lst.append(k)
#     lst.insert(0, s)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))

# 9 урок
import math


# 10 Занятие
# Задание №"1

# s = ('ab', 'abcd', 'cde', 'abc', 'def')
# a = str(input('->'))
# print(s)
# print('s =', a)
# print('yes' if a in s else 'no')
#
#
# # №2
#
# # Введите по порядку, без пробелов, элементы кортежа: 253523651
# s = tuple(str(input("->")))
# print(s)
# print('Количество 2 =', s.count('2'))
# print('Количество 5 =', s.count('5'))
# print('Количество 3 =', s.count('3'))
# print('Количество 6 =', s.count('6'))
# print('Количество 1 =', s.count('1'))
#

#Условия задания:

#На вход программе даётся строка, состоящая из слов, разделенных
#пробелами. Напишите программу, которая подсчитывает количество слов в
#этой строке.
#Примечание: задачу можно решить в одну строку кода.

#Алгоритм:


result = 0
str_input = input('Введите строку >')

print(f'Количество слов в строке {len(str_input.split())}')

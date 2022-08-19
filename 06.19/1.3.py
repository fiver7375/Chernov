#Условия задания:

#На вход программе подаётся натуральное число n. Напишите программу,
#которая вычисляет сумму всех его делителей.

#Алгоритм:


from cmath import sqrt

from numpy import square

result = 0
int_input = int(input('Введите целое число >'))
for i in range(1, int_input + 1):
    if int_input % i == 0:
        result += i
print(f'Сумма всех делителей числа {int_input} равна {result}')

#Условия задания:

#Напишите программу, которая считывает три числа и подсчитывает
#сумму только положительных чисел.

#Алгоритм:


int_input1 = int(input('Введите первое целое число >'))
int_input2 = int(input('Введите второе целое число >'))
int_input3 = int(input('Введите третье целое число >'))

result = 0

if int_input1 > 0: result = result + int_input1
if int_input2 > 0: result = result + int_input2
if int_input3 > 0: result = result + int_input3

print(f'Сумма положительных чисел: {result}', sep = '\n')

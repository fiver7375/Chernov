#Условия задания:

#На вход программе подаётся натуральное число n, а затем n целых чисел,
#каждое на отдельной строке. Напишите программу, которая подсчитывает
#сумму введённых чисел.



#Алгоритм:

cnt_input = int(input('Введите целое число >'))
result = 0
for i in range(cnt_input):
    int_input = int(input(f'Введите {i + 1}-е целое число из {cnt_input}>'))
    result += int_input
print(f'Сумма введённых чисел равна {result}')

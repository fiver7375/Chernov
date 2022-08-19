#Условия задания:

#Напишите программу, которая подсчитает количество «счастливых»
#билетиков в одном рулоне, если номер первого билета в рулоне 000001, а
#номер последнего 999999.


#Алгоритм:


result = 0
for i in range(1, 1000000):
    str_input = f'{i:06}'
    #print(i, str_input, sep = ' ')
    if int(str_input[0]) + int(str_input[1]) + int(str_input[2]) == int(str_input[3]) + int(str_input[4]) + int(str_input[5]):
        result += 1

print(f'Количество "счастливых" билетов {result}')


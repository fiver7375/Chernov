#Условия задания:

#Напишите программу для пересчёта величины временного интервала,
#заданного в минутах, в величину, выраженную в часах и минутах.

#Алгоритм:
#Перевод в часы - деление нацело введенного числа на 60
#Мнуты - остаток от деления введенного числа на 60


int_input = int(input('Введите целое число >'))
print(int_input, ' минут(ы) - это ', int_input // 60 , ' час(а)(ов) ', int_input % 60, ' минут(ы)', sep = '')

# Напишите функцию, которая открывает на чтение созданные 
# в прошлых задачах файлы с числами и именами. Перемножьте 
# пары чисел. В новый файл сохраните имя и произведение:
# если результат умножения отрицательный, сохраните имя 
# записанное строчными буквами и произведение по модулю
# если результат умножения положительный, сохраните имя 
# прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк, 
# сколько в более длинном файле. При достижении конца 
# более короткого файла, возвращайтесь в его начало.

from task1 import rnd_num
from task2 import rnd_name_in_file

__all__ = ['len_list', 'open_file']

def len_list(list1, list2):
    if len(list2) > len(list1):
        temp = len(list1)
        for i in range(len(list2)):
            if i > len(list1) - 1:
                list1.append(list1[i % temp])
    elif len(list2) < len(list1):
        temp = len(list2)
        for i in range(len(list1)):
            if i > len(list2) - 1:
                list2.append(list2[i % temp])
    return list1, list2

def open_file(file_names, file_numbers, output):
    with (
        open(file_names, 'r', encoding='utf-8') as a,
        open(file_numbers, 'r', encoding='utf-8') as b,
        open(output, 'w', encoding='utf-8') as c
    ):
        names = a.read().split('\n')
        num = b.read().split('\n')
        for i, j in zip(*len_list(names, num)):
            if j == "":
                continue
            first, second = map(float, j.split('|'))
            result = first * second
            if result < 0:
                c.write(f'{i.lower()} {abs(result)}')
            elif result > 0:
                c.write(f'{i.lower()} {int(result)}')



if __name__=="__main__":
    # list2 = [1,5,8]
    # list1 = [1, 2, 3, 4, 5, 9, 9, 7]
    rnd_num(10, 'packeg_seminar7/num1.txt')
    rnd_name_in_file(5, 'packeg_seminar7/names2.txt')
    print(len_list(r'packeg_seminar7/names2.txt', r'packeg_seminar7/num1.txt', r'packeg_seminar7/output.txt'))


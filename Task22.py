# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
print("Введите количество элементов первого списка")
first_quantity=int(input())
first_list=[]
for i in range(first_quantity):
    print("Введите элемент № ",i)
    first_list.append(int(input()))
print("Первый список",first_list)
second_list=[]
print("Введите количество элементов второго списка")
second_quantity=int(input())
for j in range(second_quantity):
    print("Введите элемент № ",j)
    second_list.append(int(input()))
print("Второй список",second_list)
union_list=first_list+second_list
union_list.sort()
unique=set(union_list)
print("Уникальные отсортированные числа из обоих списков:",unique)
# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
import random




print("Введите количество кустов черники")
blackberry_quantity=int(input())
numbers_of_berries=[]




for i in range(blackberry_quantity):
    numbers_of_berries.append(random.randint(1,20))
print("Количество ягод на кустах:", numbers_of_berries)
max_of_berries=0
j=0
while j<blackberry_quantity:
    if j ==0:
        max_of_berries=numbers_of_berries[j]+numbers_of_berries[j+1]+numbers_of_berries[blackberry_quantity-1]
    elif 0<j and j<(blackberry_quantity-1):
        if max_of_berries<(numbers_of_berries[j]+numbers_of_berries[j+1]+numbers_of_berries[j-1]):
            max_of_berries=(numbers_of_berries[j]+numbers_of_berries[j+1]+numbers_of_berries[j-1]) 
    elif j==(blackberry_quantity-1):
        if max_of_berries<(numbers_of_berries[j]+numbers_of_berries[0]+numbers_of_berries[j-1]):
            max_of_berries=(numbers_of_berries[j]+numbers_of_berries[0]+numbers_of_berries[j-1])
    j+=1
    



print("За один раз собирающий модуль может собрать следующее максимальное количество ягод:", max_of_berries)
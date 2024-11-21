# Выводим все четные и нечетные числа, разные варианты

# Функция filter используется для фильтрации элементов итерируемого объекта на основе заданного условия 
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  

even_numbers_2 = list(filter(lambda x: x % 2 != 0, numbers))
print(even_numbers_2)

for i in range(1, 11):
    if i % 2 == 0:
        print(i,end=' ')
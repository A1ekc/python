# Задать список вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов
# Остаток от деления на единицу даст нужный результат : print(a%1)
lst = [1.1, 1.2, 3.1, 5, 10.01]#создаём список
lstNew = [round(i%1, 2) for i in lst if i%1 != 0]
#print(lstNew) создаём новый лист только с дробной частью, убираем нулевые значения
print(lstNew)
print(f"Разница между максимальным и минимальным значением дробной части элементов: {max(lstNew) - min(lstNew)}")

  


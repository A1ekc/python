# приложение по умножению двух чисел
x = 0
y = 0

def init(a, b): # метод по инициализации начальных значений нашим числам
    global x 
    global y
    x = a
    y = b 

def mnoz(): #метод который возвращает сумму двух чисел
    return x * y

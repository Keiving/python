#9.1. Определите функцию good(), которая возвращает следующий список:
#['Harry', 'Ron', 'Hermione'].
def good():
    return ['Harry', 'Ron', 'Hermione']
good()
['Harry', 'Ron', 'Hermione']

#9.2. Определите функцию генератора get_odds(), которая возвращает нечетные
#числа из диапазона range(10). Используйте цикл for, чтобы найти и вывести
#третье возвращенное значение.
def get_odds():
    for number in range(1,10,2):
        yield number
count = 1
for number in get_odds():
    if count == 3:
        print ("Третье нечетное число это", number)
        break
    count +=1

#9.3. Определите декоратор test, который выводит строку 'start' при вызове функ-
#ции и строку 'end', когда функция завершает свою работу.
def test(func):
    def new_func(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return new_func
@test
def greeting():
    print("Привет")
greeting()


#1. Создайте функцию:
# def func1(num):
# n = num * 5
# print (n) 
# Вызовите ее, передав в качестве аргумента значение глобальной переменной,
# затем любое число и, наконец, любую строку.
#2. Выполните с помощью интерпретатора Python скрипт, предварительно
# исправив код функции так, чтобы она возвращала значение переменной n:
# >>> def func(n):
# if n < 3:
# n = n*10

# >>> a = 2
# >>> b = func(a)
# >>> a
#2
# >>> b # Почему с переменной не связано никакого значения?



print("1._______________");
def func1(num):
	n = num * 5;
	print (n);
def func2():
	global var_int;
	n = var_int * 5;
	print (n);
def func3():
	global var_str;
	n = var_str + "_new";
	print (n);

int_1 = int(input('Введите число: '));
func1(int_1);

var_int = 111;
func2();

var_str = "lab12";
func3();






print("_________________");

print("2._______________");

print("_________________");


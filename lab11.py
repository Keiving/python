#1. Напишите функцию, которая вычисляет сумму трех чисел и возвращает
# результат в основную ветку программы.
#2. Придумайте программу, в которой из одной функции вызывается вторая. При
# этом ни одна из них ничего не возвращает в основную ветку программы, обе
# должны выводить результаты своей работы с помощью функции print().
 

print("1._______________");

def summ_3(number_1, number_2, number_3): 
	return number_1 + number_2 + number_3;

int_1 = int(input('1 число: '));
int_2 = int(input('2 число: '));
int_3 = int(input('3 число: '));

summ_3(int_1, int_2, int_3);
print('Сумма 3 чисел = ',summ_3(int_1, int_2, int_3));

print("_________________");

print("2._______________");

def one(): 
	print("öne");
	two();

def two(): 
	print("two");

one();
print("_________________");


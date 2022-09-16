#1. Напишите программу по следующему описанию:
#a. двум переменным присваиваются числовые значения;
#b. если значение первой переменной больше второй, то найти разницу
#значений переменных (вычесть из первой вторую), результат связать с
#третьей переменной;
#c. если первая переменная имеет меньшее значение, чем вторая, то третью
#переменную связать с результатом суммы значений двух первых
#переменных;
#d. во всех остальных случаях, присвоить третьей переменной значение первой переменной;
#e. вывести значение третьей переменной на экран.

from unicodedata import name


print ("1._____________");

var_1 = 4;
var_2 = 2;
if var_1 > var_2: var_3 = var_1 - var_2;
elif var_1 < var_2: var_3 = var_1 + var_2;
else : var_3 = var_1;
print ("Значение третьей переменной = ", var_3);
print('______________________');

print ("2._____________");
def findLen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter;

my_name = "Daniil";
other_name = "Denis";
if findLen(my_name) == findLen(other_name): print ("Имена одинаковые по длине");
elif findLen(my_name) > findLen(other_name): print("Первое имя длинне второго");
elif findLen(my_name) < findLen(other_name): print ("Второе имя длинне первого");
elif findLen(my_name) != findLen(other_name): print("Имена разные по длине");
else : print('Длина первого имени - ', findLen(my_name) ,' Длина второго имени - ', findLen(other_name))
	 

print('______________________');

	
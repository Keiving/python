#1. Присвойте двум переменным любые числовые значения.
#2. Составьте четыре сложных логических выражения с помощью оператора and,
# два из которых должны давать истину, а два других - ложь.
#3. Аналогично выполните п. 2, но уже используя оператор or.
#4. Попробуйте использовать в сложных логических выражениях работу с
# переменными строкового типа. 
var_1 = 1;
var_2 = 2;

if var_1 != var_2 and var_1 == 1:  print("TRUE (var_1 не равен var_2, а var_1 равен 1)")
else:  print('FALSE (var_1 равен var_2, а var_1 не равен 1)');


if var_1*var_2 != 2 or var_2*1 != 2: print("TRUE")
else: print("false");

if var_1/var_2 == 0.5 and var_2/var_1 == 1: print('true')
else: print('false')

if  str(var_1) != str(var_2) or var_2*0.5 != var_1: print ('true')
else: print ('false')
	
if var_1 == var_2: print('12321321321')
else: print('gfdsgfsgdfsg')
	
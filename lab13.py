print("Задание 1");
x = int(input('Введите число от 1 до 9: '));
print(x);

if x>=1 and x<=3:
	s = input('Введите строку: ');
	n = int(input('Введите количество повторов строки: '));
	for item in range(n):
		print(s);
elif x>=4 and x<=6:
	m=int(input('введите степень, в которую следует возвести число: '))
	print(x**m)
elif x>=7 and x<=9:
	for num in range(10):
		num = num + 1;
		print(x+num);

else: 
	print("Ошибка ввода");
	
print("____________________");


print("Задание 2 \n Общество в начале XXI века");
age = int(input("Ваш возраст: "));
if age>= 0 and age <7:
	print("Вам в детский сад");
elif age >= 7 and age<18:
	print("Вам в школу");
elif age >= 18 and age<25:
	print("Вам в профессиональное учебное заведение");
elif age >= 25 and age<60:
	print("Вам на работу");
elif age >= 60 and age<120:
	print("Вам предоставляется выбор");
elif age < 0 and age>120:
	for item in range(5):
		print("Ошибка! Это программа для людей!")
		item = item + 1;		

print("____________________");

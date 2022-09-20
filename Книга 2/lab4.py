#Выберите число от 1 до 10 и присвойте его переменной secret. Выберите еще
#одно число от 1 до 10 и присвойте его переменной guess. Далее напишите услов-
#ные проверки (if, else и elif), чтобы вывести строку 'too low', если значение
#переменной guess меньше 7, 'too high', если оно больше 7, и 'just right', если
#равно secret.
secret = 7
guess = 5
if guess < secret:
	print('too low')
elif guess > secret:
	print('too high')
else:
	print('just right')

#4.2. Присвойте значения True или False переменным small и green. Напишите не-
# сколько утверждений if/else, которые выведут на экран информацию о том,
# соответствуют ли заданным условиям следующие растения: вишня, горошек,
# арбуз, тыква.
small = False
green = True
if small:
	if green:
		print("горох")
	else:
		print("вишня")
else:
	if green:
		print("арбуз")
	else:
		print("тыква")
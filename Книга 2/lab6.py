#6.1. Используйте цикл for, чтобы вывести на экран значения списка [3, 2, 1, 0].
for value in [3, 2, 1, 0]:
	print(value);

#6.2. Присвойте значение 7 переменной guess_me и значение 1 переменной number. На-
# пишите цикл while, который сравнивает переменные number и guess_me. Выведите
# строку 'too low', если значение переменной number меньше значения переменной
# guess_me. Если значение переменной number равно значению переменной guess_me,
# выведите строку 'found it!' и выйдите из цикла. Если значение переменной
# number больше значения переменной guess_me, выведите строку 'oops' и выйдите
# из цикла. Увеличьте значение переменной number на выходе из цикла.
guess_me = 7
number = 1
while True:
	if number < guess_me:
		print('too low');
	elif number == guess_me:
		print('found it!');
		break;
	elif number > guess_me:
		print('oops');
		break;
	number += 1;

#6.3. Присвойте значение 5 переменной guess_me. Используйте цикл for, чтобы
# проитерировать с помощью переменной number по диапазону range(10). Если
# значение переменной number меньше, чем значение guess_me, выведите на экран
# ообщение 'too low'. Если оно равно значению guess_me — выведите сообщение
# found it!, а затем выйдите из цикла. Если значение переменной number больше,
# чем guess_me, выведите на экран сообщение 'oops' и выйдите из цикла.
guess_me = 5
for number in range(10):
	if number < guess_me:
		print("too low");
	elif number == guess_me:
		print("found it!");
		break;
	else:
		print("oops");
		break;
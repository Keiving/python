#Урок 8. Ввод данных с клавиатуры
#1. Создайте скрипт (файл data.py), который бы запрашивал у пользователя
#- его имя: "What is your name?"
#- возраст: "How old are you?"
#- место жительства: "Where are you live?"
#, а затем выводил три строки
#- "This is имя"
#- "It is возраст"
#- "He live in место_жительства"
#, где вместо имя, возраст, место_жительства должны быть соответствующие
#данные, введенные пользователем.
#2. Напишите программу (файл example.py), которая предлагала бы пользователю
#решить пример 4*100-54. Если пользователь напишет правильный ответ, то
#получит поздравление от программы, иначе – программа сообщит ему об
#ошибке. (При решении задачи используйте конструкцию if-else.)
#3. Перепишите предыдущую программу так, чтобы пользователю предлагалось
#решать пример до тех пор, пока он не напишет правильный ответ. (При
#решении задачи используйте цикл while.)

print("1. ____________");
name = input("Whats y name: ");
old = input("How old are y ?: ");
lacal = input("Where are y live ?: ");
print("This is, ", name);
print("It's, ", old);
print("He live in, ", lacal);
print("__________________");

print("2. ____________");

print("Решите пример: 4*100-54 =  ");
ver_result = 4*100-54
result = int(input());

if result == ver_result: 
	print("Верно !");
else: print("НЕПРАВИЛЬНО");
	
print("__________________");

print("3. ____________");
cicle = True;
print("Решите пример: 4*100-54 =  ");
ver_result = 4*100-54
while cicle: 
	result = int(input());
	if result == ver_result: 
		cicle = False
		print("Верно !")
	else: 
		print("НЕПРАВИЛЬНО, попробуй еще раз");
print("__________________");

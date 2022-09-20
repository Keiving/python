#5.1. Напишите с заглавной буквы слово, которое начинается с буквы m:
song = """When an eel grabs your arm, And it causes great harm, That's - a moray!""";
song = song.replace(" m", " M");
print(song);

#Выведите на экран все вопросы из списка, а также правильные ответы в таком
# виде:
#Q: вопрос
#A: ответ

questions = [
	"We don't serve strings around here. Are you a string?",
 	"What is said on Father's Day in the forest?",
 	"What makes the sound 'Sis! Boom! Bah!'?"
]
answers = [
	"An exploding sheep.",
	"No, I'm a frayed knot.",
	"'Pop!' goes the weasel."
]
q_a = ( (0, 1), (1,2), (2, 0) );
for q, a in q_a:
	print("Q:", questions[q])
	print("A:", answers[a])
print()

#Выведите на экран следующее стихотворение, используя старый стиль фор-
#матирования. Подставьте в него такие строки: 'roast beef', 'ham', 'head',
#и 'clam':

stih = '''
	My kitty cat likes %s,
	My kitty cat likes %s,
	My kitty cat fell on his %s
	And now thinks he's a %s.
'''
args = ('roast beef', 'ham', 'head', 'clam');
print(stih % args);

#5.4. Напишите письмо с использованием нового стиля форматирования. Сохраните
# предложенную строку в переменной letter (она понадобится вам в упражне-
# нии ниже):
	#Dear {salutation} {name},
	#Thank you for your letter. We are sorry that our {product}
	#{verbed} in your {room}. Please note that it should never
	#be used in a {room}, especially near any {animals}.
	#Send us your receipt and {amount} for shipping and handling.
	#We will send you another {product} that, in our tests,
	#is {percent}% less likely to have {verbed}.
	#Thank you for your support.
	#Sincerely,
	#{spokesman}
	#{job_title}

letter = '''
	Dear {salutation} {name},
	Thank you for your letter. We are sorry that our {product}
	{verbed} in your {room}. Please note that it should never
	be used in a {room}, especially near any {animals}.
	Send us your receipt and {amount} for shipping and handling.
	We will send you another {product} that, in our tests,
	is {percent}% less likely to have {verbed}.
	Thank you for your support.
	Sincerely,
	{spokesman}
	{job_title}
'''
print(letter);

#5.5. Присвойте значения переменным 'salutation', 'name', 'product', 'verbed' (глагол
# в прошедшем времени), 'room', 'animals', 'percent', 'spokesman' и 'job_title'.
# С помощью функции letter.format() выведите на экран значение переменной
# letter, в которую подставлены эти значения.

print (
	letter.format(salutation='Ambassador',
	name='Nibbler',
	product='pudding',
	verbed='evaporated',
	room='gazebo',
	animals='octothorpes',
	amount='$1.99',
	percent=88,
	spokesman='Shirley Iugeste',
	job_title='I Hate This Job')
)

#5.6. После проведения публичных опросов с целью выбора имени появились: ан-
# глийская подводная лодка Boaty McBoatface, австралийская беговая лошадь
# Horsey McHorseface и шведский поезд Trainy McTrainface. Используйте фор-
# матирование с символом % для того, чтобы вывести на экран победившие имена
# для утки, тыквы и шпица (пример Д.1).
print("d1__________________");
names = ["duck", "gourd", "spitz"]
for name in names:
	cap_name = name.capitalize()
	print("%sy Mc%sface" % (cap_name, cap_name))

print("d2__________________");
names = ["duck", "gourd", "spitz"]
for name in names:
	cap_name = name.capitalize()
	print("{}y Mc{}face".format(cap_name, cap_name))

print("d3__________________");
names = ["duck", "gourd", "spitz"]
for name in names:
	cap_name = name.capitalize()
	print(f"{cap_name}y Mc{cap_name}face")
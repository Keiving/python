#7.1. Создайте список years_list, содержащий год, в который вы родились, и каждый
# последующий год вплоть до вашего пятого дня рождения. Например, если вы
# родились в 1980 году, то список будет выглядеть так: years_list = [1980, 1981,
# 1982, 1983, 1984, 1985].
years_list = [1998, 1999, 2000, 2001, 2002, 2003];

#7.2. В какой год из списка years_list был ваш третий день рождения? Учтите, 
# в первый год вам было 0 лет.
print(years_list[3]);

#7.3. В какой год из списка years_list вам было больше всего лет?
print(years_list[-1]);


#7.4. Создайте список things, содержащий три элемента: "mozzarella", "cinderella", 
# "salmonella".
things = ["mozzarella", "cinderella", "salmonella"];

#7.5. Напишите с большой буквы тот элемент списка things, который означает чело-
# века, а затем выведите список. Изменился ли элемент списка?
things[1] = things[1].capitalize();
print(things);

#7.6. Переведите сырный элемент списка things в верхний регистр целиком и вы-
# ведите список.

things[0] = things[0].upper();
print(things);

#7.7. Удалите из списка things заболевание, получите Нобелевскую премию и затем
# выведите список на экран.
things.remove("salmonella");
print(things);

#7.8. Создайте список с элементами "Groucho", "Chico" и "Harpo"; назовите его
# surprise.
surprise = ['Groucho', 'Chico', 'Harpo'];

#7.9. Напишите последний элемент списка surprise со строчной буквы, затем вы-
# ведите эту строку в обратном порядке и с прописной буквы.
surprise[-1] = surprise[-1].lower()
surprise[-1] = surprise[-1][::-1]
surprise[-1].capitalize()
print(surprise[-1]);

#7.10. Используйте списковое включение, чтобы создать список с именем even, в ко-
# тором будут содержаться четные числа в промежутке range(10).

even = [number for number in range(10) if number % 2 == 0];
print(even);

#7.11. Попробуйте создать генератор рифм для прыжков через скакалку. Нужно вы-
# вести на экран последовательность двухстрочных рифм. Начните программу
# с этого фрагмента:
#start1 = ["fee", "fie", "foe"];
#rhymes = [
#	("flop", "get a mop"),
#	("fope", "turn the rope"),
#	("fa", "get your ma"),
#	("fudge", "call the judge"),
#	("fat", "pet the cat"),
#	("fog", "walk the dog"),
#	("fun", "say we're done"),
#]
#start2 = "Someone better"

start1 = ["fee", "fie", "foe"]
rhymes = [
	("flop", "get a mop"),
	("fope", "turn the rope"),
	("fa", "get your ma"),
	("fudge", "call the judge"),
	("fat", "pet the cat"),
	("fog", "pet the dog"),
	("fun", "say we're done"),
]
start2 = "Someone better"
start1_caps = " ".join([word.capitalize() + "!" for word in start1])
for first, second in rhymes:
	print(f"{start1_caps} {first.capitalize()}!")
	print(f"{start2} {second}.")
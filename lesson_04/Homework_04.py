adwentures_of_tom_sawer  =  """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01  =  = 
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
print("TASK #1")

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")

print(adwentures_of_tom_sawer)
print() #для пробілу між тасками

# task 02  =  = 
""" Замініть .... на пробіл
"""
print('TASK #2')

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")

print(adwentures_of_tom_sawer)
print() #для пробілу між тасками

# task 03  =  = 
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
print('TASK #3')

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("   ", " ")

print(adwentures_of_tom_sawer)
print() #для пробілу між тасками


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print('TASK #4')

print(adwentures_of_tom_sawer.count("h"))
print() #для пробілу між тасками

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print('TASK #5')

words_in_text  =  adwentures_of_tom_sawer.split()
count  =  sum(word[0].isupper() for word in words_in_text)

print(count)
print() #для пробілу між тасками

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print("TASK #6")

print(len(adwentures_of_tom_sawer)) #для визначення загальної кількості символів

print(adwentures_of_tom_sawer.find("Tom", 1,507))
print()#для пробілу між тасками

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
print("TASK #7")

adwentures_of_tom_sawer_sentences  =  adwentures_of_tom_sawer.split('. ')

print(adwentures_of_tom_sawer_sentences)
print()#для пробілу між тасками


# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("TASK #8")

print(adwentures_of_tom_sawer_sentences[3].lower()) #використала індекс 3 так як 4 речення під індексом 3
print()#для пробілу між тасками


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print("TASK #9")

print(any(sentence.startswith("By the time") for sentence in adwentures_of_tom_sawer_sentences))
print()#для пробілу між тасками

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print("TASK #10")

print(adwentures_of_tom_sawer_sentences[-1])
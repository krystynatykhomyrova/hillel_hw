alice_in_wonderland = "Would you tell me, please, which way I ought to go from here?""\n""That depends a good deal on where you want to get to," "said the Cat.""\n""I don't much care where ——""said Alice.""\n""Then it doesn't matter which way you go," "said the Cat.""\n""—— so long as I get somewhere," "Alice added as an explanation.""\n""Oh, you're sure to do that," "said the Cat, ""if you only walk long enough."
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
single_quotes = [char for char in alice_in_wonderland if char == "'"]
print(single_quotes)
print ("'" in alice_in_wonderland)
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)
print()  # Порожній рядок для розділення відповідей


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
print("TASK #4")
s_black_sea = int(436402)
s_azov_sea = int(37800)
sum_both_sea = s_black_sea + s_azov_sea
print("Яку площу займають Чорне та Азовське моря разом?", sum_both_sea)
print()  # Порожній рядок для розділення відповідей

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
print("TASK #5")
store_1_store_2 = 250449
store_2_store_3 = 222950
store_1_store_2_store_3 = 375291
store_1 = store_1_store_2_store_3 - store_2_store_3
store_3 = store_1_store_2_store_3 - store_1_store_2
store_2 = store_1_store_2_store_3 - store_1 - store_3

print("кількість книжок на складі 1:",store_1, "кількість книжок на складі 2:",store_2, "кількість книжок на складі 3:",store_3)

print()  # Порожній рядок для розділення відповідей

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
print("TASK #6")
month = 18
amount_per_month = 1179
price = month * amount_per_month

print("Bартість комп’ютера:", price, "грн" )
print()  # Порожній рядок для розділення відповідей


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print("TASK #7")
a = 8019 % 8
print("Остача від ділення 8019 на 8:", a)
b = 9907 % 9
print("Остача від ділення 9907 на 9:", b)
c = 2789 % 5
print("Остача від ділення 2789 на 5:", c)
d = 7248 % 6
print("Остача від ділення 7248 на 6:", d)
e = 7128 % 5
print("Остача від ділення 7128 на 5:", e)
f = 19224 % 9
print("Остача від ділення 19224 на 9:", f)
print()  # Порожній рядок для розділення відповідей

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
print("TASK #8")
pizza_large = 4
pizza_medium = 2
juice = 4
cake = 1
water = 3

price_pizza_large = 274
price_pizza_medium = 218
price_juice = 35
price_cake = 350
price_water = 21

total_price = (pizza_large * price_pizza_large +
              pizza_medium * price_pizza_medium +
              juice * price_juice +
              cake * price_cake +
              water * price_water)


print("Загальна вартість замовлення:", total_price, "грн")
print()  # Порожній рядок для розділення відповідей

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
print("TASK #9")

photos = 232
photos_per_page = 8
amount_pages =  photos/photos_per_page

print("Скільки сторінок знадобиться Ігорю, щоб вклеїти всі фото?",int(amount_pages), "сторінок" )
print()  # Порожній рядок для розділення відповідей
# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

print("TASK #10")

distance = 1600 #km
tanks_per_100_km = 9 #l
Tank_capacity = 48 #l
tank_for_all_treap = 1600/100 *  tanks_per_100_km
gas_station = tank_for_all_treap/Tank_capacity

print("Скільки літрів бензину знадобиться для такої подорожі?", int(tank_for_all_treap), "літрів")
print("Скільки щонайменше разів родині необхідно заїхати на заправку під час цієї подорожі, кожного разу заправляючи повний бак?", int(gas_station ))


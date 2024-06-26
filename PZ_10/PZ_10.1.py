#В магазинах имеются следующие товары. Магнит – молоко, соль, сахар. Пятерочка –
#мясо, молоко, сыр. Определить:
#1. какие товары из Магнита, отсутствуют в Пятерочке.
#2. какие товары из Пятерочки, отсутствуют в Магните
#3. полный перечень всех товаров.
#4. равны ли перечни товаров
magnit = {'молоко', 'соль', 'сахар',}
pyaterochka = {'мясо', 'молоко', 'сыр'}

# определение отсутствующих товаров
magnit_not_in_pyaterochka = magnit - pyaterochka
pyaterochka_not_in_magnit = pyaterochka - magnit

# полный перечень всех товаров
all_products = magnit | pyaterochka

#проверка на равенство наборов товаров
equal_sets = (magnit == pyaterochka)

# Вывод результатов
print("1)Товары из Магнита, отсутствующие в Пятерочке:", magnit_not_in_pyaterochka)
print("2)Товары из Пятерочки, отсутствующие в Магните:", pyaterochka_not_in_magnit)
print("3)Полный перечень всех товаров:", all_products)
print("4)Равны ли наборы товаров:", equal_sets)

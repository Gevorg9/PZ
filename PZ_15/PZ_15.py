"""Приложение ОПТОВАЯ БАЗА для автоматизированного контроля движения
товаров на оптовой базе. Таблица Товары должна содержать следующие данные: Код
товара, Наименование товара, Наименование магазина, Заявки магазина, Количество
товара на складе, Единицы измерения, Оптовая цена. """
import sqlite3

def create_database():

    con = sqlite3.connect('Wholesale_base.db')
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_code INTEGER PRIMARY KEY,
            product_name TEXT,
            shop_name TEXT,
            shop_applications INTEGER,
            product_amount INTEGER,
            Units TEXT,
            Wholesale_price DECIMAL
        )
    """)
    con.commit()
    con.close()

def add_product():

    con = sqlite3.connect('Wholesale_base.db')
    cur = con.cursor()

    try:
        product_code = int(input("Введите код товара: "))
        product_name = input("Введите наименование товара: ")
        shop_name = input("Введите наименование магазина: ")
        shop_applications = int(input("Введите количество заявок магазина: "))
        poduct_amount = int(input("Введите количество товара на складе: "))
        Units = input("Введите единицы измерения: ")
        Wholesale_price = float(input("Введите оптовую цену: "))

        cur.execute("""
            INSERT INTO products VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (product_code, product_name, shop_name, shop_applications,
              poduct_amount, Units, Wholesale_price))
        con.commit()
        print("Товар успешно добавлен!")

    except ValueError:
        print("Ошибка: Введены некорректные данные.")
    finally:
        con.close()

def search_products():

    print("\nВарианты поиска:")
    print("1. По коду товара")
    print("2. По наименованию товара")
    print("3. По наименованию магазина")

    choice = input("Выберите вариант поиска: ")

    con = sqlite3.connect('Wholesale_base.db')
    cur = con.cursor()

    try:
        if choice == '1':
            product_code = int(input("Введите код товара: "))
            cur.execute("SELECT * FROM products WHERE product_code=?", (product_code,))
        elif choice == '2':
            product_name = input("Введите наименование товара: ")
            cur.execute("SELECT * FROM products WHERE product_name LIKE ?", ('%' + product_name + '%',))
        elif choice == '3':
            shop_name = input("Введите наименование магазина: ")
            cur.execute("SELECT * FROM products WHERE shop_name LIKE ?", ('%' + shop_name + '%',))
        else:
            print("Неверный выбор.")
            return

        results = cur.fetchall()

        if results:
            print("\nРезультаты поиска:")
            for row in results:
                print(f"Код товара: {row[0]}, Наименование: {row[1]}, Магазин: {row[2]}, Заявки: {row[3]}, "
                      f"Количество: {row[4]}, Ед.изм.: {row[5]}, Цена: {row[6]:.2f}")
        else:
            print("Товары не найдены.")

    except ValueError:
        print("Ошибка: Введены некорректные данные.")
    finally:
        con.close()

def delete_products():

    print("\nВарианты удаления:")
    print("1. По коду товара")
    print("2. По наименованию товара")
    print("3. По наименованию магазина")

    choice = input("Выберите вариант удаления: ")

    con = sqlite3.connect('Wholesale_base.db')
    cur = con.cursor()

    try:
        if choice == '1':
            product_code = int(input("Введите код товара: "))
            cur.execute("DELETE FROM products WHERE product_code=?", (product_code,))
        elif choice == '2':
            product_name = input("Введите наименование товара: ")
            cur.execute("DELETE FROM products WHERE product_name=?", (product_name,))
        elif choice == '3':
            shop_name = input("Введите наименование магазина: ")
            cur.execute("DELETE FROM products WHERE shop_name=?", (shop_name,))
        else:
            print("Неверный выбор.")
            return

        con.commit()
        print("Записи успешно удалены!")

    except ValueError:
        print("Ошибка: Введены некорректные данные.")
    finally:
        con.close()

def edit_product():
    con = sqlite3.connect('Wholesale_base.db')
    cur = con.cursor()

    try:
        product_code = int(input("Введите код товара для редактирования: "))

        # Проверка, существует ли товар с таким кодом
        cur.execute("SELECT 1 FROM products WHERE product_code=?", (product_code,))
        if not cur.fetchone():
            print("Товар с таким кодом не найден.")
            return

        print("\nЧто вы хотите изменить?")
        print("1. Наименование товара")
        print("2. Наименование магазина")
        print("3. Заявки магазина")
        print("4. Количество товара на складе")
        print("5. Единицы измерения")
        print("6. Оптовая цена")

        choice = input("Выберите вариант: ")

        if choice == '1':
            new_name = input("Введите новое наименование товара: ")
            cur.execute("UPDATE products SET product_name=? WHERE product_code=?", (new_name, product_code))
        elif choice == '2':
            new_shop = input("Введите новое наименование магазина: ")
            cur.execute("UPDATE products SET shop_name=? WHERE product_code=?", (new_shop, product_code))
        elif choice == '3':
            new_apl = input("Введите новое количество заявок магазина: ")
            cur.execute("UPDATE products SET shop_applications=? WHERE product_code=?", (new_apl, product_code))
        elif choice == '4':
            new_product_amount = input("Введите новое количество продукта на складе: ")
            cur.execute("UPDATE products SET product_amount=? WHERE product_code=?", (new_product_amount, product_code))
        elif choice == '6':
            new_price = float(input("Введите новую оптовую цену: "))
            cur.execute("UPDATE products SET Wholesale_price=? WHERE product_code=?", (new_price, product_code))
        else:
            print("Неверный выбор.")
            return

        con.commit()
        print("Данные о товаре успешно обновлены!")

    except ValueError:
        print("Ошибка: Введены некорректные данные.")
    finally:
        cnn.close()

# Создание базы данных при запуске скрипта
create_database()

while True:
    print("\nМеню:")
    print("1. Добавить товар")
    print("2. Поиск товара")
    print("3. Удалить товар")
    print("4. Редактировать товар")
    print("5. Выход")

    choice = input("Выберите действие: ")

    if choice == '1':
        add_product()
    elif choice == '2':
        search_products()
    elif choice == '3':
        delete_products()
    elif choice == '4':
        edit_product()
    elif choice == '5':
        break
    else:
        print("Неверный выбор. Попробуйте снова.")



from db import Purchase, PurchaseDatabase
from tabulate import tabulate

def print_purchases(purchases):
    headers = ['ID', 'Тип', 'Наименование', 'Цена за ед.', 'Количество', 'Общая сумма', 'Дата']
    table = [[p[0], p[1], p[2], p[3], p[4], p[5], p[6]] for p in purchases]
    print(tabulate(table, headers=headers, tablefmt='grid'))

def main_menu():
    db = PurchaseDatabase()
    
    while True:
        print("\n=== Система учета закупок ===")
        print("1. Добавить новую закупку")
        print("2. Показать все закупки")
        print("3. Поиск закупок")
        print("4. Обновить закупку")
        print("5. Удалить закупку")
        print("0. Выход")

        choice = input("\nВыберите действие: ")

        if choice == '1':
            print("\nДобавление новой закупки:")
            type_of_purchase = input("Тип (товар/работа/услуга): ")
            name = input("Наименование: ")
            price = float(input("Цена за единицу: "))
            quantity = float(input("Количество: "))
            
            purchase = Purchase(type_of_purchase, name, price, quantity)
            db.add_purchase(purchase)
            print("Закупка успешно добавлена!")

        elif choice == '2':
            purchases = db.get_all_purchases()
            if purchases:
                print("\nВсе закупки:")
                print_purchases(purchases)
            else:
                print("\nЗакупки отсутствуют")

        elif choice == '3':
            print("\nПоиск закупок:")
            print("1. По типу")
            print("2. По наименованию")
            print("3. По дате")
            search_choice = input("Выберите критерий поиска: ")
            
            if search_choice == '1':
                value = input("Введите тип: ")
                results = db.search_purchases('type_of_purchase', value)
            elif search_choice == '2':
                value = input("Введите наименование: ")
                results = db.search_purchases('name', value)
            elif search_choice == '3':
                value = input("Введите дату (YYYY-MM-DD): ")
                results = db.search_purchases('date', value)
            else:
                print("Неверный выбор")
                continue

            if results:
                print_purchases(results)
            else:
                print("Ничего не найдено")

        elif choice == '4':
            id = input("\nВведите ID закупки для обновления: ")
            print("Введите новые данные:")
            type_of_purchase = input("Тип (товар/работа/услуга): ")
            name = input("Наименование: ")
            price = float(input("Цена за единицу: "))
            quantity = float(input("Количество: "))
            
            purchase = Purchase(type_of_purchase, name, price, quantity)
            db.update_purchase(id, purchase)
            print("Закупка успешно обновлена!")

        elif choice == '5':
            id = input("\nВведите ID закупки для удаления: ")
            db.delete_purchase(id)
            print("Закупка успешно удалена!")

        elif choice == '0':
            print("\nДо свидания!")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main_menu() 
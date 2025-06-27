from models import Purchase, PurchaseDatabase
from tabulate import tabulate


def print_purchases(purchases):
    headers = ["ID", "Тип", "Наименование", "Цена за ед.", "Количество", "Общая сумма", "Дата"]
    table = [[p[0], p[1], p[2], p[3], p[4], p[5], p[6]] for p in purchases]
    print(tabulate(table, headers=headers, tablefmt="grid"))


def main():
    db = PurchaseDatabase()

    while True:
        print("\n\nВыберите что вас интересует:\n1. Добавить закупку\n2. Показать все закупки\n3. Поиск закупки\n4. Обновить закупку\n5. Удалить закупку\n0. Выход")

        choice = input("\nВыберите действие: ")

        if choice == '1':
            print("--- Добавление закупки ---")
            type_of_purchase = input("Тип товара(товар/услуга/работа): ")
            name = input("Наименование: ")
            try:
                price = float(input("Цена за единицу: "))
                quantity = float(input("Количество: "))
            except ValueError as ex:
                print(f"ОШИБКА --- {ex}")
                continue


            purchase = Purchase(type_of_purchase, name, price, quantity)
            db.add_purchase(purchase)
            print("Закупка успешно добавлена!")

        elif choice == '2':
            purchases = db.get_all_purchases()
            if purchases:
                print("\nВсе закупки:")
                print_purchases(purchases)
            else:
                print("\nЗакупки отсутствуют!")
        
        elif choice == '3':
            print("Поиск закупок\n1. По типу\n2. По наименованию\n3. По дате")
            search_choice = input("Выберите критерий поиска: ")


            if search_choice == '1':
                value = input("Введите тип: ")
                results = db.search_purchases("type_of_purchase", value)
            elif search_choice == '2':
                value = input("Введите наименование: ")
                results = db.search_purchases("name", value)
            elif search_choice == '3':
                value = input("Введите (YYYY-MM-DD))): ")
                results = db.search_purchases("date", value)
            else:
                print('Неверный выбор!')
                continue

            if results:
                print_purchases(results)
            else:
                print("Ничего не найдено!")
        
        elif choice == '4':
            print("--- Обновление закупки ---")
            try:
                id = int(input("Введите ID закупки для обновления: "))
            except ValueError as ex:
                print(f"ОШИБКА --- {ex}")
                continue
            type_of_purchase = input("Тип товара(товар/услуга/работа): ")
            name = input("Наименование: ")
            try:
                price = float(input("Цена за единицу: "))
                quantity = float(input("Количество: "))
            except ValueError as ex:
                print(f"ОШИБКА --- {ex}")
                continue

            purchase = Purchase(type_of_purchase, name, price, quantity)
            db.update_purchase(id, purchase)
            print("Закупка успешно обновлена!")

        elif choice == '5':
            try:
                id = int(input("Введите ID закупки для удаления: "))
            except ValueError as ex:
                print(f"ОШИБКА --- {ex}")
                continue
            db.delete_purchases(id)
            print('Закупка удалена!')

        elif choice == '0':
            print("Досвидания!")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")



if __name__ == '__main__':
    main()
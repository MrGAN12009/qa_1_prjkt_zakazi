# Система учета закупок

Консольное приложение на Python для управления базой данных закупок.

## Функциональность

- Добавление новых закупок (товаров, работ, услуг)
- Просмотр всех закупок
- Поиск закупок по различным параметрам
- Редактирование существующих закупок
- Удаление закупок

## Установка

1. Убедитесь, что у вас установлен Python 3.x
2. Установите необходимые зависимости:
```
pip install -r requirements.txt
```

## Запуск

```
python main.py
```

## Примеры запросов к API

### Получить все покупки
```bash
curl -X GET http://localhost:8888/api/purchases
```

### Получить покупку по id
```bash
curl -X GET http://localhost:8888/api/purchases/1
```

### Добавить новую покупку
```bash
curl -X POST http://localhost:8888/api/purchases \
  -H "Content-Type: application/json" \
  -d '{
    "type_of_purchase": "food",
    "name": "apple",
    "price_per_unit": 10,
    "quantity": 5,
    "date": "2024-06-01"
  }'
```

### Обновить покупку по id
```bash
curl -X PUT http://localhost:8888/api/purchases/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "banana",
    "quantity": 10
  }'
```

### Удалить покупку по id
```bash
curl -X DELETE http://localhost:8888/api/purchases/1
``` 
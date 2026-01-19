# TODO Напишите функцию для поиска индекса товара

def find_item_index(items, item_to_find):
    """
    Функция для поиска индекса первого вхождения товара в списке.

    Args:
        items: Список товаров
        item_to_find: Товар, который нужно найти

    Returns:
        Индекс первого вхождения товара или None, если товар не найден
    """
    try:
        # Используем метод index() для поиска первого вхождения
        return items.index(item_to_find)
    except ValueError:
        # Если товар не найден, возвращаем None
        return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item) # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")




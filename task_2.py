# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, delimiter=','):
    """
    Функция для поиска общих участников между двумя группами.

    Args:
        group1: Строка с участниками первой группы
        group2: Строка с участниками второй группы
        delimiter: Разделитель между фамилиями (по умолчанию запятая)

    Returns:
        Список общих участников, отсортированный в алфавитном порядке
    """
    # Разделяем строки на списки участников
    participants1 = group1.split(delimiter)
    participants2 = group2.split(delimiter)

    # Преобразуем в множества для поиска пересечения
    set1 = set(participants1)
    set2 = set(participants2)

    # Находим общих участников и возвращаем отсортированный список
    common_participants = list(set1.intersection(set2))
    common_participants.sort()

    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
# Вызываем функцию с разделителем "|"
result = find_common_participants(
    participants_first_group,
    participants_second_group,
    delimiter='|'
)

print(f"Общие участники:", result)
money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# Количество месяцев, которое можно протянуть без долгов
months = 0
current_capital = money_capital  # Начальный капитал (без зарплаты)
current_spend = spend  # Текущие траты

# Пока можем покрыть траты текущего месяца
while current_capital + salary >= current_spend:

    # Увеличиваем счетчик месяцев
    months += 1

    # В начале месяца получаем зарплату и вычитаем траты
    current_capital = current_capital + salary - current_spend

    # Увеличиваем траты на следующий месяц (кроме первого месяца)
    current_spend *= (1 + increase)

print("Количество месяцев, которое можно протянуть без долгов:", months)
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# Рассчитываем необходимую подушку безопасности
required_money = 0
current_spend = spend

for month in range(months):
    # Нехватка в текущем месяце
    deficit = current_spend - salary
    # Добавляем к общей сумме
    required_money += deficit
    # Увеличиваем траты на следующий месяц
    current_spend *= (1 + increase)

# Округляем до целого числа (математическое округление)
money_capital = round(required_money)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)

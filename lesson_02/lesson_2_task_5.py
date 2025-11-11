def month_to_season(month):
    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    else:
        return "Осень"


try:
    month = int(input("Введите номер месяца (1-12): "))
    if month < 1 or month > 12:
        raise ValueError
    print(f"Месяц {month} относится к сезону: {month_to_season(month)}")

except ValueError:
    print("Пожалуйста, введите корректный номер месяца.")

# Конвертер валют (Версия 0.1.1)

rates = {
    "USD": 90.0,
    "EUR": 98.5,
    "CNY": 12.4
}

print("Добро пожаловать в Конвертер валют v0.1.1!")

while True:
    print("\nВыберите действие:")
    print("1 - Перевести рубли в доллары (USD)")
    print("2 - Перевести рубли в евро (EUR)")
    print("3 - Перевести рубли в юани (CNY)")
    print("0 - Выход")

    choice = input("Ваш выбор: ")

    if choice == "0":
        print("Выход из программы. До свидания!")
        break
    elif choice in ("1", "2", "3"):
        try:
            rub = float(input("Введите сумму в рублях: "))
            if rub <= 0:
                print("Ошибка: сумма должна быть больше нуля!")
                continue

            if choice == "1":
                result = rub / rates["USD"]
                print("Результат:", round(result, 2), "USD")
            elif choice == "2":
                result = rub / rates["EUR"]
                print("Результат:", round(result, 2), "EUR")
            elif choice == "3":
                result = rub / rates["CNY"]
                print("Результат:", round(result, 2), "CNY")
        except ValueError:
            print("Ошибка: нужно ввести число!")
    else:
        print("Неверный пункт меню, попробуйте еще раз.")
def calculator():
    print("=== Простой калькулятор ===")
    print("Доступные операции: +, -, *, /")
    print("Для выхода введите 'exit'\n")

    while True:
        user_input = input("Введите действие (или exit): ").strip().lower()
        if user_input == 'exit':
            print("До свидания!")
            break

        num1 = float(input("Введите первое число: "))
        op = input("Введите операцию (+, -, *, /): ").strip()
        num2 = float(input("Введите второе число: "))

        if op == '+':
            res = num1 + num2
        elif op == '-':
            res = num1 - num2
        elif op == '*':
            res = num1 * num2
        elif op == '/':
            if num2 == 0:
                print("Ошибка: деление на ноль!")
                continue
            res = num1 / num2
        else:
            print("Неизвестная операция!")
            continue

        print(f"Результат: {res}\n")

if __name__ == "__main__":
    calculator()

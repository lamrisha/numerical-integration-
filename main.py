def main():
    print("Введите функцию от x используйте math")
    expr = input("f(x) = ")

    try:
        a = float(input("Введите нижний предел a: "))
        b = float(input("Введите верхний предел b: "))
        n = int(input("Введите число разбиений n: "))
    except ValueError:
        print("Ошибка ввода")
        return

    # Создаём функцию после ввода a, чтобы проверить в допустимой точке
    try:
        f = lambda x: eval(expr, {'x': x, 'math': math, 'np': np})
        test_val = f(a)  # проверяем в нижнем пределе
    except Exception as e:
        print(f"Ошибка в выражении при x={a}: {e}")
        return

    print("\nВыберите метод:")
    print("1 - Средние прямоугольники")
    print("2 - Трапеции")
    print("3 - Симпсон")
    print("4 - Трёх восьмых")
    method_choice = input("Ваш выбор (1-4): ")

    methods = {
        '1': ('rectangle', rectangle, 2),
        '2': ('trapezoib', trapezoib, 2),
        '3': ('Simpson', Simpson, 4),
        '4': ('three_eight', three_eight, 4)
    }

    if method_choice not in methods:
        print("Неверный выбор метода")
        return

    method_name, method_func, order = methods[method_choice]
    result = method_func(f, a, b, n)
    if isinstance(result, str):
        print(result)
        return

    print(f"\nПриближённое значение интеграла: {result:.10f}")

    # Оценка погрешности по Рунге
    error, richardson = runge_error(f, a, b, n, method_func, order)
    if error is not None:
        print(f"Оценка погрешности (Рунге): {error:.2e}")
        print(f"Уточнённое значение (Ричардсон): {richardson:.10f}")
    else:
        print("Не удалось оценить погрешность (слишком мало n для удвоения)")

    plot_function(f, a, b, n, method_name)

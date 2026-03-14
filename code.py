import math
import matplotlib.pyplot as plt
import numpy as np

def rectangle(f, a, b, n):
    if n <= 0:
        return 'Please, change n, n must be >= 1 '
    h = (b - a) / n
    result = 0
    for i in range(1, n+1):         
        xi = a + i * h                
        result += f(xi - h/2)          
    return h * result

def trapezoib(f, a, b, n):
    if n <= 0:                     
        return 'Please, change n,  n must be >= 1'
    h = (b - a) / n
    result = 0
    for i in range(1, n):         
        xi = a + i * h                
        result += f(xi)    
    xn = a + n * h   
    result += (f(a) + f(xn))/2
    return h * result

def Simpson(f, a, b, n):
    if n % 2 != 0:
        return 'Please, change n,  n must be % 2 == 0 '
    h = (b - a) / n
    result_even = 0
    result_uneven = 0
    for i in range(1, n):         
        xi = a + i * h  
        if i % 2 == 0:              
            result_even += f(xi)
        else:
            result_uneven += f(xi)
    xn = a + n * h 
    return h/3 * (f(a) + f(xn) + 4*result_uneven + 2*result_even)

def three_eight(f, a, b, n):
    if n % 3 != 0:                  
        return 'Please, change n, n must be multiple of 3'
    h = (b - a) / n
    m = n // 3  
    result = 0
    result += f(a) + f(b)
    sum3 = 0
    sum2 = 0
    
    for k in range(1, m + 1):
        x1 = a + (3*k - 2) * h
        x2 = a + (3*k - 1) * h
        sum3 += f(x1) + f(x2)
        if k < m:
            x3 = a + 3*k * h
            sum2 += f(x3)
    result += 3 * sum3 + 2 * sum2
    return (3 * h / 8) * result

def runge_error(f, a, b, n, method, p):
    I_h = method(f, a, b, n)
    if isinstance(I_h, str):  
        return None, None
    
    n2 = n // 2
    if n2 < 1:
        return None, None
    I_2h = method(f, a, b, n2)
    if isinstance(I_2h, str):
        return None, None
    
    error = abs(I_h - I_2h) / (2**p - 1)
    I_richardson = (2**p * I_h - I_2h) / (2**p - 1)
    return error, I_richardson


def plot_function(f, a, b, n, method_name):
    x = np.linspace(a, b, 1000)
    y = [f(xi) for xi in x]
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', linewidth=2, label='f(x)')
    
    h = (b - a) / n
    nodes = [a + i*h for i in range(n+1)]
    y_nodes = [f(xi) for xi in nodes]
    
    if method_name == 'rectangle':
        for i in range(n):
            x_left = nodes[i]
            x_right = nodes[i+1]
            x_mid = (x_left + x_right) / 2
            y_mid = f(x_mid)
            plt.fill([x_left, x_left, x_right, x_right],
                     [0, y_mid, y_mid, 0],
                     'g', alpha=0.3, edgecolor='green')
        plt.title('Метод средних прямоугольников')
    elif method_name == 'trapezoib':
        for i in range(n):
            x_left = nodes[i]
            x_right = nodes[i+1]
            y_left = f(x_left)
            y_right = f(x_right)
            plt.fill([x_left, x_left, x_right, x_right],
                     [0, y_left, y_right, 0],
                     'orange', alpha=0.3, edgecolor='orange')
        plt.title('Метод трапеций')
    else:
        plt.scatter(nodes, y_nodes, color='red', zorder=5)
        for i in range(n+1):
            plt.vlines(nodes[i], 0, y_nodes[i], colors='gray', linestyles='--', linewidth=0.8)
        plt.title(f'Метод {method_name} (разбиение на {n} частей)')
    
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

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

if __name__ == "__main__":
    main()

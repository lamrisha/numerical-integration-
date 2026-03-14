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
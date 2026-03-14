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
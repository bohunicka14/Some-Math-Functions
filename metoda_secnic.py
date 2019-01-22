import math

def compute_x(func, x0, x1):
    result = x1 - (func(x1)/((func(x1) - func(x0))/(x1-x0)))

    return result

def compute_root(func, x0, x1, epsilon):
    new_x = compute_x(func, x0, x1)
    new_y = func(new_x)

    x0 = x1
    x1 = new_x
    print('x = {}, y = {}'.format(new_x, new_y))
    while abs(new_y) > epsilon:
        new_x = compute_x(func, x0, x1)
        new_y = func(new_x)
        print('x = {}, y = {}'.format(new_x, new_y))
        x0 = x1
        x1 = new_x
        
# startovacie hodnoty
x0 = 0.5
x1 = 0

compute_root(lambda x : 2*math.sin(2*x)*math.cos(x) - x/2 - 1/2, x0, x1, 0.0001)


import math
def symetric_derivative(func, a):
    h = 1
    k = 1
    lines = 5
    #derived_func = (func(a+h) - func(a-h))/2*h
    result = []
    for i in range(lines):
        result.append([None]*lines)
        
    for j in range(0,lines):
        for i in range(j,lines):
            if j == 0:
                result[i][j] = (func(a+h) - func(a-h))/(2*h)
                h = h/2
            else:
                result[i][j] = (result[i-1][j-1] - (4**(k+j-1))*result[i][j-1])/(1-4**(k+j-1))
    
    for j in range(0,lines):
        for i in range(j,lines):
            print('F{}{} = {}'.format(i, j, result[i][j]))
    print(50*'_')

func = math.sin
symetric_derivative(func, 0)

func1 = lambda x : x/(x+2)
symetric_derivative(func1, 0)

# Name: Bailey Brumfield
# Date: 1/22/2023
# Professor: Juan Parra
# Asignment: Assignment 1

import math
import decimal
import numpy as np
# define function that converts 64-bit binary number into a floating point number, chops and rounds the number,
# and computes the absolute and relative error
def binary_to_float():
    # 1)
    # enter sign (s); 0 for positive and 1 for negative
    s = 0

    # enter exponent (c)
    exponent = 10000000111
    c, i = 0, 0

    while(exponent != 0):
        exp = exponent % 10
        c = c + exp * pow(2, i)
        exponent = exponent//10
        i += 1

    # enter fraction (f)
    fraction = str(1110101110010000000000000000000000000000000000000000)
    i = 1
    f = 0

    for item in fraction:
        f = f + int(item) * (0.5**i)
        i += 1

    # plug into formuala to convert 64-bit binary number into a floating point number
    n = ((-1)**s)*(2**(c - 1023))*((1 + f))
    print(n)
    print()
    
    number = n

    # 2)
    # chopping number at 3 decimal places
    n *= (10 ** -3)
    print((math.floor(n * 1000)) / 1000)
    print()

    # 3)
    # rounding number at 3 decimal places
    n += 0.0005
    print(round(n, ndigits = 3))
    print()

    # 4)
    # define functions that caculates absolute error
    def absolute_error(exact: float, approx: float):
        return abs(exact - approx)
    print(absolute_error(number, round(number, 0)) / 1000)

    def relative_error(exact: float, approx: float):
        return abs((absolute_error(decimal.Decimal(exact), decimal.Decimal(approx))) / decimal.Decimal(exact))
    print(relative_error(number, round(number, 0)))
    print()

    return

# 5)
# define function that finds minimum terms
def infinite_series():
    def ser(x, k: int):
        return((-1) ** k) * ((x ** k) / (k ** 3))

    minimum_error = 1e-4
    iteration_number = 1

    while(abs(ser(1, iteration_number))> minimum_error):
        iteration_number += 1
    print(iteration_number - 1)
    print()
    return

# 6)
# define function for bisection method and newton raphson method
def number_6():
    # a)
    def bisection_method(f, a, b, acc):
        if np.sign(f(a)) == np.sign(f(b)):
            raise Exception("The scalars a and b do not bound a root")
        midpoint = (a + b) / 2
        if np.abs(a - b) <= acc:
            return 0
        elif np.sign(f(a)) == np.sign(f(midpoint)):
            return bisection_method(f, midpoint, b, acc) + 1
        elif np.sign(f(b)) == np.sign(f(midpoint)):
            return bisection_method(f, a, midpoint, acc) + 1

    # b)
    def newton_raphson_method(f,df, init, acc):
        answer = f(init) / df(init)
        x = init
        counter = 1

        while(abs(answer) >= acc):
            x -= answer
            counter += 1
            answer = f(x) / df(x)
        return counter
    
    f_x = lambda x: (x **3) + (4 * (x ** 2)) - 10
    df_dx = lambda x: 3 * (x ** 2) + (8 *x)

    print(bisection_method(f_x, -4 ,7 , 0.0001))
    print()
    
    print(newton_raphson_method(f_x,df_dx, 7, 0.0001))
    print()
# questions 1-4
binary_to_float()

# question 5
infinite_series()

# question 6
number_6()
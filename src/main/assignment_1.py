# Name: Bailey Brumfield
# Date: 1/22/2023
# Professor: Juan Parra
# Asignment: Assignment 1

import math
# define function that converts 64-bit binary number into a floating point number, chops and rounds the number,
# and computes the absolute and relative error
def binary_to_decimal():
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
    print("{:.5f}".format(n))

    # 2)
    # chopping number at 3 decimal places
    n *= (10 ** -3)
    print((math.floor(n * 1000)) / 1000)

    # 3)
    # rounding number at 3 decimal places
    n += 0.0005
    print(round(n, ndigits = 3))
    return

binary_to_decimal()


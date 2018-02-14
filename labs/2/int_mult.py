"""
Greg Stewart

Your python script should take d, the number of digits, as a command line parameter.
You will need to perform r=10 runs to record the average time to multiply two d-digit 
integers in decimal using the three methods above.

For each run generate a random pair of integers x and y, that are d digits long,
by using random.randint() or similar python function from the random module. 
(You can generate d random digits, concatenate them and convert into int). Call 
Method1, Method2 and Method3 on these inputs and record their running time on each pair.

Finally, print the average time for each method over the r=10 runs.
"""
import timeit
import matplotlib.pyplot as plt
import sys
import random

def meth1(x, y):
    y_bin = "{0:b}".format(y)
    product = 0
    for i in range(len(y_bin)):
        product += (x<<i) * int(y_bin[i])
    return product

def meth2(x,y):
    if (y == 0): return 0
    z = meth2(x, y>>1)
    if (y%2 == 0):
        return z<<1
    else:
        return x + (z<<1)

def meth3(x,y):
    x_len = x.bit_length()
    y_len = y.bit_length()
    n = max(x_len, y_len)%2
    if (n == 0 or n == 1): 
        return x*y
    bin_right = 2**(n>>1) - 1
    bin_left = 0
    for i in range(0, (n>>1)):
        bin_left += 2**((n>>1)+i)
    #print('num', n)

    x_l = ((bin_left>>(n-x_len)) & x)>>(n>>1)
    x_r = bin_right&x # int(x_bin[x_len-(n>>1)], 2)
    y_l = ((bin_left>>(n-y_len))&y)>>(n>>1)
    y_r = bin_right&y # int(y_bin[y_len-(n>>1)], 2)

    P_1 = meth3(x_l, y_l)
    P_2 = meth3(x_r, y_r)
    P_3 = meth3(x_l + x_r, y_l + y_r)

    return P_1 * 2**n + (P_3 - P_1 - P_2) * 2**(n>>1) + P_2




if __name__ == "__main__":
    d = int(sys.argv[1])

    time_1 = 0
    time_2 = 0
    time_3 = 0
    for i in range(0, 10):
        x, y = 0, 0
        for j in range(0,d):
            x += random.randint(0,9) * 10**j
            y += random.randint(0,9) * 10**j
        time_1+=timeit.timeit("meth1(%d, %d)" %(x, y), setup="from __main__ import meth1", number=1)
        if (d < 300):
            time_2+=timeit.timeit("meth2(%d, %d)" %(x, y), setup="from __main__ import meth2", number=1)
        time_3+=timeit.timeit("meth3(%d, %d)" %(x, y), setup="from __main__ import meth3", number=1)

    time_1 = time_1/10.
    time_2 = time_2/10.
    time_3 = time_3/10.

    print("Method\tTime\n"+"="*20)
    print("  1   \t%.7f s" %time_1)
    print("  2   \t%.7f s" %time_2)
    print("  3   \t%.7f s" %time_3)

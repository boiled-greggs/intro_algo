import timeit
import numpy as np
import matplotlib.pyplot as plt


def fib1(n):
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    return fib1(n-1) + fib1(n-2)



def fib2(n):
    if (n == 0):
        return 0
    f = []
    f.append(0)
    f.append(1)
    for x in range(2,n+1):
        f.append(f[x-1] + f[x-2])
    return f[n]


if __name__ == "__main__":
    f = open('timetable.txt', 'w')
    n_1 = [1,5,10,15,20,25,30,35,40,41,42,43]
    times_1 = []
    """
    for n in n_1:
        times_1.append(timeit.timeit("fib1(%d)" %n, setup="from __main__ import fib1", number=1))
    f.write("="*20+"\nTimes for fib1(n)\n"+"="*20)
    for x in range(len(n_1)):
        f.write("\n%d\t%.7f s" %(n_1[x], times_1[x]))

    fig, ax = plt.subplots()
    ax.set_title('fib1(n) runtimes')
    ax.set_ylabel('time (s)')
    ax.set_xlabel('number')
    ax.plot(n_1, times_1)
    fig.savefig('fib1.pdf')
    
    n_2 = [2**10, 2**12, 2**14, 2**16, 2**18, 2**19]
    times_2 = []
    for n in n_2:
        times_2.append(timeit.timeit("fib2(%d)" %n, setup="from __main__ import fib2", number=1))
    f.write("\n"+"="*20+"\nTimes for fib2(n)\n"+"="*20)
    for x in range(len(n_2)):
        f.write("\n%d\t%.7f s" %(n_2[x], times_2[x]))
    fig2, ax2 = plt.subplots()
    ax2.set_title('fib2(n) runtimes')
    ax2.set_ylabel('time (s)')
    ax2.set_xlabel('number')
    ax2.plot(n_2, times_2)
    fig2.savefig('fib2.pdf')
    """
    times_3 = []
    for n in n_1:
        times_3.append(timeit.timeit("fib2(%d)" %n, setup="from __main__ import fib2", number=1))
    fig3, ax3 = plt.subplots()
    ax3.set_title('fib2(n) runtimes')
    ax3.set_ylabel('time (s)')
    ax3.set_xlabel('n')
    ax3.plot(n_1,times_3)
    fig3.savefig('fib2small.pdf')

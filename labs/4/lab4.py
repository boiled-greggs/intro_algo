import numpy as np
import sys


def selection(array, n, k):
    rl = []
    rv = []
    rr = []
    v = np.random.randint(n)
    while (True):
        for i in range(len(array)):
            if array[i] > v:
                rr.append(array[i])
            elif array[i] < v:
                rl.append(array[i])
            else:
                rv.append(array[i])
        if k <= len(rl):
            array = rl
            print(len(rl))
            if v != 0: v = np.random.randint(0, v) 
            else: v = 0
            rl = []
            rv = []
            rr = []
        elif k > (len(rl) + len(rv)):
            array = rr
            v = np.random.randint(v, high=n)
            k = k - len(rl) - len(rv)
            rl = []
            rv = []
            rr = []
        else:
            return v #found = True


if __name__ == "__main__":
    n = int(sys.argv[1])
    k = int(sys.argv[2])

    rarray = np.random.randint(n,size=n)
    sorted_a = np.sort(rarray)

    kth = selection(rarray, n, k)

    print("Random Array:", rarray)
    print("Sorted Array:",sorted_a)
    print("The %d-th element:"%k, kth)

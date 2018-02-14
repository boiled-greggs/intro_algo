import random
import numpy as np
def modexp(x, y, N):
    if (y == 0): 
        return 1
    z = modexp(x, abs(y/2), N)
    if (not y%2):
        return (z*z)%N
    else:
        return (x*z**2)%N

def primality(N, k):
    randints = []
    for i in range(0,k):
        randints.append(random.randint(1,N-1))
    prime = True
    for i in range(0,k):
        if 1 != modexp(randints[i],1-N,N):
            return False
            break
    return True 



if __name__ == "__main__":
    ans = modexp(1,1,63)

    k=1000
    Ns = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973, 75361, 101101, 115921, 126217, 162401, 172081, 188461, 252601, 278545, 294409, 314821, 334153, 340561, 399001, 410041, 449065, 488881]
    no_primes = np.zeros(32)
    
    for i in range(0,32):
        for j in range(0,k):
            prime = primality(Ns[i],1)
            if (prime): no_primes[i] += 1

    for i in range(0,32):
        no_primes[i] = no_primes[i]/1000.

    print("Probabilities of Not Working\n"+"="*25)
    print("Number\t\tProbability\n"+"-"*25)
    for i in range(0,32):
        print("%d\t\t%.5f" %(Ns[i], no_primes[i]))
    
























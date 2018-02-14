def calculate_factorial_prime_decompose(number):

    prime = [True]*(number + 1)
    result = 1
    for i in range (2, number+1):
        if prime[i]:
            #update prime table
            j = i+i
            while j <= number:
                prime[j] = False
                j += i
            sum = 0
            t = i
            while t <= number:
                sum += number/t
                t *= i
            result *= i**sum
    return result

print(calculate_factorial_prime_decompose(5))

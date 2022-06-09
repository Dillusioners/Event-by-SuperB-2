def isPrime(n):
    c = 0
    for i in range(1, n + 1):
        if n % i == 0:
            c += 1

    return c == 2

n = int(input("Enter the number: "))

if n<= 9 or n>=50:
    print("Invalid Input")
elif n%2 != 0:
    print("Invalid Input")
else:
    a = 3
    b = 0
    if n / 2 >= a:
        b = n - a
        if isPrime(a) and isPrime(b):
            print(f'{a} and {b} are the Goldbach Numbers')
        else:
            print(f'{n} does not have the Goldbach Numbers')
        a = a+2

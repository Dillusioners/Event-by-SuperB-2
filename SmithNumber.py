num = int(input("Enter your number: "))
if num == 2 or num % 2 != 0:
    print("Number is not a Smiths Number")
num2 = str(num)
sum = 0
jog = 0
bokachuda = 0
for i in range(len(num2)):
    jog=jog + num % 10
    num = num // 10
c = 2
primes = []
while(num>1):
            if num%c == 0:
                primes.append(c)
                num/=c
            else:
                c+=1
                continue
for n in range(len(primes)-1):
    bokachuda = bokachuda + int(primes[n])

if sum == bokachuda:
    print("Your number is a Smiths number")
else:
    print("Nikal Laude")
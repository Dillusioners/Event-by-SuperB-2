num = int(input("Enter your number"))
num2 = ""
c = 0
i = 0
while num >= 1:
    num2 = num2 + str(num % 2)
    num = num // 2 
    num_check = list(num2)
for i in range(len(num_check)):
    if '1' in num2[i]:
        c += 1
    
if c % 2 ==0:
    print("Number is Evil :(")
else:
    print("Number is not Evil :)")

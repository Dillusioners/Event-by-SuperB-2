num = int(input("Enter your number"))
if num < 100:
    print ("Number is not a fascinating number")
value = str(num) + str(num * 2) + str(num * 3)
value = list(value)
if '1' in value and '2' in value and '3' in value and '4' in value and '5'in value and '6' in value and '7' in value and '8' in value and '9' in value:
    print("Your number is a Fascinating number")
else:
    print("Your number is not a Fascinating number")
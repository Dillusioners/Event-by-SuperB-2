number = int(input("Enter a number: "))
if number > 100:
    digits = list(str(number))
    length = len(digits)
    inc = True
    dec = True
    prev = number % 10
    while number != 0:
        d = number % 10
        if d > prev:
            break
        prev = d
        number = number // 10

    while number != 0:
        d = number % 10
        inc = False
        if d < prev:
            dec = False
            break
        prev = d
        number = number // 10

    if inc and dec:
        print("Bouncy")
    else:
        print("Not bouncy")
else:
    print("Not a Bouncy Number")
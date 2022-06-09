number = int(input("Enter a number: "))
digits = list(str(number))
length = len(digits)
ok1 = True
ok2 = True
ok3 = True
ok4 = True
ok5 = True
ok6 = True
ok7 = True
ok8 = True
ok9 = True
ok0 = True

if digits.count("0") > 0:
    ok0 = True
    if digits.count("0") > 1:
        ok0 = False
if digits.count("1") > 0:
    ok1 = True
    if digits.count("1") > 1:
        ok1 = False
if digits.count("2") > 0:
    ok2 = True
    if digits.count("2") > 1:
        ok2 = False
if digits.count("3") > 0:
    ok3 = True
    if digits.count("3") > 1:
        ok3 = False
if digits.count("4") > 0:
    ok4 = True
    if digits.count("4") > 1:
        ok4 = False
if digits.count("5") > 0:
    ok5 = True
    if digits.count("5") > 1:
        ok5 = False
if digits.count("6") > 0:
    ok6 = True
    if digits.count("6") > 1:
        ok6 = False
if digits.count("7") > 0:
    ok7 = True
    if digits.count("7") > 1:
        ok7 = False
if digits.count("8") > 0:
    ok8 = True
    if digits.count("8") > 1:
        ok8 = False
if digits.count("9") > 0:
    ok9 = True
    if digits.count("9") > 1:
        ok9 = False

if ok1 and ok2 and ok3 and ok4 and ok5 and ok6 and ok7 and ok8 and ok9:
    print(f'{number} is a Unique Number')
else:
    print(f'{number} is a not a Unique Number')
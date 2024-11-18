a = input('first num: ')
b = input('second num: ')
c = input('third num: ')

if a == b == c:
    print(3)

elif a == b != c or a != b == c:
    print(2)

else:
    print(0)


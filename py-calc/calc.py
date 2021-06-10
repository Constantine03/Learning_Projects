# title

title = "Smart Calc"
print("Hello! I am a " + title)

o = input('Enter operation: ')
if o not in('+','-','*','/','//','%','**'):
    print('Error! Unknown operation!')
else:
    a = int(input('a = '))
    b = int(input('b = '))

    if o == '+':
        print('a + b = ', a + b)
    elif o == '-':
        print('a - b = ', a - b)
    elif o == '*':
        print('a * b = ', a * b)
    elif o == '/':
        if b == 0:
            print('Error! Division by 0!')
        else:
            print('a / b = ', a / b)
    elif o == '//':
        if b == 0:
            print('Error! Division by 0!')
        else:
            print('a // b = ', a // b)
    elif o == '%':
        if b == 0:
            print('Error! Division by 0!')
        else:
            print('a % b = ', a % b)
    else: # o == '**'
        print('a ** b = ', a ** b)



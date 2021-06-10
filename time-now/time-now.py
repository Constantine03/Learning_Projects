n = int(input('Enter n - the number of minutes passed: '))
n_short = n % 1440 # n_short - number of minutes converted to the range 0..1439
if n < 0:
    answer = input('n < 0. Are you sure you want to travel into past? (y/n): ')
    if answer == 'n':
        print('Wise choice. Shutting down.')
    elif answer not in ('n','y'):
        print('Unknown command. Shutting down')
    else:
        print('It is ',n_short // 60,":",n_short % 60,' on the clock')
else:
    print('It is ',n_short // 60,":",n_short % 60,' on the clock')
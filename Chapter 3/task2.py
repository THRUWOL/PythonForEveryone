hours = input('Enter Hours: ')

try:
    hours = int(hours)
except:
    hours = -1
    print('Error, please enter numeric input')

rate = input('Enter Rate: ')

try:
    rate = float(rate)
except:
    rate = -1
    print('Error, please enter numeric input')

if hours != -1 and rate != -1:
    if hours > 40:
        upwork = (hours % 40) * 1.5
        pay = (rate * 40) + (rate * upwork)
        print('Pay: ', pay)
    else:
        pay = hours * rate
        print('Pay: ', pay)
elif hours == -1:
    print('Hours not a number')
elif rate == -1:
    print('Rate not a number')

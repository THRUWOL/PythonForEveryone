hours = input('Enter Hours: ')
hours = int(hours)
rate = input('Enter Rate: ')
rate = float(rate)

if hours > 40:
    upwork = (hours % 40) * 1.5
    pay = (rate * 40) + (rate * upwork)
    print('Pay: ', pay)
else:
    pay = hours * rate
    print('Pay: ', pay)

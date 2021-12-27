counter = 0
amount = 0
min = None
max = None

while True:
    number = input("Enter a number: ")

    try:
        number = int(number)
    except:
        if number == 'done':
            break
        else:
            print("Invalid input")
            continue

    amount += number
    counter += 1

    if min is None or min > number:
        min = number
    elif max is None or max < number:
        max = number

print(amount, counter, max, min)

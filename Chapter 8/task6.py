numbers = list()
while True:
    number = input("Enter a number: ")

    try:
        number = float(number)
        numbers.append(number)
    except:
        if number == 'done':
            print(f'Maximum: {max(numbers)}\n'
                  f'Minimum: {min(numbers)}')
            break
        else:
            print("Invalid input")
            continue

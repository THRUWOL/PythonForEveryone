counter = 0
amount = 0
average = 0

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
    average = amount / counter

print(amount, counter, average)

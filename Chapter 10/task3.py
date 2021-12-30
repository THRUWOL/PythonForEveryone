def openFile(file):
    try:
        return open(file)
    except:
        print("Cannot open the file: ", file)
        quit()


def alphabetsLowercase(alphabet):
    for i in range(97, 123):
        alphabet.append(chr(i))
    return alphabet


file = input("Enter a file name: ")
messages = dict()
lst = list()
sum = 0

alphabet = list()
alphabet = alphabetsLowercase(alphabet)

for line in openFile(file):
    letters = [char for char in line.lower()]
    for letter in letters:
        if letter in alphabet:
            messages[letter] = messages.get(letter, 0) +1

for key, val in sorted(list(messages.items())): sum += val

for key, val in sorted(list(messages.items())):
    print(f'{key} | {val} | {round(val/sum * 100,3)} %')

print(f'Total: {sum}')

import re


def openFile(file):
    try:
        return open(file)
    except:
        print("Cannot open the file: ", file)
        quit()


fileName = input('Enter file: ')
ofile = openFile(fileName)

counter = 0
numbers = 0
averageOfNumber = 0

for line in ofile:
    findedLine =re.findall('^New Revision: [0-9]+', line)
    if len(findedLine) != 0:
        counter += 1
        numbers += float(str(findedLine[0]).split(':')[1])

averageOfNumber = numbers / counter
print(averageOfNumber)

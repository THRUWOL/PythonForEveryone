def openFile(file):
    try:
        oFile = open(file)
        return oFile
    except:
        print('Cannot open the file: ', file)
        quit()


def findMaxMessage(dictionaries, bigWord, bigCount):
    for word, count in dictionaries.items():
        if bigWord is None or count > bigCount:
            bigWord = word
            bigCount = count
    print(bigWord, bigCount)


file = input('Enter a file name: ')
oFile = openFile(file)
counts = dict()

bigWord = None
bigCount = None

for line in oFile:
    if 'From' in line and len(line.split()) > 2:
        counts[line.split()[1]] = counts.get(line.split()[1], 0) +1
findMaxMessage(counts, bigWord, bigCount)

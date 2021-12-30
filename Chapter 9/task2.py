def openFile(file):
    try:
        oFile = open(file)
        return oFile
    except:
        print('Cannot open the file: ', file)
        quit()


file = input('Enter a file name: ')
oFile = openFile(file)
counts = dict()

for line in oFile:
    if 'From' in line and len(line.split()) > 3:
        words = line.split()[2]
        counts[words] = counts.get(words, 0)+1
print(counts)

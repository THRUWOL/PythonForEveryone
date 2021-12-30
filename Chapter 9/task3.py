def openFile(file):
    try:
        oFile = open(file)
        return oFile
    except:
        print('Cannot open the file: ', file)


file = input('Enter a file name: ')
oFile = openFile(file)
counts = dict()

for line in oFile:
    if 'From' in line and len(line.split()) > 2:
        counts[line.split()[1]] = counts.get(line.split()[1], 0) +1
print(counts)

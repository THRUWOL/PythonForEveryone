def openFile(file):
    try:
        oFile = open(file)
        return oFile
    except:
        print('File cannot be opened: ', file)
        quit()


file = input('Enter file: ')

oFile = openFile(file)
concatLine = list()

for line in oFile:
    sLine = line.split()
    concatLine += sLine

sumLine = list(set(concatLine))
print(sorted(sumLine))

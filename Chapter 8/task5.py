def openFile(file):
    try:
        oFile = open(file)
        return oFile
    except:
        print('File cannot be opened: ', file)
        quit()


def findMail(count, oFile):
    for line in oFile:
        if 'From' in line:
            if line.split()[0] == 'From':
                count += 1
            line = line.split()[1]
            print(line)
    return count


file = input('Enter file: ')
count = 0

oFile = openFile(file)

count = findMail(count, oFile)
print(f'There were {count} lines in the file with From as the first word')

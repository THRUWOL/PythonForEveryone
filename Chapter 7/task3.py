def openFile(file):
    easterEgg(file)
    try:
        oFile = open(file)
        return oFile
    except:
        print('File cannot be opened: ', file)
        quit()


def easterEgg(file):
    if file.lower() == "na na boo boo":
        print('NA NA BOO BOO TO YOU - You have been punk\'d!')
        quit()


file = input('Enter the file name: ')
linesCount = 0

oFile = openFile(file)

for line in oFile:
    if 'Subject:' in line:
        linesCount += 1

print(linesCount)

def openFile(file):
    try:
        oFile = open(file)
        return oFile
    except:
        print('Can\'t find the file: ', file)
        quit()


file = input('Enter the file name: ')
startString = 'X-DSPAM-Confidence:'
count = 0
summary = 0
average = 0

oFile = openFile(file)

for list in oFile:
    if startString in list:
        count += 1
        number = float(list[list.find(':')+1:])
        summary += number

average = summary/count
print('Average spam confidence: ', average)

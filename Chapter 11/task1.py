import re


def openFile(file):
    try:
        return open(file)
    except:
        print("Cannot open the file: ", file)
        quit()


file = input("Enter the file: ")
oFile = openFile(file)
regularExpression = input("Enter a regular expression: ")
regularCounter = 0

for line in oFile:
    try:
        if len(re.findall(regularExpression, line)) != 0: regularCounter +=1
    except: pass

print(f'{file} had {regularCounter} lines that matched {regularExpression}')

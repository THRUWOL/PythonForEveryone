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

bigWord = None
bigCount = None

for line in oFile:
    if 'From' in line and len(line.split()) > 2:
        try: domain = line.split()[1].split('@')[1]
        except: pass
        counts[domain] = counts.get(domain, 0) + 1
print(counts)

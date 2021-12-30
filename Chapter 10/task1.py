def openFile(file):
    try:
        return open(file)
    except:
        print("Cannot open the file: ", file)
        quit()


file = input("Enter a file name: ")
messages = dict()
lst = list()

for line in openFile(file):
    if 'From' in line and len(line.split()) > 2:
        messages[line.split()[1]] = messages.get(line.split()[1], 0) +1

for key,val in messages.items():
    lst.append((val,key))

for key, val in list(dict(sorted(lst, reverse=True)[:1]).items()):
    print(val, key)

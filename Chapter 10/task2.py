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
    if 'From' in line:
        try:
            day = line.split()[5].split(':')[0]
            messages[day]= messages.get(day, 0) +1
        except: pass

for key, val in sorted(list(messages.items())):
    print(key, val)

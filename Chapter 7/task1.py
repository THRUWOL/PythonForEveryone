while True:
    try:
        file = input('Enter a file name: ')
        ofile = open(file)

        for line in ofile:
            print(line.rstrip().upper())
        break
    except:
        print('Can\'t find the file')

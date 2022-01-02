import socket


def getSocket(url):
    try:
        sock = str(url).split('/')[2]
        return sock
    except:
        print('Cannot read this url: ', url)
        quit()


# http://data.pr4e.org/romeo.txt

url = input('Enter the url: ')
sock = getSocket(url)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((sock, 80))

cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

counterAllChar = 0

while True:
    data = mysock.recv(1)
    counterAllChar += 1
    if len(data) < 1 or counterAllChar == 3000:
        break
    print(data.decode(),end='')
mysock.close()

print(f'\n{counterAllChar}')

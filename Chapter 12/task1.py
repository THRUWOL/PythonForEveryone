import socket


def getSocket(url):
    try:
        sock = str(url).split('/')[2]
        return sock
    except:
        print('Cannot read this url: ', url)
        quit()


url = input('Enter the url: ')
sock = getSocket(url)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((sock, 80))

cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()

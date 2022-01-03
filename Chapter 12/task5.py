import socket


def getSocket(url):
    try:
        sock = str(url).split('/')[2]
        return sock
    except:
        print('Cannot read this url: ', url)
        quit()


# http://data.pr4e.org/romeo.txt
# http://data.pr4e.org/romeo-full.txt

url = input('Enter the url: ')
sock = getSocket(url)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((sock, 80))

cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

data = mysock.recv(512)
message = data.decode()
header_end_pos = message.find('\r\n\r\n') + 4

print(message[header_end_pos:], end='')
while True:
    data = mysock.recv(512)
    if not data:
        break
    print(data.decode())
mysock.close()

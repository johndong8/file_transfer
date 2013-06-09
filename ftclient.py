import socket

HOST = '127.0.0.1'
PORT = 9050

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

s.connect((HOST, PORT))

while 1:
    filename = raw_input('list or get <filename>: ')
    s.sendall(filename)
    data = s.recv(1024)
    if not data: break
    else:
        print data



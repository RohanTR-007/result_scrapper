import socket
import struct

s = socket.socket()
s.bind(("localhost", 8100))
s.listen(3)

print('Waiting for connections')
while True:
    c, addr = s.accept()
    print(f'Connected with {c} with address {addr}')

    # Receive file size
    f_size_data = c.recv(8)
    # Unpack the 8-byte representation
    f_size = struct.unpack('!Q', f_size_data)[0]
    print("File size:", f_size)

    # Receive file data
    file_path = 'C:/Users/ROHAN/mypython/client-server/recv.png'
    with open(file_path, 'wb') as f:
        total_received = 0
        while total_received < f_size:
            data = c.recv(4096)
            total_received += len(data)
            f.write(data)
            print(f'Received {total_received} bytes')

    print("File received successfully.")

    # Prompt for captcha input
    captcha = input("Enter captcha: ")
    c.send(captcha.encode())

    c.close()
    print('Do u wanna exit ?')
    x=input('enter y or n')
    if(x == "y"):
        break
s.close()

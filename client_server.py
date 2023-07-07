import socket
import os
import struct


def client():
    c = socket.socket()
    c.connect(("localhost", 8100))
    # 10.100.17.65
    # "100.68.194.73", 40488
    file_path = 'captcha_src.png'

    # Send file size
    f_size = os.path.getsize(file_path)
    # Convert file size to 8-byte representation
    f_size_data = struct.pack('!Q', f_size)
    c.sendall(f_size_data)

    # Send file data
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            c.sendall(data)

    # Receive captcha response
    captcha_recv = c.recv(4096).decode()
    print(f'Captcha response: {captcha_recv}')
    c.close()
    return captcha_recv


def server():
    s = socket.socket()
    s.bind(("localhost", 8100))
    s.listen(3)

    print('Waiting for connections')

    # Flag to indicate if the server should continue running
    running = True

    while running:
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

        print("File received successfully.")

        # Prompt for captcha input
        captcha = input("Enter captcha: ")
        c.send(captcha.encode())

        c.close()

        # Check if the termination condition is met
        print('Do u wanna exit ?')
        x = input('enter y or n :')
        if (x == "y"):
            break


    s.close()
    

# Call the functions
# client()
# server()

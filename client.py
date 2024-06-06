import socket


HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f'Connected to server at {HOST}:{PORT}')
    while True:
        message = input("Enter message: ")
        if message.lower() == 'exit':
            break
        s.sendall(message.encode())
        data = s.recv(1024)
        print(f"Received echo: {data.decode()}")
import socket
import threading


HOST = '127.0.0.1'
PORT = 65432

def handle_client(conn, addr):
    print(f'Connected by {addr}')
    with open('chat_log.txt', 'a') as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode()
            print(f"Received: {message}")
            f.write(f"{addr}: {message}\n")
            if message.strip().lower() == "hello":
                response = "Hello, we will answer soon"
                conn.sendall(response.encode())
                print(f"Sent: {response}")
                f.write(f"Server: {response}\n")
            else:
                conn.sendall(data)
    conn.close()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f'Server listening on {HOST}:{PORT}')
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
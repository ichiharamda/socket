import socket

def start_server():
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind(('', 4200))
    s.listen(1)
    print("Server is listening on port 4200...")

    while True:
        try:
            conn, addr = s.accept()
            print('Connected to:', addr)

            data = conn.recv(1024)
            if not data:
                print('There was no data Closing the connection!')
            else:
                conn.send(data)
                print('Received and sent back:', data)

        except Exception as e:
            print('An error occurred:', e)
        finally:
            conn.close()

if __name__ == "__main__":
    start_server()
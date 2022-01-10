import socket
import selectors


# файловый дескриптор - это номер файла в системе

def server():
    server_socket = socket.socket()
    server_socket.bind(('localhost', 9090))
    server_socket.listen()
    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_socket)


def accept_socket(server_socket):
    client_socket, addr = server_socket.accept()
    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_message)
    print(f'connected: {addr}')


def send_message(socket):
    data = socket.recv(1024)
    if data:
        socket.send(data)
    else:
        socket.close()


def event_loop():
    server()

    while True:
        select = selector.select() # return (key, events)

        for SelectorKey, events  in select:

            callback = SelectorKey.data
            callback(SelectorKey.fileobj)




if __name__ == '__main__':
    selector = selectors.DefaultSelector()
    event_loop()
import socket
from select import select

server_socket = socket.socket()
server_socket.bind(('localhost', 9090))
server_socket.listen()
to_monitor = []
# файловый дескриптор - это номер файла в системе. любой объект с методом fileno() имеет этот номер - может быть отмониторен




def accept_socket(server_socket):
    client_socket, addr = server_socket.accept()
    print(f'connected: {addr}')
    to_monitor.append(client_socket)

def send_message(socket):
    data = socket.recv(1024)
    if data:
        socket.send(data)
    else:
        socket.close()


def event_loop():
    while True:
        ready_to_read, _, _ = select(to_monitor, [], []) # read, write, errros
        print(ready_to_read)
        for socket in ready_to_read: # Если в этом списке появляется серверный сокет, значит к нему кто то пытается подрубится. Тогда ты понимаешь что пора ловить новый коннект
            if socket is server_socket:
                accept_socket(server_socket)
            else:
                send_message(socket)




if __name__ == '__main__':
    to_monitor.append(server_socket)
    event_loop()
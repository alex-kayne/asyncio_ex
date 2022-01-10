import socket
from select import select


def accept_connect():
    server_socket = socket.socket()
    server_socket.bind(('localhost', 9090))
    server_socket.listen()
    while True:
        yield ('read', server_socket)
        client_socket, addr = server_socket.accept()
        tasks.append(recv_and_send(client_socket))

def recv_and_send(client_socket):
    while True:
        yield ('read', client_socket)
        data = client_socket.recv(1024)
        yield ('write', client_socket)
        client_socket.send(data)

def event_loop():

    while any([tasks, to_read, to_write]):
        while not tasks:
            print(f'1: {tasks}')
            ready_to_read, ready_to_write, _ = select(to_read, to_write, []) # vernet socket, t.k iteriruetsy po kluchu slovary
            for sock in ready_to_read:
                tasks.append(to_read.pop(sock)) # должен вовзращать функцию
            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))

        try:
            print(f'2: {tasks}')
            task = tasks.pop(0)
            reason, sock = next(task)
            if reason == 'read':
                to_read[sock] = task
            if reason == 'write':
                to_write[sock] = task
        except StopIteration:
            print('We are done here')



to_read = {}
to_write = {}
tasks = []
tasks.append(accept_connect())
event_loop()
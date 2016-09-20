import socket
import logging

import server_logger

class TCPServer(object):
    BUFFER_SIZE = 1024
    HOST = '127.0.0.1'
    PORT = 5000

    def __init__(self):
        pass

    def handle_data(self, data):
        raise NotImplementedError

    def accept_client(self):
        logger.info('Waiting...')
        connection, address = self.server_socket.accept()
        logger.info('Connection from {}'.format(address))
        return connection, address

    def process_data(self, connection):
        buff = ''
        while True:
            buff += connection.recv(self.BUFFER_SIZE)
            if not buff:
                logger.info('Close connection')
                break

            response = self.handle_data(buff)
            if response:
                logger.info('response: "{}"'.format(response))
                connection.send(response)
                connection.close()
                break

    def listen_port(self):
        self.server_socket = socket.socket()
        #self.server_socket.setblocking(0)
        self.server_socket.bind((self.HOST, self.PORT))
        self.server_socket.listen(1)


    def run(self):
        self.listen_port()
        while True:
            new_connection, address = self.accept_client()
            self.process_data(new_connection)

logger = server_logger.init_logger()

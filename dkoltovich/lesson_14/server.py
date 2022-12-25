import os
import socket
from dotenv import load_dotenv
from db import connector
from repository import UserRepo
import json
load_dotenv()


class Server:
    """
    Class represents server
    """

    def __init__(self):
        self.sock = socket.socket()
        self.sock.bind((os.getenv('SOCKET_HOST'), int(os.getenv('SOCKET_PORT'))))
        self.sock.listen(1)
        self.conn, self.address = self.sock.accept()
        self.user_repo = UserRepo(next(connector))

    def run(self):
        """
        Main method that represents server performance
        Returns: None
        """
        try:
            while True:
                try:
                    data = self.conn.recv(1024).decode()
                    if not data:
                        break
                    data_dict = json.loads(data)
                    self.process_operation(data_dict)
                except Exception as e:
                    response = str(e)
                    self.conn.send(response.encode())
                    continue
                self.conn.send('Ok'.encode())
        finally:
            self.conn.close()

    def process_operation(self, data: dict):
        """
        Process client's operation
        Args:
            data: dictionary with user's values

        Returns: None

        """
        match data.get('operation'):
            case 1: self.user_repo.create(data)
            case 2: self.user_repo.edit(data)
            case 3: self.user_repo.delete(data)


Server().run()

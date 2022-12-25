import os
import socket
import json
from dotenv import load_dotenv
load_dotenv()


class Client:
    """
    Class represents client
    """
    def __init__(self):
        self.sock = socket.socket()
        self.sock.connect(('', int(os.getenv('SOCKET_PORT'))))

    def run(self):
        """
        Main method that represents client performance
        Returns: None
        """
        try:
            while True:
                match self.operation_request():
                    case 1: serialized = self.add_request()
                    case 2: serialized = self.edit_request()
                    case 3: serialized = self.delete_request()
                self.sock.send(serialized.encode())
                print(self.sock.recv(1024))

        finally:
            self.sock.close()

    @staticmethod
    def add_request():
        """
        Method calls when client want to add user
        Returns: Serialized data as JSON formatted str.

        """
        username = input('Enter username\n')
        first_name, last_name = input('Enter user\'s fullname:\n').split()
        data = {'operation': 1, 'username': username, 'first_name': first_name, 'last_name': last_name}
        return json.dumps(data)

    @staticmethod
    def edit_request():
        """
        Method calls when client want to edit user
        Returns: Serialized data as JSON formatted str.

        """
        username = input('Enter username that you want to edit\n')
        fields_to_change = input('What fields you want to edit (username, first_name or last_name)\n').split()
        new_values = input('Enter new values (in order with fields)\n').split()
        data = {field: value for field, value in zip(fields_to_change, new_values)}
        data.update({'old_username': username, 'operation': 2})
        return json.dumps(data)

    @staticmethod
    def delete_request():
        """
        Method calls when client want to delete user
        Returns: Serialized data as JSON formatted str.

        """
        username = input('Enter username that you want to delete\n')
        data = {'operation': 3, 'username': username}
        return json.dumps(data)

    @staticmethod
    def operation_request():
        """
        Interact with user to choose operation
        Returns: 1 when operation is 'add', 2 when operation is 'edit', 3 when operation is 'delete'

        """
        print('Enter "1" to add user', 'Enter "2" to edit user', 'Enter "3" to delete user', sep='\n')
        try:
            choice = int(input())
            if not 1 <= choice <= 3:
                raise ValueError
            return choice
        except ValueError:
            print('Invalid input')
            Client.operation_request()


Client().run()

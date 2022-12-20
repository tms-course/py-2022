from PyQt6.QtWidgets import (
    QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
    QHBoxLayout, QVBoxLayout, QMainWindow, QTextEdit)
from PyQt6.QtCore import Qt, QSize
from PyQt6 import QtWidgets, uic
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
        self.hist_pane = QWidget()
        self.msg_box = QTextEdit()
        self.msg_box.keyPressed.connect(self.msg_box_key_pressed)
        self.msg_box.setFixedHeight(80)
        self.main_widget = QWidget()                 # Widget that contains the collection of Vertical Box
        self.hist_pane_layout = QVBoxLayout()
        self.main_layout = QVBoxLayout()             # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
        self.main_layout.addWidget(self.scroll)
        self.main_layout.addWidget(self.msg_box)
        
        for i in range(1,50):
            object = QLabel("TextLabel")
            self.hist_pane_layout.addWidget(object)

        self.hist_pane.setLayout(self.hist_pane_layout)
        self.main_widget.setLayout(self.main_layout)

        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.hist_pane)

        self.setCentralWidget(self.main_widget)

        self.setGeometry(600, 100, 740, 580)
        self.setWindowTitle('Scroll Area Demonstration')
        self.show()

        return

    def msg_box_key_pressed(self, e):
        print(e)

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

# import socket

# host = socket.gethostname()
# port = 2000

# client_socket = socket.socket()
# client_socket.connect((host, port))

# message = input(" -> ")

# while message.lower().strip() != 'bye':
#     client_socket.send(message.encode())
#     data = client_socket.recv(1024).decode()

#     print('Received from server: ' + data)

#     message = input(" -> ")

# client_socket.close() 

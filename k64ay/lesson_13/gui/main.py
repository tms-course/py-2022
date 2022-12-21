import sys

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QSizePolicy,
    QVBoxLayout, QWidget, QLabel, QScrollArea
)
from PyQt6.QtGui import QKeyEvent


class Textarea(QTextEdit):
    messageSubmit = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()

    def keyPressEvent(self, event: QKeyEvent):
        if event.modifiers() & Qt.KeyboardModifier.ControlModifier \
                and event.key() == Qt.Key.Key_Return:
            self.messageSubmit.emit(self.toPlainText())
            self.clear()
            event.accept()

        super().keyPressEvent(event)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(640, 480)

        self.chat_pane_layout = QVBoxLayout()
        self.chat_pane = QWidget()
        self.chat_pane.setLayout(self.chat_pane_layout)

        self.textarea = Textarea()
        self.textarea.messageSubmit.connect(self.on_message_submit)
        self.textarea.setFixedHeight(80)

        self.scroll = QScrollArea()

        layout = QVBoxLayout()
        layout.addWidget(self.scroll)
        layout.addWidget(self.textarea)

        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.chat_pane)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def on_message_submit(self, text: str):
        label = QLabel(f"<strong>Alex</strong><div>{text}</div>")
        label.setStyleSheet("QLabel { background-color : red; color : blue; }")
        label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        label.setWordWrap(True)
        self.chat_pane_layout.addWidget(label)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
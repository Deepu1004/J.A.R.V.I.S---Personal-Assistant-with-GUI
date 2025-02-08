from PyQt5.QtWidgets import QWidget, QPushButton, QTextEdit, QVBoxLayout, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class Ui_Assistant:
    def setupUi(self, Assistant):
        Assistant.setWindowTitle("Voice Assistant")
        Assistant.resize(700, 500)
        Assistant.setStyleSheet("background-color: #f5f5f5;")  # Light background color

        self.centralwidget = QWidget(Assistant)
        Assistant.setCentralWidget(self.centralwidget)

        self.layout = QVBoxLayout(self.centralwidget)

        # Output Text Box
        self.output = QTextEdit(self.centralwidget)
        self.output.setReadOnly(True)  # Make it read-only
        self.output.setFont(QFont("Arial", 14))
        self.output.setStyleSheet("""
            QTextEdit {
                background-color: #ffffff;
                color: #333333;
                border: 2px solid #cccccc;
                border-radius: 10px;
                padding: 10px;
            }
        """)
        self.layout.addWidget(self.output)

        # Input Bar
        self.input_bar = QLineEdit(self.centralwidget)
        self.input_bar.setPlaceholderText("Type your command here...")
        self.input_bar.setFont(QFont("Arial", 14))
        self.input_bar.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                color: #333333;
                border: 2px solid #cccccc;
                border-radius: 10px;
                padding: 10px;
                margin-top: 10px;
                font-size: 14px;
            }
        """)
        self.layout.addWidget(self.input_bar)

        # Activate/Deactivate Button
        self.activate_button = QPushButton("Activate", self.centralwidget)
        self.activate_button.setFont(QFont("Arial", 16, QFont.Bold))
        self.activate_button.setFixedSize(100, 100)  # Spherical dimensions
        self.activate_button.setStyleSheet(self.activate_button_style())
        self.layout.addWidget(self.activate_button, alignment=Qt.AlignCenter)

    @staticmethod
    def activate_button_style():
        return """
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 50px;  /* Fully rounded corners for a sphere */
                font-size: 18px;
            }
            QPushButton:pressed {
                background-color: #45a049;
            }
        """

    @staticmethod
    def deactivate_button_style():
        return """
            QPushButton {
                background-color: #f44336;
                color: white;
                border: none;
                border-radius: 50px;  /* Fully rounded corners for a sphere */
                font-size: 18px;
            }
            QPushButton:pressed {
                background-color: #d32f2f;
            }
        """

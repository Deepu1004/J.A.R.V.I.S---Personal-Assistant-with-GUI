import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QThread, pyqtSignal
from datetime import datetime
from ui import Ui_Assistant
from utils import VoiceAssistant


class VoiceThread(QThread):
    update_output = pyqtSignal(str)
    deactivate_signal = pyqtSignal()  # Signal to notify deactivation

    def __init__(self, assistant):
        super().__init__()
        self.ui = Ui_Assistant()
        self.ui.setupUi(self)
        self.assistant = assistant
        self.running = True

    def run(self):
        self.update_output.emit("<b>Listening...</b><br>")
        while self.running:
            try:
                command = self.assistant.listen_and_respond()
                if not command.strip():
                    continue

                if "deactivate" in command.lower():
                    self.update_output.emit("<b>Reply:</b> Deactivating voice assistant. Waiting for activation.<br>")
                    self.assistant.speak("Deactivating voice assistant. Waiting for activation.")
                    self.deactivate_signal.emit()
                    break

                self.update_output.emit(f"<b>User:</b> {command}<br>")
                response = self.assistant.process_command(command)
                self.update_output.emit(f"<b>Reply:</b> {response}<br>")
                self.assistant.speak(response)
                self.update_output.emit("<b>Listening...</b><br>")
            except Exception as e:
                self.update_output.emit(f"<b>Error:</b> {e}<br>")

    def stop(self):
        self.running = False
        if self.assistant.engine._inLoop:
            self.assistant.engine.endLoop()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Assistant()
        self.ui.setupUi(self)

        self.voice_thread = None
        self.is_active = False
        self.first_activation = True
        self.assistant = VoiceAssistant()

        # Connect UI elements to functionality
        self.ui.activate_button.clicked.connect(self.toggle_voice_assistant)
        self.ui.input_bar.returnPressed.connect(self.process_text_command)

    def toggle_voice_assistant(self):
        if not self.is_active:
            self.activate_voice_assistant()
        else:
            self.deactivate_voice_assistant()

    def activate_voice_assistant(self):
        if self.voice_thread and self.voice_thread.isRunning():
            self.voice_thread.stop()
            self.voice_thread.wait()

        self.voice_thread = VoiceThread(self.assistant)
        self.voice_thread.update_output.connect(self.update_output)
        self.voice_thread.deactivate_signal.connect(self.deactivate_voice_assistant)
        self.voice_thread.start()

        self.ui.activate_button.setText("Deactivate")
        self.ui.activate_button.setStyleSheet(self.ui.deactivate_button_style())

        if self.first_activation:
            greeting = self.get_greeting()
            self.update_output(f"<b>Reply:</b> {greeting}<br>")
            self.assistant.speak(greeting)
            self.first_activation = False
        self.is_active = True

    def deactivate_voice_assistant(self):
        if self.voice_thread:
            self.voice_thread.stop()
            self.voice_thread.quit()
            self.voice_thread.wait()

        self.ui.activate_button.setText("Activate")
        self.ui.activate_button.setStyleSheet(self.ui.activate_button_style())
        self.update_output("<b>Reply:</b> Hope you had a great time. Waiting to activate.<br>")
        self.assistant.speak("Hope you had a great time. Waiting to activate.")
        self.is_active = False

    def process_text_command(self):
        command = self.ui.input_bar.text().strip()
        if not command:
            return

        self.update_output(f"<b>User:</b> {command}<br>")
        response = self.assistant.process_command(command)
        self.update_output(f"<b>Reply:</b> {response}<br>")
        self.assistant.speak(response)
        self.ui.input_bar.clear()

    def update_output(self, text):
        self.ui.output.append(text)
        self.ui.output.verticalScrollBar().setValue(self.ui.output.verticalScrollBar().maximum())

    @staticmethod
    def get_greeting():
        current_hour = datetime.now().hour
        if 5 <= current_hour < 12:
            return "Good morning!"
        elif 12 <= current_hour < 18:
            return "Good afternoon!"
        elif 18 <= current_hour < 22:
            return "Good evening!"
        else:
            return "Hello! Hope you’re having a great time!"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

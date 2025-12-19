"""
Input Panel Component - Handles user input and send button
"""
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QPushButton
from PyQt6.QtCore import pyqtSignal, Qt
from ..styles import Styles

class InputPanel(QWidget):
    # Signal emitted when user sends a message
    message_sent = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_ui()
    
    def _setup_ui(self):
        """Initialize the input panel UI"""
        self.setStyleSheet(Styles.BOTTOM_PANEL)
        
        # Create layout
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)
        
        # Create input box
        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Type your message here...")
        self.input_box.setStyleSheet(Styles.INPUT_BOX)
        self.input_box.returnPressed.connect(self._on_send)
        
        # Create send button
        self.send_button = QPushButton("Send")
        self.send_button.setStyleSheet(Styles.SEND_BUTTON)
        self.send_button.clicked.connect(self._on_send)
        self.send_button.setFixedWidth(100)
        
        # Add widgets to layout
        layout.addWidget(self.input_box)
        layout.addWidget(self.send_button)
    
    def _on_send(self):
        """Handle send button click or Enter key press"""
        message = self.input_box.text().strip()
        if message:
            self.message_sent.emit(message)
            self.clear_input()
    
    def clear_input(self):
        """Clear the input box"""
        self.input_box.clear()
    
    def set_enabled(self, enabled: bool):
        """Enable or disable input controls"""
        self.input_box.setEnabled(enabled)
        self.send_button.setEnabled(enabled)
    
    def focus_input(self):
        """Set focus to the input box"""
        self.input_box.setFocus()

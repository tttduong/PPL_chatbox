"""
Chat Display Component - Shows conversation history
"""
from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtGui import QTextCursor
from PyQt6.QtCore import Qt
from ..styles import Styles

class ChatDisplay(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_ui()
    
    def _setup_ui(self):
        """Initialize the chat display widget"""
        self.setReadOnly(True)
        self.setStyleSheet(Styles.CHAT_DISPLAY)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        
    def add_message(self, sender: str, message: str):
        """
        Add a message to the chat display
        
        Args:
            sender: Name of the message sender
            message: Message content
        """
        if not message:
            return
        
        # Format message with HTML for better styling
        formatted_msg = f"""
        <div style='margin-bottom: 10px;'>
            <span style='color: {Styles.ACCENT_COLOR}; font-weight: bold;'>{sender}:</span>
            <span style='color: {Styles.TEXT_COLOR};'> {message}</span>
        </div>
        """
        
        self.append(formatted_msg)
        self.scroll_to_bottom()
    
    def scroll_to_bottom(self):
        """Scroll to the bottom of the chat display"""
        cursor = self.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        self.setTextCursor(cursor)
    
    def clear_chat(self):
        """Clear all messages from the display"""
        self.clear()
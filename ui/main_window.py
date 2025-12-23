"""
Main Window - Orchestrates all UI components
"""
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QFrame
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QIcon
import json

from .components.chat_display import ChatDisplay
from .components.input_panel import InputPanel
from .styles import Styles

# Import your existing Response class
try:
    from Response import Response
except ImportError:
    # Fallback if Response module not found
    class Response:
        def get_list(self, msg):
            return {'verbs': None, 'objects': None}
        def get_response(self, msg):
            return f"Echo: {msg}"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.response = Response()
        self.bot_name = "VA"
        self._setup_ui()
    
    def _setup_ui(self):
        """Initialize the main window UI"""
        self.setWindowTitle("Virtual Assistant Chat")
        self.setFixedSize(600, 500)  # (width, height)
        self.setStyleSheet(Styles.MAIN_WINDOW)
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Add header
        self.header = self._create_header()
        main_layout.addWidget(self.header)
        
        # Add divider line
        divider = self._create_divider()
        main_layout.addWidget(divider)
        
        # Add chat display
        self.chat_display = ChatDisplay()
        main_layout.addWidget(self.chat_display, stretch=1)
        
        # Add input panel
        self.input_panel = InputPanel()
        self.input_panel.message_sent.connect(self._on_message_sent)
        main_layout.addWidget(self.input_panel)
        
        # Set focus to input
        self.input_panel.focus_input()
        
        # Welcome message
        self.chat_display.add_message(
            self.bot_name,
            'Welcome back! I am your Virtual Assistant 👋 I can help you manage your calendar 😁. You can try: "show calendar today", "check event incompleted 22/12/2025", "set meeting 15:30 17:00 today".'
        )

    def _create_header(self):
        """Create the header label"""
        header = QLabel("🤖 Virtual Assistant")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setStyleSheet(Styles.HEADER_LABEL)
        header.setFixedHeight(50)
        return header
    
    def _create_divider(self):
        """Create a horizontal divider line"""
        divider = QFrame()
        divider.setFrameShape(QFrame.Shape.HLine)
        divider.setStyleSheet(Styles.DIVIDER_LINE)
        divider.setFixedHeight(2)
        return divider
    
    def _on_message_sent(self, message: str):
        """Handle message sent from input panel"""
        # Display user message
        self.chat_display.add_message("You", message)
        
        # Parse message
        element_list = self.response.get_list(message)
        
        # Check for Pomodoro command
        if (element_list.get('verbs') == "start" and 
            element_list.get('objects') == "pomodoro"):
            self._handle_pomodoro(message)
        else:
            self._handle_normal_response(message)
    
    def _handle_pomodoro(self, message: str):
        """Handle Pomodoro timer request"""
        try:
            with open("data/Data_pomodoro.json", 'r') as f:
                data = json.load(f)
            duration = data['pomodoro']['duration']
        except (FileNotFoundError, KeyError):
            duration = 25 * 60  # Default 25 minutes
        
        # Display Pomodoro start message
        self.chat_display.add_message(
            self.bot_name,
            "🍅 Pomodoro session started! Focus time begins now..."
        )
        
        # Disable input during Pomodoro
        self.input_panel.set_enabled(False)
        
        # Schedule end of Pomodoro
        QTimer.singleShot(duration * 1000, lambda: self._end_pomodoro(message))
    
    def _end_pomodoro(self, original_message: str):
        """Handle end of Pomodoro session"""
        self.chat_display.add_message(
            self.bot_name,
            "✅ Pomodoro session completed! Great work! Time for a break."
        )
        
        # Re-enable input
        self.input_panel.set_enabled(True)
        self.input_panel.focus_input()
    
    def _handle_normal_response(self, message: str):
        """Handle normal message response"""
        response_msg = self.response.get_response(message)
        self.chat_display.add_message(self.bot_name, response_msg)
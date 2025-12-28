"""
Main Window - Orchestrates all UI components with Guide Panel
"""
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                              QLabel, QFrame, QScrollArea)
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

class GuidePanel(QWidget):
    """Panel hiển thị hướng dẫn sử dụng"""
    def __init__(self):
        super().__init__()
        self._setup_ui()
    
    def _setup_ui(self):
        """Thiết lập giao diện bảng hướng dẫn"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(15)
        
        # Tiêu đề
        title = QLabel("User Guide")
        title.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: #2E2A3B;
                padding: 12px;
                background-color: #C8BFE7;
                border-radius: 8px;
            }
        """)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        # Scroll area cho nội dung
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
            QScrollBar:vertical {
                background: #F2EFFA; 
                width: 10px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical {
                background: #8E84F5; 
                border-radius: 5px;
                min-height: 30px;
            }
            QScrollBar::handle:vertical:hover {
                background: #7A6FF0;
            }
        """)
        
        # Widget chứa nội dung hướng dẫn
        content_widget = QWidget()
        content_widget.setStyleSheet("""
            QWidget {
                background-color: #C8BFE7;
            }
        """)

        content_layout = QVBoxLayout(content_widget)
        content_layout.setSpacing(20)
        content_layout.setContentsMargins(10, 10, 10, 10)
        
        # Danh sách các mục hướng dẫn
        guides = [
            ("➕ CREATE MEETING", [
                "Command format:",
                "• set meeting [start_time] [end_time] [date]",
                "",
                "Examples:",
                "• set meeting 15:30 17:00 today",
                "• set meeting 09:00 11:00 22/12/2025",
                "",
                "After submitting, enter title in double quotes:",
                "• \"Monthly Team Meeting\"",
                "• \"Project Review\"",
            ]),
            
            ("➕ CREATE EVENT", [
                "Command format:",
                "• set event [start_time] [end_time] [date]",
                "",
                "Examples:",
                "• set event 15:30 17:00 today",
                "• set event 09:00 11:00 22/12/2025",
                "",
                "After submitting, enter title in double quotes:",
                "• \"Christmas Party\"",
                "• \"Team Building\"",
            ]),
            
            ("📅 VIEW CALENDAR", [
                "Show both meetings and events:",
                "• show calendar today",
                "• check calendar 22/12/2025",
                "• show pending calendar today",
                "• check done calendar 22/12/2025",
            ]),
            
            ("📅 VIEW MEETINGS", [
                "Show meetings only:",
                "• show meeting today",
                "• check meeting today",
                "• show pending meeting today",
                "• check done meeting 22/12/2025",
            ]),
            
            ("📅 VIEW EVENTS", [
                "Show events only:",
                "• show event today",
                "• check event 22/12/2025",
                "• show pending event today",
                "• check done event 22/12/2025",
            ]),
            
            ("✅ COMPLETE EVENTS", [
                "Mark specific event as complete (use [id] from list):",
                "• complete [id]",
                "• finish [id]",
                "",
                "Examples:",
                "• complete 1",
                "• finish 2",
                "",
                "Complete all events on a date:",
                "• complete event today",
                "• finish event on 22/12/2025",
            ]),
            
            ("↩️ UNDO EVENTS", [
                "Mark specific event as incomplete (use [id] from list):",
                "• incomplete [id]",
                "• unfinish [id]",
                "",
                "Examples:",
                "• incomplete 1",
                "• unfinish 2",
                "",
                "Undo all events on a date:",
                "• incomplete event today",
                "• unfinish event on 22/12/2025",
            ]),
            
            ("🗑️ DELETE EVENT", [
                "Delete specific event (use [id] from list):",
                "• delete [id]",
                "• remove [id]",
                "• cancel [id]",
                "",
                "Examples:",
                "• delete 1",
                "• remove 2",
                "• cancel 3",
            ]),
        ]
        
        # Thêm từng mục hướng dẫn
        for category, examples in guides:
            section = self._create_guide_section(category, examples)
            content_layout.addWidget(section)
        
        content_layout.addStretch()
        scroll.setWidget(content_widget)
        layout.addWidget(scroll)
        
        # Style cho panel
        self.setStyleSheet("""
            GuidePanel {
                background-color: #C8BFE7;
                border-right: 2px solid #C8BFE7;
            }
        """)
    
    def _create_guide_section(self, title: str, examples: list) -> QWidget:
        """Tạo một section hướng dẫn"""
        section = QWidget()
        section.setStyleSheet("""
            QWidget {
                background-color: #FFFFFF;
                border-radius: 10px;
                padding: 5px;
            }
        """)
        
        layout = QVBoxLayout(section)
        layout.setContentsMargins(15, 12, 15, 12)
        layout.setSpacing(8)
        
        # Tiêu đề section
        title_label = QLabel(title)
        title_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                font-weight: bold;
                color: #2E2A3B;
                padding-bottom: 6px;
                background-color: transparent;
            }
        """)
        layout.addWidget(title_label)
        
        # Các ví dụ
        for example in examples:
            if example == "":
                # Thêm khoảng trống
                spacer = QLabel("")
                spacer.setFixedHeight(4)
                layout.addWidget(spacer)
            else:
                example_label = QLabel(example)
                example_label.setWordWrap(True)
                example_label.setTextInteractionFlags(
                    Qt.TextInteractionFlag.TextSelectableByMouse
                )
                
                # Style khác cho dòng heading và content
                if example.endswith(":"):
                    style = """
                        QLabel {
                            font-size: 12px;
                            font-weight: 600;
                            color: #2E2A3B;
                            padding: 4px 0px 2px 0px;
                            background-color: transparent;
                        }
                    """
                else:
                    style = """
                        QLabel {
                            font-size: 12px;
                            color: #555555;
                            padding: 2px 0px 2px 8px;
                            background-color: transparent;
                            font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
                        }
                    """
                
                example_label.setStyleSheet(style)
                layout.addWidget(example_label)
        
        return section

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.response = Response()
        self.bot_name = "VA"
        self._setup_ui()
    
    def _setup_ui(self):
        """Initialize the main window UI"""
        self.setWindowTitle("Calendar Chatbot")
        self.setWindowIcon(QIcon("ui/components/chatbot_logo.svg"))
        self.setFixedSize(950, 500)  # Mở rộng width từ 600 -> 950
        self.setStyleSheet(Styles.MAIN_WINDOW)
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create main horizontal layout
        main_h_layout = QHBoxLayout(central_widget)
        main_h_layout.setContentsMargins(0, 0, 0, 0)
        main_h_layout.setSpacing(0)
        
        # Add guide panel (bên trái)
        self.guide_panel = GuidePanel()
        self.guide_panel.setFixedWidth(350)  # Chiều rộng bảng hướng dẫn
        main_h_layout.addWidget(self.guide_panel)
        
        # Create chat area (bên phải)
        chat_widget = QWidget()
        chat_widget.setFixedWidth(600)  # Giữ nguyên width ban đầu
        chat_layout = QVBoxLayout(chat_widget)
        chat_layout.setContentsMargins(0, 0, 0, 0)
        chat_layout.setSpacing(0)
        
        # Add header
        self.header = self._create_header()
        chat_layout.addWidget(self.header)
        
        # Add divider line
        divider = self._create_divider()
        chat_layout.addWidget(divider)
        
        # Add chat display
        self.chat_display = ChatDisplay()
        chat_layout.addWidget(self.chat_display, stretch=1)
        
        # Add input panel
        self.input_panel = InputPanel()
        self.input_panel.message_sent.connect(self._on_message_sent)
        chat_layout.addWidget(self.input_panel)
        
        main_h_layout.addWidget(chat_widget)
        
        # Set focus to input
        self.input_panel.focus_input()
        
        # Welcome message
        self.chat_display.add_message(
            self.bot_name,
            'Welcome back! I am your Calendar Chatbot 👋 I can help you manage your calendar 😁. You can try: "show calendar today", "check pending event  22/12/2025", "set meeting 15:30 17:00 today".'
        )

    def _create_header(self):
        """Create the header label"""
        header = QLabel("🤖 Calendar Chatbot")
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
        self._handle_normal_response(message)
      
    def _handle_normal_response(self, message: str):
        """Handle normal message response"""
        response_msg = self.response.get_response(message)
        self.chat_display.add_message(self.bot_name, response_msg)
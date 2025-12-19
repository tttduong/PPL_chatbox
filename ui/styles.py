"""
Centralized stylesheet definitions for the application
"""

class Styles:
    # Colors
    BG_GRAY = "#ABB2B9"
    BG_COLOR = "#17202A"
    TEXT_COLOR = "#EAECEE"
    INPUT_BG = "#2C3E50"
    ACCENT_COLOR = "#3498db"
    HOVER_COLOR = "#5DADE2"
    
    # Main Window Stylesheet
    MAIN_WINDOW = f"""
        QMainWindow {{
            background-color: {BG_COLOR};
        }}
    """
    
    # Header Label Stylesheet
    HEADER_LABEL = f"""
        QLabel {{
            background-color: {BG_COLOR};
            color: {TEXT_COLOR};
            font-size: 16px;
            font-weight: bold;
            padding: 10px;
        }}
    """
    
    # Chat Display Stylesheet
    CHAT_DISPLAY = f"""
        QTextEdit {{
            background-color: {BG_COLOR};
            color: {TEXT_COLOR};
            border: none;
            font-size: 14px;
            padding: 5px;
        }}
    """
    
    # Input Box Stylesheet
    INPUT_BOX = f"""
        QLineEdit {{
            background-color: {INPUT_BG};
            color: {TEXT_COLOR};
            border: 2px solid {BG_GRAY};
            border-radius: 5px;
            padding: 8px;
            font-size: 14px;
        }}
        QLineEdit:focus {{
            border: 2px solid {ACCENT_COLOR};
        }}
    """
    
    # Send Button Stylesheet
    SEND_BUTTON = f"""
        QPushButton {{
            background-color: {ACCENT_COLOR};
            color: {TEXT_COLOR};
            border: none;
            border-radius: 5px;
            padding: 8px 15px;
            font-size: 13px;
            font-weight: bold;
        }}
        QPushButton:hover {{
            background-color: {HOVER_COLOR};
        }}
        QPushButton:pressed {{
            background-color: {ACCENT_COLOR};
        }}
    """
    
    # Divider Line Stylesheet
    DIVIDER_LINE = f"""
        QFrame {{
            background-color: {BG_GRAY};
            border: none;
        }}
    """
    
    # Bottom Panel Stylesheet
    BOTTOM_PANEL = f"""
        QWidget {{
            background-color: {BG_GRAY};
        }}
    """
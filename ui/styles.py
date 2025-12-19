"""
Centralized stylesheet definitions for the application
"""

class Styles:
    # Colors - dark blue 
    # BG_GRAY = "#ABB2B9"
    # BG_COLOR = "#17202A"
    # TEXT_COLOR = "#EAECEE"
    # INPUT_BG = "#2C3E50"
    # ACCENT_COLOR = "#3498db"
    # HOVER_COLOR = "#5DADE2"
   # Colors - Pink Theme 🌸
    BG_GRAY = "#E8B4C8"        # Hồng nhạt
    BG_COLOR = "#2D1B2E"       # Tím đen làm nền
    TEXT_COLOR = "#FFE5F1"     # Hồng trắng
    INPUT_BG = "#4A2C46"       # Tím đậm cho input
    ACCENT_COLOR = "#FF69B4"   # Hot Pink cho buttons
    HOVER_COLOR = "#FF85C1"    # Hồng sáng khi hover

    # Colors - Purple Pastel Light Theme
    BG_GRAY = "#F2EFFA"            # Nền phụ / panel (rất sáng)
    BG_COLOR = "#C8BFE7"           # Nền chính (tím pastel)

    TEXT_COLOR = "#2E2A3B"         # Text chính (tím xám đậm → đọc rõ)
    INPUT_BG = "#FFFFFF"           # Input nền trắng

    ACCENT_COLOR = "#7A6FF0"       # Nút / highlight chính
    HOVER_COLOR = "#8E84F5"        # Hover (sáng hơn accent)

    # Status colors (giữ nguyên)
    SUCCESS = "#5FB3A2"
    WARNING = "#F2C94C"
    ERROR = "#EB5757"

    
    # Status colors
    # SUCCESS = "#5FB3A2"
    # WARNING = "#F2C94C"
    # ERROR = "#EB5757"
    # # Main Window Stylesheet
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
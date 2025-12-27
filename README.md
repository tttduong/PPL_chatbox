# PPL Chatbox

A chatbot application with integrated to-do list functionality, built for the Principles of Programming Language course.

## Prerequisites

- Python 3.x
- Command Prompt (Windows)

## Setup Instructions

### 1. Environment Configuration

Create a `.env` file in the project root directory and add the following:
```

```

### 2. Virtual Environment Setup

Open Command Prompt and run the following commands:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate.bat

# Install dependencies
pip install -r requirements.txt
```

### 3. Running the Application
```bash
# Generate necessary files
python run.py gen

# Start the application
python main.py
```

## Usage Examples

### Viewing Calendar and Tasks
```
show calendar 22/12/2025
show meeting incomplete today
show event today
show calendar 18/11/2025
```

### Adding Items to Calendar
```
set meeting 08:00 12:00 25/12/2025
set meeting 15:30 17:00 today
```

## Features

- Interactive chatbot interface
- Calendar management
- Meeting scheduling
- Event tracking
- Task completion status
- MongoDB integration for data persistence

## Notes

- This application is designed to run in Command Prompt only
- Ensure your virtual environment is activated before running the application
- All times should be in 24-hour format (HH:MM)
- Dates should be in DD/MM/YYYY format

## Project Structure
```
PPL_chatbox/
├── .env                 # Environment variables
├── requirements.txt     # Python dependencies
├── run.py              # Setup script
├── main.py             # Main application entry point
└── venv/               # Virtual environment (generated)
```

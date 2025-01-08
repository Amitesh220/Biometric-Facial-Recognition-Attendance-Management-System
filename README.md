
# Biometric-Facial-Recognition-Attendance-System

This project is a facial recognition attendance system implemented using React for the frontend user interface, Flask for the backend server, and OpenCV with dlib for facial recognition capabilities.


## Features

- **Register Face:** Allows users to register their face by providing their name. The system captures their image using the webcam and stores their facial encoding in a database.
  
- **Mark Attendance:** Marks attendance by recognizing registered faces in real-time. When a recognized face is detected, it records the attendance along with the timestamp.

- **View Attendance:** Displays a list of attendance records showing who attended and when.

## Prerequisites

Before running the application, ensure you have the following installed:

- Node.js and npm
- Python 3
- Flask (Python package)
- dlib (Python package, requires CMake and Visual Studio Build Tools on Windows)
- face_recognition (Python package)
- MongoDB (for storing face encodings)

## Installation

### Frontend (React)

1. Clone the repository:
   ```bash
   git clone https://github.com/Amitesh220/Biometric-Facial-Recognition-Attendance-Management-System.git
   cd facial-recognition-attendance/frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

### Backend (Flask)

1. Navigate to the backend directory:
   ```bash
   cd ../backend
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

### Backend (Flask)

1. Set up environment variables:
   - Rename `.env.example` to `.env`.
   - Configure your database connection details and any other environment-specific configurations.

2. Start the Flask server:
   ```bash
   python app.py
   ```

### Frontend (React)

1. Open `src/App.js` and modify the API URL (`baseURL`) in Axios requests to match your backend server address (default is `http://localhost:5000`).

2. Start the React development server:
   ```bash
   npm start
   ```

## Usage

1. **Register Face:**
   - Enter your name in the input field and click "Register Face".
   - The system captures your image using the webcam and saves it for recognition.

2. **Mark Attendance:**
   - Click "Mark Attendance" to start real-time face recognition.
   - When a registered face is detected, your attendance is recorded with a timestamp.

3. **View Attendance:**
   - Click "View Attendance" to see the list of attendance records.
   - Each record shows the name of the attendee and the timestamp.
   ------

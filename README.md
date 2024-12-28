# CCTV Camera System

## Project Description
This project implements a CCTV camera monitoring system using computer vision and web technologies. It provides real-time video streaming, motion detection, and recording capabilities through a user-friendly web interface.

## Tech Stack
- **Frontend:**
    - HTML/CSS/JavaScript
    - Vite + React.js

- **Backend:**
    - Python
    - OpenCV
    - Flask

- **Database:**
    - SQLite

## Workflow
1. **Camera Initialization:**
     - System detects and initializes connected cameras
     - Establishes video streams

2. **Video Processing:**
     - Real-time video capture
     - Face detection processing
     - Frame optimization

3. **Storage & Retrieval:**
     - Frame details stored in database

4. **User Interface:**
     - Live stream viewing

## Local Setup Instructions
1. Clone the repository:
     ```bash
     git clone https://github.com/arghyadutta080/mini-cctv-camera.git
     cd cctv-camera
     ```

2. Install dependencies:
     ```bash
     # Backend dependencies
     cd server
     pip install -r requirements.txt
     
     # Frontend dependencies
     cd client
     npm install
     ```


3. Run the application:
     ```bash
     # Start backend server
     cd server
     python app.py
     
     # Start frontend development server
     cd client
     npm run dev
     ```

4. Access the application:
     - Open browser and navigate to `http://localhost:5173`
     

## Requirements
- Python 3.8+
- Node.js 14+
- Webcam or IP camera
- 2GB RAM minimum
- 500MB free disk space
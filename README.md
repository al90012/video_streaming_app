# API-First Video Streaming App

This project consists of a Flask backend and a React Native (Expo) frontend.

## Prerequisites
- Python 3.8+
- Node.js & npm
- MongoDB Instance (Atlas or Local)

## Setup Backend
1. Navigate to `backend/`:
   ```bash
   cd backend
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Mac/Linux:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure environment:
   - Copy `.env.example` to `.env`
   - Update `MONGO_URI`
5. Seed database:
   ```bash
   python seed.py
   ```
6. Run server:
   ```bash
   python app.py
   ```

## Setup Frontend
1. Navigate to `mobile-app/`:
   ```bash
   cd mobile-app
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Update API URL:
   - Open `src/services/api.ts`
   - Set `API_URL` to your machine's IP address (e.g., `http://192.168.1.5:5000` or `http://10.0.2.2:5000` for Android Emulator).
4. Run app:
   ```bash
   npx expo start
   ```

## Features
- **JWT Auth**: Secure user registration and login.
- **Dashboard**: Lists exactly 2 active videos.
- **Streaming**: Masks actual YouTube links via backend proxy/abstraction.

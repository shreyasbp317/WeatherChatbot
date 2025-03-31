# WeatherChatbot
This is a simple weather chatbot that provides real-time weather updates based on user queries. The chatbot detects continent names in user messages and returns weather information for a representative city in that continent using the OpenWeatherMap API.

Features

🌍 Detects continent names in user input.

☁️ Fetches real-time weather details using OpenWeatherMap API.

🔗 Simple API integration with a frontend.

📡 Uses Flask backend with CORS enabled for seamless communication.

Installation & Setup

1️⃣ Prerequisites

Ensure you have Python 3 installed on your system.

2️⃣ Clone the Repository
git clone https://github.com/yourusername/weather-chatbot.git
cd weather-chatbot
3️⃣ Install Dependencies
pip install flask flask-cors requests
4️⃣ Get an OpenWeatherMap API Key

Sign up at OpenWeatherMap

Get a free API key

Replace API_KEY in app.py with your key

5️⃣ Run the Flask Backend
python app.py
The backend will start at: http://127.0.0.1:5001/

6️⃣ Open the Frontend

Open index.html in your browser.

If using VS Code, open with Live Server.

Enter queries like: weather in Europe.

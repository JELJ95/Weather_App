# Weather App ☁️🌦️

## 📌 Project Description

This is a simple weather application written in Python. It allows users to enter a city name and fetches current weather data using the OpenWeatherMap API. The application displays temperature (in Celsius), weather description, wind speed, and the timestamp of the data retrieved.

## 🛠️ Technologies and Tools

- **Python 🐍**
- **Libraries:** Requests, Datetime
- **API:** OpenWeatherMap (Current Weather Data)

## 🧠 Key Features

- Retrieves real-time weather data for any city
- Converts temperature from Kelvin to Celsius
- Converts Unix timestamp to readable UTC date and time
- Handles errors gracefully (e.g. invalid city names)
- Keeps sensitive information (API key) secure via `secrets.py`

## 🔐 API Security

To avoid exposing the API key:
- The key is stored in a separate file (`secrets.py`)
- The file is excluded from version control using `.gitignore`

## 🚀 How to Run the Project

1. **Install dependencies**
   ```bash
   pip install requests
   ```

2. **Create a `secrets.py` file** in the root of your project:
   ```python
   API_KEY = "your_openweathermap_api_key"
   ```

3. **Run the script**
   ```
   python Weather_app.py
   ```

4. **Enter a city name when prompted**

## 💡 What Did I Learn?

- How to interact with public APIs (HTTP requests and JSON parsing)
- How to secure sensitive data using `.gitignore`
- Error handling and user-friendly input
- Converting timestamps and temperature units

## 💎 Contact

If you have any questions or feedback, feel free to reach out:  
📧 julie_emmy_95@hotmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/julie-jansen-a73232138)

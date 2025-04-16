import requests
from datetime import datetime, timezone
from secrets import API_KEY


def city_weather():
    """
    Prompts the user to enter a city name, fetches weather data from OpenWeatherMap,
    and prints temperature, weather description, wind speed, and timestamp.
    """

    city_name = input("Please enter city name: ")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"

    # Sends a GET request to the API and parses the response as JSON.
    r = requests.get(url)
    data = r.json()

    # If the city is not found (invalid input), display a message and exit the function.
    if r.status_code != 200:
        print("City not found. Please try again.")
        return

    # Converts the Unix timestamp to a readable UTC date and time.
    timestamp = data["dt"]
    date = datetime.fromtimestamp(timestamp, timezone.utc)

    # Converts temperature from Kelvin to Celsius.
    kelvin_temp = data["main"]["temp"]
    celsius_temp = kelvin_temp - 273.15

    print(f"\nWeather data for {city_name} on {date.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Temperature: {celsius_temp:.2f} °C")
    print(f"Weather: {data['weather'][0]['description']}")
    print(f"Wind: {data['wind']['speed']} m/s")

city_weather()
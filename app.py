import requests

api_key = "YOUR_API_KEY"

city = input("Enter a city name: ")

response = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
)

weather_data = response.json()


if response.status_code == 200:
    print("\n==========================")
    print("      WEATHER REPORT")
    print("==========================")

    print("City:", weather_data["name"])
    print("Country:", weather_data["sys"]["country"])
    print("Temperature:", weather_data["main"]["temp"], "°C")
    print("Feels Like:", weather_data["main"]["feels_like"], "°C")
    print("Humidity:", weather_data["main"]["humidity"], "%")
    print("Wind Speed:", weather_data["wind"]["speed"], "m/s")
    print("Weather:", weather_data["weather"][0]["description"])

    print("==========================")

else:
    print("City not found!")
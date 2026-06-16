import tkinter as tk
import requests

# Enter your OpenWeather API key here
api_key = "619a7cd068e213198396e26133333253"


def get_weather(city=None):

    if city is None:
        city = city_entry.get()

    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    )

    weather_data = response.json()

    if response.status_code == 200:

        weather = weather_data["weather"][0]["description"].title()

        result = f"""
🌍 City: {weather_data['name']}
🏳️ Country: {weather_data['sys']['country']}

🌡️ Temperature: {weather_data['main']['temp']} °C
🤗 Feels Like: {weather_data['main']['feels_like']} °C
💧 Humidity: {weather_data['main']['humidity']} %
💨 Wind Speed: {weather_data['wind']['speed']} m/s
lalitude: {weather_data['coord']['lat']}
longitude: {weather_data['coord']['lon']}

☁️ Weather: {weather}
"""

    else:
        result = f"❌ Error: {weather_data.get('message', 'Unknown error')}"

    result_label.config(text=result)


# Create main window
root = tk.Tk()
root.title("🌤 Weather App")
root.geometry("650x550")
root.configure(bg="lightblue")


# Title
title = tk.Label(
    root,
    text="🌤 Weather App",
    font=("Arial", 22, "bold"),
    bg="lightblue"
)
title.pack(pady=10)


# Instruction
instruction = tk.Label(
    root,
    text="Enter a city or choose one below:",
    font=("Arial", 12),
    bg="lightblue"
)
instruction.pack()


# City Entry
city_entry = tk.Entry(
    root,
    width=30,
    font=("Arial", 14)
)
city_entry.pack(pady=10)


# Quick City Buttons
button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="🏔 Kathmandu",
    command=lambda: get_weather("Kathmandu")
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="🇬🇧 London",
    command=lambda: get_weather("London")
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="🗼 Tokyo",
    command=lambda: get_weather("Tokyo")
).grid(row=0, column=2, padx=5)

tk.Button(
    button_frame,
    text="🗽 New York",
    command=lambda: get_weather("New York")
).grid(row=0, column=3, padx=5)


# Search Button
search_button = tk.Button(
    root,
    text="Get Weather",
    font=("Arial", 12, "bold"),
    command=get_weather
)
search_button.pack(pady=10)


# Result Label
result_label = tk.Label(
    root,
    text="Weather information will appear here.",
    font=("Arial", 12),
    bg="lightblue",
    justify="left"
)
result_label.pack(pady=20)


root.mainloop()
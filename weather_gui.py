import tkinter as tk
import requests

api_key = "67099730000ce3e884e1f0ab30c71941"

def get_weather():
    city = city_entry.get()

    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    )

    weather_data = response.json()

    if response.status_code == 200:
        result = f"""
==========================
      WEATHER REPORT
==========================

City: {weather_data['name']}
Country: {weather_data['sys']['country']}
Temperature: {weather_data['main']['temp']} °C
Feels Like: {weather_data['main']['feels_like']} °C
Humidity: {weather_data['main']['humidity']} %
Wind Speed: {weather_data['wind']['speed']} m/s
Weather: {weather_data['weather'][0]['description'].title()}

==========================
"""
    else:
        result = f"Error: {weather_data.get('message', 'Unknown error')}"

    result_label.config(text=result)


# Create window
root = tk.Tk()
root.title("Weather App")
root.geometry("450x500")

# Heading
heading = tk.Label(
    root,
    text="Weather App",
    font=("Arial", 18, "bold")
)
heading.pack(pady=10)

# City input
city_entry = tk.Entry(root, width=30, font=("Arial", 12))
city_entry.pack(pady=10)

# Button
search_button = tk.Button(
    root,
    text="Get Weather",
    font=("Arial", 12),
    command=get_weather
)
search_button.pack(pady=10)

# Result label
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 11),
    justify="left"
)
result_label.pack(pady=20)

# Run app
root.mainloop()
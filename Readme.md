# Day 1: Python Weather App Journey 🌤

## Topics Covered

* Python Packages
* API
* JSON
* Requests Library
* OpenWeather API
* Tkinter GUI
* Git & GitHub

---

## 1. Python Packages

Packages are collections of Python modules that provide extra functionality.

### Installing Packages

```bash
pip install requests
```

### Importing a Package

```python
import requests
```

---

## 2. API (Application Programming Interface)

API allows two applications to communicate.

Example:

```text
Python App → OpenWeather API → Weather Data
```

### API Request URL

```python
url = "https://api.openweathermap.org/data/2.5/weather"
```

---

## 3. HTTP GET Request

```python
response = requests.get(url)
```

### Common HTTP Methods

| Method | Purpose       |
| ------ | ------------- |
| GET    | Retrieve data |
| POST   | Create data   |
| PUT    | Update data   |
| DELETE | Remove data   |

---

## 4. Response Object

```python
print(response.status_code)
```

### Status Codes

| Code | Meaning      |
| ---- | ------------ |
| 200  | Success      |
| 401  | Unauthorized |
| 404  | Not Found    |
| 500  | Server Error |

---

## 5. JSON

JSON stands for **JavaScript Object Notation**.

Example JSON:

```json
{
  "name": "Kathmandu",
  "main": {
    "temp": 28.5,
    "humidity": 45
  }
}
```

Convert JSON to Python dictionary:

```python
weather_data = response.json()
```

---

## 6. Python Dictionary

Access dictionary values:

```python
weather_data["name"]
weather_data["main"]["temp"]
weather_data["main"]["humidity"]
weather_data["weather"][0]["description"]
```

---

## 7. Error Handling

```python
if response.status_code == 200:
    print("Success")
else:
    print("Error")
```

---

## 8. OpenWeather API

Use API key:

```python
api_key = "YOUR_API_KEY"
```

Create request:

```python
response = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
)
```

---

## 9. Tkinter GUI

Import Tkinter:

```python
import tkinter as tk
```

Create Window:

```python
root = tk.Tk()
root.mainloop()
```

### Widgets Learned

* Label
* Entry
* Button
* Frame

Example:

```python
label = tk.Label(root, text="Weather App")
```

---

## 10. Git Commands

Initialize repository:

```bash
git init
```

Add files:

```bash
git add .
```

Commit changes:

```bash
git commit -m "Initial commit"
```

Check version:

```bash
git --version
```

---

## 11. GitHub

GitHub is used to:

* Store code online
* Create portfolio projects
* Collaborate with developers
* Track changes

---

## Weather App Features Built

* [x] City Search
* [x] Temperature
* [x] Humidity
* [x] Wind Speed
* [x] Feels Like Temperature
* [x] Error Handling
* [x] Tkinter GUI
* [x] Git & GitHub

---

## Key Concepts Learned

* Variables
* Functions
* Dictionaries
* JSON
* APIs
* Packages
* GUI Development
* Git
* GitHub

---

## Next Goals

* [ ] Weather Icons
* [ ] Sunrise & Sunset
* [ ] Dark Mode
* [ ] Streamlit Web App
* [ ] Flask
* [ ] Database

> "Small progress every day leads to big results."

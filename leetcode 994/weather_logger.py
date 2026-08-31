import requests
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

API_KEY = "ca1a11b2a9cf411b4c997fd47d19e0aa"
CITIES = ["Lahore", "Karachi", "Islamabad", "Vilnius", "London"]

# Google Sheets auth
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("service_account.json", scopes=scopes)
client = gspread.authorize(creds)
sheet = client.open("Weather Log").sheet1  # must match your exact sheet name

def fetch_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    return {
        "city": city,
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "condition": data["weather"][0]["description"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def main():
    for city in CITIES:
        weather = fetch_weather(city)
        sheet.append_row([
            weather["city"],
            weather["temp"],
            weather["humidity"],
            weather["condition"],
            weather["timestamp"]
        ])
        print(f"Logged: {weather}")

if __name__ == "__main__":
    main()
from bs4 import BeautifulSoup
import requests


def get_weather(city: str):
    url = f"https://wttr.in/{city}?0q&lang=ru"
    resp = requests.get(url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser')
        weather_info = soup.get_text()
        return weather_info
    else:
        return "Error"

city = 'moscow'
weather = get_weather(city)
print(weather)
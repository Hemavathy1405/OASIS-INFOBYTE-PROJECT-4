pip install beautifulsoup4 requests
import requests
from bs4 import BeautifulSoup

def get_weather(location):
    url = f"https://www.google.com/search?q=weather+{location}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        temperature = soup.find("span", attrs={"id": "wob_tm"}).text
        condition = soup.find("span", attrs={"id": "wob_dc"}).text
        humidity = soup.find("span", attrs={"id": "wob_hm"}).text

        return {
            'temperature': temperature,
            'condition': condition,
            'humidity': humidity
        }
    except AttributeError:
        return None

def main():
    location = input("Enter the city or ZIP code: ")
    weather = get_weather(location)
    
    if weather:
        print(f"Weather in {location.capitalize()}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Condition: {weather['condition']}")
        print(f"Humidity: {weather['humidity']}")
    else:
        print("Could not retrieve weather data. Please check the location.")

if __name__ == "__main__":
    main()

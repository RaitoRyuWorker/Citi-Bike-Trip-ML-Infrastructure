import requests

def get_weather_data(lon, lat, api_key):
    url = f"https://api.openweathermap.org/data/3.0/onecall/overview?lon={lon}&lat={lat}&appid={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

if __name__ == "__main__":
    lon = -11.8092
    lat = 51.509865
    api_key = "YOUR_API_KEY_HERE"
    
    weather_data = get_weather_data(lon, lat, api_key)
    
    if weather_data:
        print(weather_data)
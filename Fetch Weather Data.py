#Example Code: Fetch Weather Data
import requests

# Example of an API key (usually required for real-world APIs)
api_key = 'your_api_key'
city = 'London'

# Construct the API URL
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

# Make the request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print(f"Current weather in {city}: {data['weather'][0]['description']}")
else:
    print(f"Failed to retrieve data: {response.status_code}")

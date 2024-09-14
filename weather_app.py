import requests
import json

def get_weather(city_name):
    api_key = "5c107820f466926b62d0066787d85e58"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"


    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url)

    data = response.json()

# Checking either data successfully fetch or not

    if data["cod"] != "404" :

# Extracting relevant data from response

        main = data["main"]
        weather = data["weather"][0]

# Extracting Temprate, Pressure, humidity from 
        temprature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        description = weather["description"]

# converting temprature from kelvin to celcius

        temp_kel_to_cel = temprature - 273.15


        print(f"City Name: {city_name}")
        print(f"Temprature: {temp_kel_to_cel:.2f}°C ")
        print(f"Pressure: {pressure} hpa")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description.capitalize()}")

    else:
        print("City not found!")


def main():
    city_name = input("Enter city name: ")

    get_weather(city_name)

if __name__ == "__main__":
    main()





# weather_app

𝐎𝐯𝐞𝐫𝐯𝐢𝐞𝐰:
The 'Weather App' is a Python-based command-line tool that allows users to check real-time weather conditions for any city using the OpenWeatherMap API. By entering the name of a city, the app fetches the latest weather data and displays the temperature, weather description, humidity, and other important details. This project helped me learn about handling APIs, making HTTP requests, and parsing JSON data.

This project was developed with the goal of enhancing my skills in working with APIs and handling real-time data. Through this, I gained deeper insights into interacting with external services and managing JSON data in Python.


𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬:
(i). Fetch Real-time Weather Data: Users can input the name of a city and receive up-to-date weather information including temperature, humidity, and weather description.
(ii). API Integration: Uses the OpenWeatherMap API to fetch live weather data for the user-specified location.
(iii). Error Handling: The app includes error-handling mechanisms to ensure that invalid city names or API issues do not crash the program.
(iv). JSON Parsing: The weather data is provided in JSON format, which is parsed and presented in a user-friendly manner.
(v). Simple and Clear Interface: Easy-to-use command-line interface that interacts with the user and displays the weather data in a clean, readable format.


𝐀𝐏𝐈 𝐊𝐞𝐲 𝐚𝐧𝐝 𝐄𝐧𝐯𝐢𝐫𝐨𝐧𝐦𝐞𝐧𝐭:
To run this project, you will need to get your API key from 'OpenWeatherMap' by sign up, and store it in a secure place. You can either hard-code the API key (not recommended) or store it in an environment variable for secure access.


𝐇𝐨𝐰 𝐭𝐨 𝐑𝐮𝐧 𝐭𝐡𝐞 𝐏𝐫𝐨𝐣𝐞𝐜𝐭?

(i) Clone the repository:
git clone https://github.com/abdullahsaqib100/weather-app.git

(ii) Navigate to the project directory:
cd weather-app

(iii) Install required dependencies:
The app uses the requests module to handle HTTP requests, which you can install using:
pip install requests

(iv) Run the Python script:
python3 weather_app.py


𝐒𝐚𝐦𝐩𝐥𝐞 𝐑𝐮𝐧/ 𝐎𝐮𝐭𝐩𝐮𝐭 𝐑𝐞𝐬𝐮𝐥𝐭:
Enter city name: London  
Current temperature: 15°C  
Weather: Clear sky  
Humidity: 65%  
Wind Speed: 5.5 m/s  


𝐋𝐢𝐜𝐞𝐧𝐬𝐞:
This project is licensed under the MIT License - see the LICENSE file for details.

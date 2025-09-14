import requests
import streamlit as st
from datetime import datetime

# The main title of the Streamlit application.
st.title("🌦 Real-Time Weather App")

# Input field for the user to enter a city name. The default value is London.
city = st.text_input("Enter City Name", "London")

# from OpenWeatherMap. You can get one for free from their website.
API_KEY = "ce5b9ef1aae1446dfd474dfa66785f4b"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# Button to trigger the weather data retrieval.
if st.button("Get Weather"):
    if city:
        # Check if the API key has been replaced.
        if API_KEY == "YOUR_API_KEY":
            st.error(" Please replace 'YOUR_API_KEY' with your actual API key.")
        else:
            # Construct the full URL for the API request.
            url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"

            # Use a try-except block to handle potential errors gracefully.
            try:
                # Make the GET request to the OpenWeather API.
                response = requests.get(url)
                
                # Check if the response status code is 200 (OK).
                if response.status_code == 200:
                    data = response.json()
                    
                    # Extract and format the weather information from the JSON response.
                    temp = data["main"]["temp"]
                    feels_like = data["main"]["feels_like"]
                    humidity = data["main"]["humidity"]
                    pressure = data["main"]["pressure"]
                    wind = data["wind"]["speed"]
                    sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M:%S")
                    sunset = datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M:%S")
                    description = data["weather"][0]["description"].title()
                    
                    # Display the weather information in a clean format using Streamlit.
                    st.subheader(f" Weather in {city}")
                    st.write(f"Temperature: {temp} °C (Feels like {feels_like} °C)")
                    st.write(f" Humidity: {humidity}%")
                    st.write(f" Wind Speed: {wind} m/s")
                    st.write(f" Pressure: {pressure} hPa")
                    st.write(f" Sunrise: {sunrise}")
                    st.write(f" Sunset: {sunset}")
                    st.write(f" Condition: {description}")
                else:
                    # Display an error if the city is not found or other API issues occur.
                    st.error(" City not found. Please check the spelling and try again.")
            
            except requests.exceptions.RequestException as e:
                # Catch and handle network-related errors.
                st.error(f"An error occurred while fetching data: {e}. Please check your internet connection.")
            except KeyError:
                # Handle cases where the API response might be missing expected keys.
                st.error(" Invalid API response. The city might not be supported or the data structure is unexpected.")
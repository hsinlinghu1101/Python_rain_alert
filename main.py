import requests
import os
from twilio.rest import Client
import config

My_LATITUDE = 33.659771
MY_LONGITUDE = -117.999313

MY_API = config.OWM_API_KEY
account_sid = config.account_sid
auth_token = config.auth_token
PHONE = config.twilio_phone

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall?lat={My_LATITUDE}&lon={MY_LONGITUDE}&exclude=current,minutely,daily,alerts&appid={MY_API}")

get_weather_id = [hour["weather"][0]["id"] for hour in response.json()["hourly"][:12]]

will_rain = False
for hour in get_weather_id:
    if hour < 700:
        will_rain = True

client = Client(account_sid, auth_token)
if will_rain:

        message = client.messages \
          .create(
            body="It's going to rain today. Remember to bring an ☂️",
            from_=PHONE,
            to='+13234048799'
    )
        print(message.sid)
else:

        message = client.messages \
          .create(
            body="Nice weather 🥰",
            from_=PHONE,
            to='+13234048799'
    )
        print(message.sid)

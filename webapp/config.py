from datetime import timedelta
import os

from sqlalchemy import false


basedir = os.path.abspath(os.path.dirname(__file__))

WEATHER_DEFAULT_CITY = "Voronezh,Russia"
WEATHER_API_KEY = "3a5fce89ea704f8fb20191957222705"
WEATHER_URL = "http://api.worldweatheronline.com/premium/v1/weather.ashx"

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "..", "webapp.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "flkjvnh3ohfga8pyghq3890ygh9ayh[p0erq9p23t8yh[g043aertw34t3qhw"

REMEMBER_COOKIE_DURATION = timedelta(days=5)
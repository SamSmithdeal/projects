"""Configure application settings such as the database URI, secret key, etc."""

import socket

TEAM = "team24"

# Determine whether connecting from on/off campus
try:
    socket.gethostbyname("data.cs.jmu.edu")
    HOST = "data.cs.jmu.edu"
except socket.gaierror:
    HOST = "localhost"


# See https://flask-appbuilder.readthedocs.io/en/latest/config.html

SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg://{TEAM}@{HOST}/{TEAM}"

SECRET_KEY = "4363504cd866941740d3022d84cbad4264b37be0685adfe78044596e81a10fe2"

AUTH_TYPE = 1  # Database style (user/password)

APP_NAME = "Spotlight"

APP_THEME = "readable.css"

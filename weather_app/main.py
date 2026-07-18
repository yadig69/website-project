# TODO: Fix the imports below!
# We want to use get_weather() and format_temp()
from utils.formatter import get_weather, format_temp
import utils.fetcher as fetcher

print("--- WEATHER DASHBOARD ---")
raw_temp = get_weather()
print(f"Current Temperature: {format_temp(raw_temp) }")
from utils.fetcher import get_weather

def format_temp(celsius):
    return f"{celsius}°C ({celsius * 9/5 + 32}°F)"

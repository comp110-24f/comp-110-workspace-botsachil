def get_weather_report() -> str:
    weather: str = input("What is the weather?")

    if weather == "rainy" or "cold":
        print("Bring a jacket!")

    elif weather == "hot":
        print("Keep cool out there!")

    else:
        print("I dont recognize this weather.")

    return weather

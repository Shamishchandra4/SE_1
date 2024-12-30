def classify_weather(weather):
    if weather > 4000:
        return "Sunny"
    elif 2000 < weather <= 4000:
        return "Cloudy"
    elif 1000 < weather <= 2000:
        return "Rainy"
    else:
        return "Stormy"

def calculate_weather(temperature, humidity, windspeed):
    return 1.5 * temperature - 0.4 * humidity + 0.3 * windspeed - 10

def process_file(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) != 3:
                    raise ValueError("Each line must have three values: temperature, humidity, windspeed.")
                temperature, humidity, windspeed = map(float, data)
                weather = calculate_weather(temperature, humidity, windspeed)
                classification = classify_weather(weather)
                print(f"Input: {data} => Calculated weather: {weather} ({classification})")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    process_file("input.txt")

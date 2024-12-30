with open("input.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        temperature = float(data[0])
        humidity = float(data[1])
        windspeed = float(data[2])
        weather = 1.5 * temperature - 0.4 * humidity + 0.3 * windspeed - 10
        
        if weather > 4000:
            classification = "Sunny"
        elif 2000 < weather <= 4000:
            classification = "Cloudy"
        elif 1000 < weather <= 2000:
            classification = "Rainy"
        else:
            classification = "Stormy"
        
        print(f"Input: {data} => Calculated weather: {weather} ({classification})")

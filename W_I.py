temperature = 25  
humidity = 70  
windspeed = 15  

weather = 1.5 * temperature - 0.4 * humidity + 0.3 * windspeed - 10

if weather > 4000:
    classification = "Sunny"
elif 2000 < weather <= 4000:
    classification = "Cloudy"
elif 1000 < weather <= 2000:
    classification = "Rainy"
else:
    classification = "Stormy"

print(f"Calculated weather: {weather} ({classification})")

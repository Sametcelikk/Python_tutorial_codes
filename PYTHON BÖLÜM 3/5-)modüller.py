import ceviriciler

for celcius in range(-100,101):
    print(f"{celcius} derece = {ceviriciler.celciusToFahrenheit(celcius):.4} fahrenayttır")

for fahrenheit in range (-50,51):
    print(f"{fahrenheit} fahrenayt = {ceviriciler.fahreneitToCelcius(fahrenheit):.4} derecedir")
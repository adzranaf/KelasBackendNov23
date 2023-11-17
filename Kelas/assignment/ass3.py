#Buatlah sebuah function yang dapat mengkonversi suhu dari fahrenheit. 
#Berikan argumen untuk memastikan bahwa outputnya dalah celcius atau kelvin

def convert_from_fahrenheit(temperature_fahrenheit, output_unit):
    
    if output_unit.upper() == 'C':
        #Konversi dari Fahrenheit ke Celcius
        temperature_celcius = (temperature_fahrenheit - 32) * 5/9
        return temperature_celcius
    elif output_unit.upper() == 'K':
        #Konversi dari Fahrenheit ke Kelvin
        temperature_celcius = (temperature_fahrenheit - 32) * 5/9
        temperature_kelvin = temperature_celcius + 273.15
        return temperature_kelvin
    else:
        print("Suhu tidak valid")

# Contoh penggunaan:
temperature_fahrenheit = 80.0
temperature_celcius = convert_from_fahrenheit(temperature_fahrenheit, 'C')
print(f"{temperature_fahrenheit} F = {temperature_celcius:.2f} C")

temperature_kelvin = convert_from_fahrenheit(temperature_fahrenheit, 'K')
print(f"{temperature_fahrenheit} F = {temperature_kelvin:.2f} K")

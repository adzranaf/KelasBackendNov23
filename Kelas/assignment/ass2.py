#Buatlah sebuah function yang dapat mengkonversi suhu ke fahrenheit. 
#Tambahkan parameter untuk memastikan bahwa argumen yang dimasukan adalah celcius atau kelvin.
#Panggil function yang pertama jika diperlukan

print("=====Konversi suhu ke fahrenheit=====")
def convert_to_fahrenheit(temperature, unit):

    if unit.upper() == 'C':
        #Celcius ke Fahrenheit
        fahrenheit = (temperature * 9/5) + 32
        return fahrenheit
    elif unit.upper() == 'K':
        #Kelvin ke Fahrenheit
        celcius = temperature - 273.15
        fahrenheit = (celcius * 9/5) + 32
        return fahrenheit
    else:
        print("Unit suhu tidak valid")

#Penerapan Celsius ke Fahrenheit:
temperature_celcius = 30.0
temperature_fahrenheit = convert_to_fahrenheit(temperature_celcius, 'C')
print(f"{temperature_celcius} C = {temperature_fahrenheit:.2f} F")

#Penerapan Kelvin ke Fahrenheit:
temperature_kelvin = 250.0
temperature_fahrenheit = convert_to_fahrenheit(temperature_kelvin, 'K')
print(f"{temperature_kelvin} K = {temperature_fahrenheit:.2f} F")

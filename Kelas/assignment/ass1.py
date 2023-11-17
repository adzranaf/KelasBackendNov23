#Buatlah sebuah function yang dapat mengkonversi suhu dari kelvin ke celcius, dan celcius ke kelvin.

print("=====Konversi kelvin ke celcius=====")
#Konversi suhu dari kelvin ke celcius
def kelvin_to_celcius(kelvin):
    celcius = kelvin - 273.15
    return celcius

#Penerapan kelvin ke celcius:
temperature_kelvin = 200.0
temperature_celcius = kelvin_to_celcius(temperature_kelvin)
print(f"Hasil Convert kelvin ke celcius = ")
print(f"Nilai dalam Kelvin : {temperature_kelvin} K")
print(f"Nilai dalam Celcius : {temperature_celcius:.2f} C")

print("=====Konversi celcius ke kelvin=====")
#Konversi suhu dari celcius ke kelvin
def celcius_to_kelvin(celcius):
    kelvin = celcius + 273.15
    return kelvin

#Penerapan Celcius ke Kelvin
temperature_celcius = 45.0
temperature_kelvin = celcius_to_kelvin(temperature_celcius)
print(f"Hasil Convert Celcius ke Kelvin = ")
print(f"Nilai dalam Kelvin : {temperature_kelvin} K")
print(f"Nilai dalam Celcius : {temperature_celcius:.2f} C")

print(f"{temperature_celcius} Celcius = {temperature_kelvin:.2f} Kelvin")

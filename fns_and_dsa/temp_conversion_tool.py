FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
try:
    user_input = input("Enter the temperature to convert: ")
    temprature = float(user_input)  
except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value.")
current_scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").capitalize()

def convert_to_celsius(fahrenheit):
    converted_temprature = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print (f"{fahrenheit}°F is {converted_temprature}°C")

def convert_to_fahrenheit(celsius):
    converted_temprature = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print (f"{celsius}°C is {converted_temprature}°F")

match current_scale:
    case 'F':
        convert_to_celsius(temprature)
        pass
    case 'C':
        convert_to_fahrenheit(temprature)
        pass
    case _:
        print("Invalid unit. Please enter the correct unit.")

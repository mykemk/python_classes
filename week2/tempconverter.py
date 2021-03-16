'''
-Function to convert temperature from fareignheight to degree celsious and vice versa
'''

def toFahrenheit(temp=0):
    '''
    Takes the temperature in degree celcius and converts the temperature in farenheit
    '''
    fahrenheit = (9/5 * temp) + 32
    print(f"The temperature {temp} degrees celcius is {fahrenheit} F")

def toCelcius(temp=0):
    '''
    Takes temperature in degree celcius and converts it to farenheit
    '''
    celsius = (5/9) * (temp-32)
    print(f"The temperature {temp} farenheit is {celsius} degrees celsius")

def toKelvin(temp):
    '''
    Takes temperature in degree celcius and converts it to Kelvin
    '''
    kelvins = temp + 273
    print(f"The temperature {temp} degrees is {kelvins} K")

toFahrenheit(temp=10)
toCelcius(temp=10)
toKelvin(10)

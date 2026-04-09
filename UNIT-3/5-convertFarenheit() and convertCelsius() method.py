# Create a Temperature class. Create 2 methods named convertFarenheit() and convertCelsius().

class Temperature:
    def convertFahrenheit(self, c):
        return (c * 9/5) + 32

    def convertCelsius(self, f):
        return (f - 32) * 5/9


temp = Temperature()

print("25°C in Fahrenheit:", temp.convertFahrenheit(25))
print("77°F in Celsius:", temp.convertCelsius(77))
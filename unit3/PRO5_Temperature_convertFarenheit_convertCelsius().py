#Create a Temperature class. Create 2 methods named convertFarenheit() and convertCelsius().

class Temperature:
    def convertFarenheit(self,c):
        f = (c * 9/5) + 32
        print(f"{c}°C = {f}°F")
    def convertCelsius(self,f):
        c = (f - 32) * 5/9
        print(f"{f}°F = {c}°C")

temp = Temperature()
temp.convertFarenheit(25)
temp.convertCelsius(77)
      










































    

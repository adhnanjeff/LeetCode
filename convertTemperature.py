#Problem 2469
class Solution(object):
    def convertTemperature(self, celsius):
        kelvin = 273.15 + celsius
        fahrenheit = (celsius * 9/5 + 32)
        return [kelvin, fahrenheit]

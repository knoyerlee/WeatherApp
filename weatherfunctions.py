
class Temperature:
    # Temp Labels
    fahrenheit_label = (" \N{DEGREE SIGN}F")
    celsius_label = (" \N{DEGREE SIGN}C")

    # Temp Conversion Functions
    def convert_to_f(temperature):
        result = (float(temperature) - 273.15) * (9/5) + 32
        return round(result, 2)

    def convert_to_c(temperature):
        result = (float(temperature) - 273.15)
        return round(result, 2)

def to_Celsius(farh):
    celcius_value = (farh - 32) * (5/9)
    return celcius_value
t_farh = float(input())        #taking input temp in fahrenheit from users.
temperature = to_Celsius(t_farh)
print("Fahrenheit to Celsius value is:", temperature)
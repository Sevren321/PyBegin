# User input of currrent temperature
userInput = input("Degrees in Celsius: ")
temperature = int(userInput)

if temperature < 0:
    print("It's freezing out there!")
elif temperature < 10: 
    print("It's pretty cold.")
elif temperature < 20: 
    print("It's cool out.")
elif temperature < 30: 
    print("It's warm.")
else: 
    print("It's too hot!")

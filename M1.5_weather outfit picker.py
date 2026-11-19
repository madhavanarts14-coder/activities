temperature = int(input("What is the current temperature in celcius: "))

if temperature < 20:
    outfit = "jacket"
    print("it is cold today, wear a", outfit)
else:
    outfit = "t-shirt"
    print("it is a sunny day, wear a", outfit)
raining = (input("is it raining?: "))

if raining == "yes":
    print("bring an umbrella ")
wind_speed = int(input("enter the wind speed: "))

if wind_speed > 30:
    windbreaker_needed = "yes"
    print("it is windy today")
    print("wear a windbreaker over your", outfit)
else:
    windbreaker_needed = "no"
    print("it is calm today")
    print("no windbreaker needed over your", outfit)
is_puddles = (input("Are there any puddles?: "))

if is_puddles == "yes":
    shoes = "boots"
    print("hey! the ground is wet ")
    print("you should wear", shoes)
else:
    shoes = "sneakers"
    print("the ground is not wet")
    print("you can wear", shoes)

print("\n Weather check is complete.\n")
print("===========weather outfit picker===========")
print("the temperature is", temperature, "celcius")
print("the outfit chosen is", outfit)
print("raining: ", raining )
print("wind breaker needed: ", windbreaker_needed)
print("shoes chosen: ", shoes)
print("===========================================")







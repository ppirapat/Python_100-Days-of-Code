# Output Welcome Text
print("Welcome to the Band Generator.")

# Ask the user for the name of the city he/she grew up in 
city = input("What is the name of the city you grew up in?\n")

# Ask the user for his/her pet name
pet = input("What is the name of a pet?\n")

# Print - Method 1: 
print("1: Your band name could be", city, pet)

# Print - Method 2:
print("2: Your band name could be " + city + " " + pet) 

# Print - Method 3: 
print(f"3: Your band name could be {city} {pet}")

# Print - Method 4: 
print("{}{}{}{}".format("4: Your band name could be ", city, " ", pet))
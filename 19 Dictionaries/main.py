# dictionary =  A changeable, unordered collection of unique key:value pairs
#               Fast because they use hashing, allow us to access a value quickly

capitals = {"USA": "Washington DC",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# Adds a new key:value pair
capitals.update({"Germany": "Berlin"})
# Updates an existing key:value pair
capitals.update({"USA": "Las Vegas"})
# Removes a certain key:value pair
capitals.pop("China")
# Removes all existing key:value pair

#print(capitals["Germany"])
# Checker
#print(capitals.get("Germany"))

# Displays the keys of a set
#print(capitals.keys())
# Displays the values of a set
#print(capitals.values())


# Displays everything WAY 1
#print(capitals.items())

# Display either keys or value WAY 2
for key, value in capitals.items():
    print(key, value)

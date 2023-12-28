programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Variable": "A piece of code that you can use to store values in it"
}

# Retrieving items from a dictionary
print(programming_dictionary["Bug"])

# Adding items to a dictionary
programming_dictionary['Loop'] = 'The action of doing something over and over again'

print(programming_dictionary)

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}

# print(programming_dictionary)

# Edit an item in a dictionary

print(programming_dictionary["Bug"])

programming_dictionary["Bug"] = "A moth in your computer"

print(programming_dictionary["Bug"])

# Loop through a dictionary

for key in programming_dictionary:
    print(programming_dictionary[key])

# Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a List in a Dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": [{"Berlin": {"asd": 1}}, "Hamburg", "Stuttgart"], "total_visits": 12}
}

print(travel_log)

# Nesting a Dictionary in a Dictionary

travel_log = {
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 12
    }
}

# Nesting a Dictionary in a List

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 12
    }
]

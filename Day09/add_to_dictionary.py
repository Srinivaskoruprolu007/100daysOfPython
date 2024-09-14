# List of dictionaries, each representing travel information for a country
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

# Function to add a new country to the travel_log
def add_new_country(country, visits, list_of_cities):
    # Create a dictionary with the new country's travel information
    new_country = {
        "country": country,
        "visits": visits,
        "cities": list_of_cities
    }
    # Append the new country dictionary to the travel_log list
    travel_log.append(new_country)

# Add a new country to the travel_log
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

# Print the updated travel_log to show the new country added
print(travel_log)
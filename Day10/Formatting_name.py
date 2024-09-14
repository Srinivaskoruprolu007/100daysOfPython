# Function to format the first and last name into title case (first letter capitalized).
def format_name(f_name: str, l_name: str):
    # Convert the first name to title case.
    formatted_f_name = f_name.title()
    # Convert the last name to title case.
    formatted_l_name = l_name.title()
    # Return the formatted full name (first name followed by last name).
    return f"{formatted_f_name} {formatted_l_name}"

# Get the first name from the user.
first_name = input("Enter your first name : \n")

# Get the last name from the user.
last_name = input("Enter your last name : \n")

# Call the format_name function and print the formatted full name.
print(format_name(first_name, last_name))
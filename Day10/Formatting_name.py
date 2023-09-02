def format_name(f_name: str, l_name: str):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


first_name = input("Enter your first name : \n")
last_name = input("Enter your last name : \n")
print(format_name(first_name, last_name))

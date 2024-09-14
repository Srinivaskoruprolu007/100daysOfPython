from prettytable import PrettyTable

# Create a new PrettyTable object
table = PrettyTable()

# Add columns to the table with alignment to the right
table.add_column("Pokemon Name", ["pikachu", "Squirrel", "fichu"], align='r')
table.add_column("Type", ["Electric", "Water", "Fire"], align='r')

# Print the table
print(table)

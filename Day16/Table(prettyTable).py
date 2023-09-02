from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["pikachu", "Squirrel", "fichu"], align='r')
table.add_column("Type", ["Electric", "Water", "Fire"], align='r')
print(table)

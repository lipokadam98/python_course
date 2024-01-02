from prettytable import PrettyTable

x = PrettyTable()

x.field_names = ["Pokemon Name", "Types"]
x.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
    ]
)
x.align = "l"

print(x)

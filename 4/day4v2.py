f = open("list.txt", "r")

transaction_list = f.read().split("\n")
ingredients = {"egg": 0, "melk": 0, "sukker": 0, "mel": 0}

for line in transaction_list:
    for ing in line.split(", "):
        ingredient, amount = ing.split(": ")
        ingredients[ingredient] += int(amount)

print(
    min(ingredients["egg"], ingredients["sukker"] / 2, ingredients["mel"] / 3,
        ingredients["melk"] / 3))

#1458014

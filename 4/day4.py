f = open("list.txt", "r")

transaction_list = f.read().split("\n")
eggs = 0
flour = 0
milk = 0
sugar = 0

for i in transaction_list:
    for j in i.split(", "):
        if j.split(": ")[0] == "egg":
            eggs += int(j.split(": ")[1])
        if j.split(": ")[0] == "mel":
            flour += int(j.split(": ")[1])
        if j.split(": ")[0] == "melk":
            milk += int(j.split(": ")[1])
        if j.split(": ")[0] == "sukker":
            sugar += int(j.split(": ")[1])

eggs_used = 0
flour_used = 0
milk_used = 0
sugar_used = 0
cakes = -1

while eggs_used <= eggs and flour_used <= flour and milk_used <= milk and sugar_used <= sugar:
    sugar_used += 2
    flour_used += 3
    milk_used += 3
    eggs_used += 1
    cakes += 1

print(cakes)
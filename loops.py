foods = ['apple', 'bread', 'cheese', 'milk', 'banana', 'graves']

""" print(foods[0])
print(foods[1])
print(foods[2])
print(foods[3])
print(foods[4]) """

print("")
print(" FOR")
print("")
for food in foods:
    if food == "cheese":
        # break # se detiene el ciclo
        continue
    print(food)
print("")
print(" WHILE")
print("")

count = 4
while count <= 10:
    print(count)
    count = count + 1
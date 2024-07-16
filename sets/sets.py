# sets - a collection which is unordered, unidexed and no duplicate
    # - a set is faster than a list

utensils = {"fork", "spoon", "knife"}

utensils.add("teaspoon")
utensils.remove("teaspoon")
# utensils.clear()

dishes = {'bowl', 'plate', 'cup', 'knife'}
dishes.update(utensils)

for x in dishes:
    print(x)

merged = utensils.union(dishes)
for x in merged:
    print(x)

print(utensils.difference(dishes)) # difference
print(dishes.difference(utensils))

print(utensils.intersection(dishes))


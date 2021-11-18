# print("Hello world!")
# print("Bizimarian23@gmail.com")



import copy

list1 = [7,8,9,2,3,1,4,10,5,6]

Ascendent = copy.deepcopy(list1)
Ascendent.sort()
print(f"Lista ascendenta este:  {Ascendent}")

Descendent = copy.deepcopy(Ascendent)
Descendent.reverse()
print(f"Lista descendenta este:  {Descendent}")

print(f"Lista numerelor cu indici pari este:  {Ascendent[1::2]}")
print(f"Lista numerelor cu indici pari este:  {Ascendent[::2]}")

print(f"Lista  elementelor care sunt multipli ai lui 3 este: {Ascendent[2::3]}")
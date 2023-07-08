cargo = [40,20,4,5,30,8,2,7,3,19,32,40,20,35,15,32,9]

boxCapacity = 90
box = []
i = 0

lenCargo = len(cargo)

while i < lenCargo and sum(box) <= boxCapacity and sum(box) + min(cargo) <= boxCapacity:
    box.append(min(cargo))
    cargo.pop(cargo.index(min(cargo)))
    i+=1
else:
    print('The collected items sum is:', sum(box))
    print('The elements are:', box)


print(cargo)


print('#################################################')

cargo = [40,20,4,5,30,8,2,7,3,19,32,40,20,35,15,32,9]
cargo.sort()
cargo.reverse()
boxCapacity = 90
box = []
i = 0

while i < len(cargo) and (boxCapacity - sum(box) >= min(cargo)):
    if (boxCapacity - sum(box)) >= cargo[i]:
        box.append(cargo[i])
    i+=1

print('The collected items sum is:', sum(box))
print('The elements are:', box)

print('#################################################')


cargo = [40, 20, 4, 5, 30, 8, 2, 7, 3, 19, 32, 40, 20, 35, 15, 32, 9]
boxCapacity = 90
box = []
i = 0

while sum(box) < boxCapacity and i < len(cargo):
    if sum(box) + cargo[i] <= boxCapacity:
        box.append(cargo[i])
    i += 1

print("Box contents:", box)
print("Total items in the box:", len(box))
print("Total weight in the box:", sum(box))


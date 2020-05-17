#nums = [int(x) for x in input().split()]
#print(nums)

names = (input().split())
index = names.index(max(names, key=len))
names[index] = names[index].upper()
print(names)
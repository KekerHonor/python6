# Нэрсийн дарааллаас хамгийн урт нэрийг ол.
names = (input().split())
print(names)
z = 0
for i in names:
    urt = len(i)
    if z <= urt:
        z = urt
        a = i
print(a)
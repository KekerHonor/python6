# Нэрсийн дарааллаас хамгийн богино нэрийг ол.
names = (input().split())
print(names)
z = 99
for i in names:
    urt = len(i)
    if z >= urt:
        z = urt
        a = i
print(a)
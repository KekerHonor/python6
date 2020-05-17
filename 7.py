# Нэрсийн дарааллаас хамгийн богино нэрийг олж 'Сайн уу?' гэж соль.
names = ["danzanravjaa","bold","bat"]
print(names)
z = 99
for i in names:
    urt = len(i)
    if z >= urt:
        z = urt
        a = i
index = names.index(a)
names.insert(index,"Sain uu?")
print(names)
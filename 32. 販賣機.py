moeny = int(input("小明身上有幾元:"))
drink = int(input("販賣機有幾種飲料:"))
a = 0
for i in range(drink):
    price = int(input())
    if moeny >= price:
        a += 1
print(a)
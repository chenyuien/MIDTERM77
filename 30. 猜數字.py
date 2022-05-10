ans = input()
z = input()
a,b = 0,0
while z != "0000":
    for i in z:
        if i in ans:
            if z.index(i) == ans.index(i):
                a += 1
            else:
                b += 1
    print(f"{a}A{b}B")
    z = input()
    a,b = 0,0
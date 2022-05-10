def ten2two(x):
    num = 0
    for i in range(1,len(x)):
        if "0" not in x[:i]:
            num += 1
    num *= 2
    if x[-1] == "1":
        num += 1
    return str(num)

num1,num2 = input().split()
new_num = int(ten2two(num1)+ten2two(num2))
if new_num + 67 == 91:
    print("A")
elif new_num + 67 == 92:
    print("B")
elif new_num + 67 == 93:
    print("C")
else:
    print(chr(new_num + 67))
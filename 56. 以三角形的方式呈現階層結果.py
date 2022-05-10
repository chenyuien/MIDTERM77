a = int(input("請輸入一個正整數(<10)："))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print()
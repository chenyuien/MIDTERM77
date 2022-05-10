n = int(input("整數n:"))
while n != 1:
    if n % 2 == 0:
        print(int(n),end=" ")
        n /= 2
    else:
        print(int(n),end=" ")
        n = 3*n+1
else:
    print(int(n),end=" ")
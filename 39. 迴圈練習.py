n = int(input())  # only input 奇數

# print 正三角
for i in range(1,n+1,2):
    for j in range((n-i)//2,0,-1):
        print(" ",end="")
    print("*"*i)


# print 倒三角
for i in range(n-2,0,-2):
    for j in range((n-i)//2,0,-1):
        print(" ",end="")
    print("*"*i)
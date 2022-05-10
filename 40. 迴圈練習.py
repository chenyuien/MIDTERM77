n = int(input())
# 上側直向
for i in range(1,n,2):
    print(" "*(n//2)+str(i))
# 左側橫向
for i in range(1,n+1,2):
    print(i,end="")
# 右側橫向
for i in range(n-2,0,-2):
    print(i,end="")
print()
# 下側直向
for i in range(n-2,0,-2):
    print(" "*(n//2)+str(i))
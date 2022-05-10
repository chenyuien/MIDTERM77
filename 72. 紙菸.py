n = int(input("請輸入 n："))
k = int(input("請輸入 k："))
add = n // k
total = add
while add >= k:
    add //= k
    total += add
print(f"Peter 可以抽 {n+total} 支紙菸")
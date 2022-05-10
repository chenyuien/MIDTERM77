a = int(input("組數為:"))
c = []
for i in range(a):
    b = list(map(int,input(f"\n第 {i+1} 組:").split()))
    c.append(b[0]*250+b[1]*175)

for i in range(a):
    print(f"\n第 {i+1} 組應收費用:{c[i]}")
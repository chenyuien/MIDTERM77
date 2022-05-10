a = input().split()
card = {"A":1,"J":11,"Q":12,"K":13}
ans = 0
for i in a:
    if i in card:
        ans += card[i]
    else:
        ans += int(i)
print(ans)
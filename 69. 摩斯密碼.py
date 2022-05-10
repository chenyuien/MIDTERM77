moss = input().split()
ans = ""
for i in moss:
    if i[-1] == "-":
        dit = i.rstrip("-")
        ans += str(len(dit))
    elif i[-1] == ".":
        dah = i.rstrip(".")
        ans += str(5 + len(dah))
print(ans)
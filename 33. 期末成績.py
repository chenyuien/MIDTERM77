a = {"國文":0,"英文":0,"微積分":0,"體育":0,"程式設計":0}
for i in a:
    score = int(input(i+":"))
    a[i] = score

print("平均分數：%.2f"%(sum(a.values())/len(a)))

high = "".join([k for k,v in a.items() if v == max(a.values())])
slow = "".join([k for k,v in a.items() if v == min(a.values())])
print(f"最高分科目：{high}{max(a.values())}分")
print(f"最高分科目：{slow}{max(a.values())}分")
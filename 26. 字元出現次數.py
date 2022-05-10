s1 = input("檢測的字串(end結束):")
while s1 != "end":
    s2 = input("\n檢測的單一字元:")
    print(f"字元 {s2} 出現次數為:{s1.count(s2)}")
    s1 = input("檢測的字串(end結束):")
print("檢測結束")
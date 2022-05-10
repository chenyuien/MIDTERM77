num_list1 = []
for i in range(10):
    num = int(input(f"請輸入第 {i+1} 個數字："))
    num_list1.append(num)
num_list2 = num_list1.copy()
big,small = [],[]
for i in range(3):
    big.append(str(max(num_list1)))
    small.append(str(min(num_list2)))
    num_list1.remove(max(num_list1))
    num_list2.remove(min(num_list2))
small.sort(reverse=True)
print("最大的 3 個數字為："+",".join(big))
print("最小的 3 個數字為："+",".join(small))
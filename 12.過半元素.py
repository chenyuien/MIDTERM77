num_list = input().split()
a = "NO"
for i in num_list:
    if num_list.count(i) > len(num_list)/2:
        a = i
print(f"過半元素為:{a}")
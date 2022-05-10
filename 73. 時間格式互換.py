time1 = input("請輸入時間 1(時:分:秒)：")
hour,minute,second = time1.split(":")
ans1 = int(hour)*3600 + int(minute)*60 + int(second)

time2 = int(input("請輸入時間 2(秒)："))
ans_hour,y = divmod(time2,3600)
ans_minute,ans_second = divmod(y,60)
ans2 = f"{ans_hour}:{ans_minute}:{ans_second}"
print(f"時間 1 ({time1})格式轉換後為 {ans1} 秒")
print(f"時間 2 ({time2} 秒) = {ans2}")
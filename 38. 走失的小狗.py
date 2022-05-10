place = int(input())
distance_list = []
for i in range(place):
    distance = int(input())
    distance_list.append(distance)
for i,j in enumerate(distance_list):
    if j % 9 == 0 or j % 11 == 0:
        print(f"第{i+1}個點 {j}")
a = int(input("測試的資料量:"))
blood = {"O O":["O"],"O A":["A","O"],"O B":["B","O"],"O AB":["A","B"],
         "A A":["A","O"],"A B":["A","B","O","AB"],"A AB":["A","B","AB"],
         "B B":["B","O"],"B AB":["A","B","AB"],"AB AB":["A","B","AB"]}
for i in range(a):
    b = input()
    if b[:3] in blood:
        if b[-1] in blood[b[:3]]:
            print("YES")
        else:
            print("IMPOSSIBLE")
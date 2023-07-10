row = int(input())  # 10
col = int(input())  # 20
tree_num = int(input())
trees =[]
for i in range(1,col+1):
    trees.append(i)
    trees.append(col*row-col+i)
    
for i in range(1,col*row,col):
    trees.append(i)

print(True if tree_num in trees else False)
row = int(input())  # 10
col = int(input())  # 22
tree_num = int(input())

if(tree_num<=col or tree_num%col==0 or tree_num%col==1):
    print(True)
else:
    print(False)
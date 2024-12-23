def common(L1,L2):
    L3=[]
    for i in L1:
        if i in L2:
            L3.append(i)
    return L3

L1=eval(input("enter list: "))
L2=eval(input("enter list: "))
print("the merged list is:", common(L1,L2))
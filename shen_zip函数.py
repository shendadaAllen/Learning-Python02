l1 = [1,2,3,4,5,6]
l2 =[11,22,33,44,55,66,]
l3 = ["大白","大米","大明","小白","小米","小明"]
z = zip(l1,l2)
for i in z:
    print(i)
x = zip(l1,l2,l3)
l = [i for i in x]
print(l)


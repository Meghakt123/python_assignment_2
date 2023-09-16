

# python program to find smallest number in a list:


list1=[]
x=int(input('limits:'))
for i in range(0,x):
    a=int(input('enter value:'))
    list1.append(a)
k=list1[0]
for a in list1:
    if a<k:
        k=a
print(k)


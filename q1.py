# python program to interchange first and last elements in a list

list1=[]
x=int(input('enter limits:'))
for i in range(0,x):
    y=input('enter name:')
    list1.append(y)
print(list1)
a=list1[0]
list1[0]=list1[-1]
list1[-1]=a
print(list1)
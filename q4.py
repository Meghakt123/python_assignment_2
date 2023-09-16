



# python program to write odd numbers in a list:

list1=[]
x=int(input('limits:'))
for i in range(0,x):
    a=int(input('enter value:'))
    if a%2!=0:
        list1.append(a)
print(list1)
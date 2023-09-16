

# write a python program to print maximum and minimum number in tuple

x=(12,32,64,15,16,27,38)
y=list(x)
k=y[0]
p=y[0]
for i in y:
    if i>k:
        k=i
print('maximum is:',k)

for i in y:
    if i<p:
        p=i
print('minimum is:',p)
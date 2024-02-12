b=1
c=1
counter=0
check=0
x=0
a=1
s=1000
x=1
while counter==0:
    for i in range(1,a+1):
        b=b*i
    x=x+1/b
    check=check+1
    b=1
    a=a+1
    if check==s:
        print (x)
        break



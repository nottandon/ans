def prime(n) :
    f=True
    for i in range(2,n) :
        if n%i==0 :
            f=False
            break
    return f
num=input("enter a no")
num=int(num)
p=prime(num)
if not p==True :
    quit()
a=num
d=0
while a!=0 :
    d+=1
    a=int(a/10)
a=num
for i in range(1,d) :
    a=a*10
    a+=a/(10**d)
    a=a%int(10**d)
    a=int(a)
    p=prime(a)
if(p==True) :
    print(num,"is circular prime")
    

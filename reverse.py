num=(input("enter a no"))
num=int(num)
a=0
while num!=0 :
    a=(a*10)+(num%10)
    num//=10
print(a)

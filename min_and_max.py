lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
min=lst[0]
max=lst[0]
for i in range(n) :
    if lst[i]>max :
        max=lst[i]
    if lst[i]<min :
        min=lst[i]
print("minimum is",min,"and max is",max)


a=int(input("Enter number:"))
i=1
j=0
num=1

while(i<=a):
    l=[]
    sum=0
    for j in range(1,num):
        if(num%j==0):
            l.append(j)
            sum+=j
    if(sum==num):
         i+=1
         l="+".join(map(str,l))
         print(f"{num}={l}")
    num+=1
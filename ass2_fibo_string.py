#print fibonaci strings..('A','B','BAB',')
n=int(input("enter value"))
a="A"
b="B"
if n > 29:
    print("limited value ocuupie to fcatorial string.")
else:

    for i in range(1,n):
        c=a+b
        a=b
        #b=c[:10]
        b=c
        print(b)



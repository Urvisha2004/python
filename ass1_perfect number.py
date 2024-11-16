#1Find the Perfect numbers. (A number is perfect if the sum of its proper divisors equals itself. E.g: 28 = 1+2+4+7+14)
def is_perfect_number(n):#(6)
    sum = 0
    for i in range(1, n): #(1,6)
        if n % i == 0:  #(6/6=0)
            sum=sum+i;() #(0=0+6) =6
    return sum == n #6=6
number=int(input("enter number"))
if is_perfect_number(number):  #6
    print(f"{number} is a perfect nuer.")
else:
    print(f"{number} is not a perfect number.")

"""
6
28
496
8128
130816
2096128
33550336 up to infinity."""

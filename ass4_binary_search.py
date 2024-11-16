#Write a program for binary search.

arr = list(map(int, input("enter element ").split()))
arr.sort()
x = int(input("enetr search element: "))
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2  
        if arr[mid] == x:
            return mid     
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
      return -1
#arr.sort()
res = binary_search(arr, 0, len(arr)-1, x)
if res != -1:
    print("element index is:", res)
else:
    print("element not found")

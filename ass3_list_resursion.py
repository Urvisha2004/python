#2.3 Print a list recursively.
def rec_function(l, n):
    if n < 0:
        return
    else:
        print(l[n])
        rec_function(l, n - 1)
l = []
while True:
    choice = input("1. Insert element\n2. Display List\n3. Exit\nEnter your choice: ")

    
    if not choice.isdigit():   
        print("Only numerical values are allowed.")
        continue

    choice = int(choice)

    if choice == 1:
        n = input("Enter element: ")

       
        if not n.isdigit(): 
            print("Only numerical values are allowed.")
        else:
            l.append(int(n))

    elif choice == 2:
        size = len(l)
        if size == 0:
            print("The list is empty.")
        else:
            rec_function(l, size - 1)

    elif choice == 3:
        break

    else:
        print("Wrong choice.")

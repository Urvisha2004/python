import academi as a

while True:
    aa = input("1. add  courses \n2. delete\n3. display\n4. cgpa\n5. exit\nEnter your choice: ")
    match aa:
        case '1':
            cc = input("Add course: ")
            try:
                cr = float(input("Add credits: "))
                er = float(input("Add earned points: "))
                a.add(cc, cr, er)  
                print(f"Course '{cc}' with credits {cr} and earned points {er} is added.")
            except ValueError:
                print("enter require input")

        case '2':
            dc = input("Enter course to delete: ")
            a.drop(dc)  
            print(f"Course '{dc}' deleted.")

        case '3':
            a.print_courses()  

        case '4':
            cgpa_value= a.cgpa()
            if cgpa_value is not None:  # Ensure CGPA calculation was successful
                print(f"Your CGPA is: {cgpa_value:.2f}")
            else:
                print("CGPA could not be calculated. Make sure courses are added.")

        case '5':
            print("Exiting...")
            break
        


courses = []

def add(cc, cr, er):
    courses.append((cc, cr, er)) 
    print(f"add course '{cc}' and credits  {cr} and earnpoint {er} .")

def drop(cc):
    for course in courses:
        if course[0] == cc: 
            courses.remove(course)
            print(f"delete course '{cc}'.")
            return
    print(f"{cc} is not in the course list.")  # If course not found

def print_courses():
    if courses:
        print("cource full etail:")
        for cc, cr, er in courses:
            print(f"Course: {cc}, Credits: {cr}, Earned Points: {er}")
    else:
        print("No courses available.")


def cgpa():
    numerator = 0
    denominator = 0
    for cc, cr, er in courses:
        numerator += cr * er
        denominator += cr
    if denominator == 0:
        return 0  # To avoid division by zero
    return numerator / denominator
'''def cgpa():
    total_credits = sum(cr for cc, cr, er in courses)
    total_er = sum(er for cc, cr, er in courses)
    
    if total_credits == 0:
        print("Total credits are zero, cannot calculate CGPA.")
        return 
    result = total_er / total_credits
    return result
print (cgpa())'''


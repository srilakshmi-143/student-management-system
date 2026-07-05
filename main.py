import json
import os

print("=" * 50)
print("      STUDENT MANAGEMENT SYSTEM")
print("      Developed in Python")
print("=" * 50)

FILE_NAME = "students.json"

def load_students():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except:
        return []

def save_students(students):
    with open(FILE_NAME, "w") as f:
        json.dump(students, f, indent=4)

def add_student(students):
    roll=input("Enter Roll Number: ").strip()
    if not roll:
        print("Roll Number cannot be empty.")
        return
    for s in students:
        if s["roll"]==roll:
            print("Student with this Roll Number already exists!")
            return
    name=input("Enter Name: ").strip()
    while True:
        age=input("Enter Age: ").strip()
        if age.isdigit():
            break
        print("Age should contain only numbers.")
    department=input("Enter Department: ").strip()
    while True:
        try:
            cgpa=float(input("Enter CGPA (0-10): "))
            if 0<=cgpa<=10:
                break
            print("CGPA must be between 0 and 10.")
        except ValueError:
            print("Enter a valid CGPA.")
    students.append({"roll":roll,"name":name,"age":age,"department":department,"cgpa":cgpa})
    save_students(students)
    print("Student Added Successfully!")

def view_students(students):
    if not students:
        print("\nNo Student Records Found.\n")
        return
    print("\n"+"-"*70)
    print("{:<10}{:<15}{:<10}{:<15}{:<10}".format("Roll","Name","Age","Department","CGPA"))
    print("-"*70)
    for s in students:
        print("{:<10}{:<15}{:<10}{:<15}{:<10}".format(s["roll"],s["name"],s["age"],s["department"],s["cgpa"]))
    print("-"*70)
    print("Total Students :",len(students))

def search_student(students):
    roll=input("Enter Roll Number to Search: ")
    for s in students:
        if s["roll"]==roll:
            print("\nStudent Found!")
            print(f"Roll Number : {s['roll']}")
            print(f"Name        : {s['name']}")
            print(f"Age         : {s['age']}")
            print(f"Department  : {s['department']}")
            print(f"CGPA        : {s['cgpa']}")
            return
    print("Student Not Found.")

def update_student(students):
    roll=input("Enter Roll Number to Update: ")
    for s in students:
        if s["roll"]==roll:
            print("\nLeave blank if you don't want to change a field.\n")
            name=input(f"Enter New Name ({s['name']}): ").strip()
            age=input(f"Enter New Age ({s['age']}): ").strip()
            if age and not age.isdigit():
                print("Invalid Age!")
                return
            department=input(f"Enter New Department ({s['department']}): ").strip()
            cgpa=input(f"Enter New CGPA ({s['cgpa']}): ").strip()
            if cgpa:
                try:
                    cg=float(cgpa)
                    if not (0<=cg<=10):
                        print("CGPA must be between 0 and 10.")
                        return
                    cgpa=cg
                except ValueError:
                    print("Invalid CGPA!")
                    return
            if name: s["name"]=name
            if age: s["age"]=age
            if department: s["department"]=department
            if cgpa!="": s["cgpa"]=cgpa
            save_students(students)
            print("Student Updated Successfully!")
            return
    print("Student Not Found.")

def delete_student(students):
    roll=input("Enter Roll Number to Delete: ")
    for s in students:
        if s["roll"]==roll:
            c=input("Are you sure? (y/n): ").lower()
            if c=="y":
                students.remove(s)
                save_students(students)
                print("Student Deleted Successfully!")
            else:
                print("Deletion Cancelled.")
            return
    print("Student Not Found.")

def menu():
    print("\n"+"="*50)
    print("        STUDENT MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

students=load_students()
while True:
    menu()
    ch=input("Enter your choice: ")
    if ch=="1":
        add_student(students)
    elif ch=="2":
        view_students(students)
    elif ch=="3":
        search_student(students)
    elif ch=="4":
        update_student(students)
    elif ch=="5":
        delete_student(students)
    elif ch=="6":
        save_students(students)
        print("Thank you for using Student Management System.")
        break
    else:
        print("Invalid choice.")

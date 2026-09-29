# ==========================================================
#              COLLEGE MANAGEMENT SYSTEM
#              Registration No: 26MIM10209
# ==========================================================

students = []
faculty = []
courses = []
attendance = []
marks = []
fees = []
timetable = []


# ================= STUDENT MANAGEMENT =====================

def add_student():
    print("\n--- Add Student ---")

    name = input("Enter student name: ")
    reg_no = input("Enter registration number: ")
    branch = input("Enter branch: ")
    year = input("Enter year: ")

    student = [name, reg_no, branch, year]
    students.append(student)

    print("Student added successfully!")


def view_students():
    print("\n--- Student Records ---")

    if len(students) == 0:
        print("No student records found.")
    else:
        for student in students:
            print("Name:", student[0])
            print("Registration No:", student[1])
            print("Branch:", student[2])
            print("Year:", student[3])
            print("----------------------")


# ================= FACULTY MANAGEMENT =====================

def add_faculty():
    print("\n--- Add Faculty ---")

    name = input("Enter faculty name: ")
    faculty_id = input("Enter faculty ID: ")
    department = input("Enter department: ")

    teacher = [name, faculty_id, department]
    faculty.append(teacher)

    print("Faculty added successfully!")


def view_faculty():
    print("\n--- Faculty Records ---")

    if len(faculty) == 0:
        print("No faculty records found.")
    else:
        for teacher in faculty:
            print("Name:", teacher[0])
            print("Faculty ID:", teacher[1])
            print("Department:", teacher[2])
            print("----------------------")


# ================= COURSE MANAGEMENT ======================

def add_course():
    print("\n--- Add Course ---")

    code = input("Enter course code: ")
    name = input("Enter course name: ")
    teacher = input("Enter faculty name: ")

    course = [code, name, teacher]
    courses.append(course)

    print("Course added successfully!")


def view_courses():
    print("\n--- Course Records ---")

    if len(courses) == 0:
        print("No course records found.")
    else:
        for course in courses:
            print("Course Code:", course[0])
            print("Course Name:", course[1])
            print("Faculty:", course[2])
            print("----------------------")


# ================= ATTENDANCE MANAGEMENT ==================

def add_attendance():
    print("\n--- Add Attendance ---")

    name = input("Enter student name: ")
    total = int(input("Enter total classes: "))
    present = int(input("Enter classes attended: "))

    percentage = (present / total) * 100

    record = [name, total, present, percentage]
    attendance.append(record)

    print("Attendance added successfully!")
    print("Attendance Percentage:", round(percentage, 2), "%")


def view_attendance():
    print("\n--- Attendance Records ---")

    if len(attendance) == 0:
        print("No attendance records found.")
    else:
        for record in attendance:
            print("Student:", record[0])
            print("Total Classes:", record[1])
            print("Classes Attended:", record[2])
            print("Attendance:", round(record[3], 2), "%")
            print("----------------------")


# ================= EXAMINATION MANAGEMENT =================

def add_marks():
    print("\n--- Add Examination Marks ---")

    name = input("Enter student name: ")
    subject = input("Enter subject: ")
    score = float(input("Enter marks out of 100: "))

    if score >= 90:
        grade = "A+"
    elif score >= 75:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 40:
        grade = "C"
    else:
        grade = "Fail"

    record = [name, subject, score, grade]
    marks.append(record)

    print("Marks added successfully!")
    print("Grade:", grade)


def view_marks():
    print("\n--- Examination Records ---")

    if len(marks) == 0:
        print("No examination records found.")
    else:
        for record in marks:
            print("Student:", record[0])
            print("Subject:", record[1])
            print("Marks:", record[2])
            print("Grade:", record[3])
            print("----------------------")


# ================= FEES MANAGEMENT ========================

def add_fee():
    print("\n--- Add Fee Record ---")

    name = input("Enter student name: ")
    total = float(input("Enter total fee: "))
    paid = float(input("Enter amount paid: "))

    balance = total - paid

    if balance <= 0:
        status = "Paid"
    else:
        status = "Pending"

    record = [name, total, paid, balance, status]
    fees.append(record)

    print("Fee record added successfully!")


def view_fees():
    print("\n--- Fee Records ---")

    if len(fees) == 0:
        print("No fee records found.")
    else:
        for record in fees:
            print("Student:", record[0])
            print("Total Fee:", record[1])
            print("Amount Paid:", record[2])
            print("Balance:", record[3])
            print("Status:", record[4])
            print("----------------------")


# ================= TIMETABLE MANAGEMENT ===================

def add_class():
    print("\n--- Add Class ---")

    day = input("Enter day: ")
    time = input("Enter time: ")
    subject = input("Enter subject: ")
    room = input("Enter room number: ")

    record = [day, time, subject, room]
    timetable.append(record)

    print("Class added successfully!")


def view_timetable():
    print("\n--- College Timetable ---")

    if len(timetable) == 0:
        print("No timetable records found.")
    else:
        for record in timetable:
            print("Day:", record[0])
            print("Time:", record[1])
            print("Subject:", record[2])
            print("Room:", record[3])
            print("----------------------")


# ================= MAIN MENU ==============================

while True:

    print("\n")
    print("================================================")
    print("          COLLEGE MANAGEMENT SYSTEM")
    print("          Registration No: 26MIM10209")
    print("================================================")

    print("1. Student Management")
    print("2. Faculty Management")
    print("3. Course Management")
    print("4. Attendance Management")
    print("5. Examination Management")
    print("6. Fees Management")
    print("7. Timetable Management")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    # Student
    if choice == "1":

        print("\n1. Add Student")
        print("2. View Students")

        option = input("Enter option: ")

        if option == "1":
            add_student()

        elif option == "2":
            view_students()

        else:
            print("Invalid option!")

    # Faculty
    elif choice == "2":

        print("\n1. Add Faculty")
        print("2. View Faculty")

        option = input("Enter option: ")

        if option == "1":
            add_faculty()

        elif option == "2":
            view_faculty()

        else:
            print("Invalid option!")

    # Courses
    elif choice == "3":

        print("\n1. Add Course")
        print("2. View Courses")

        option = input("Enter option: ")

        if option == "1":
            add_course()

        elif option == "2":
            view_courses()

        else:
            print("Invalid option!")

    # Attendance
    elif choice == "4":

        print("\n1. Add Attendance")
        print("2. View Attendance")

        option = input("Enter option: ")

        if option == "1":
            add_attendance()

        elif option == "2":
            view_attendance()

        else:
            print("Invalid option!")

    # Examination
    elif choice == "5":

        print("\n1. Add Marks")
        print("2. View Marks")

        option = input("Enter option: ")

        if option == "1":
            add_marks()

        elif option == "2":
            view_marks()

        else:
            print("Invalid option!")

    # Fees
    elif choice == "6":

        print("\n1. Add Fee")
        print("2. View Fees")

        option = input("Enter option: ")

        if option == "1":
            add_fee()

        elif option == "2":
            view_fees()

        else:
            print("Invalid option!")

    # Timetable
    elif choice == "7":

        print("\n1. Add Class")
        print("2. View Timetable")

        option = input("Enter option: ")

        if option == "1":
            add_class()

        elif option == "2":
            view_timetable()

        else:
            print("Invalid option!")

    # Exit
    elif choice == "8":

        print("\nThank you for using College Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
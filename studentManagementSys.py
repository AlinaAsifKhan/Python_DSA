students = {}  # dictionary to store students with roll number as key

class Student:
    def __init__(self, rollNumber, name, course, grades):
        self.rollNumber = rollNumber
        self.name = name
        self.course = course
        self.grades = grades

        # calculating average here only
        total = 0
        count = 0

        for grade in grades:
            total += grade
            count += 1

        self.avg = total / count if count > 0 else 0

    def __str__(self):
        return f"\nRoll Number: {self.rollNumber} | Name: {self.name} | Course: {self.course} | Grades: {self.grades} | Average: {self.avg:.2f}"

def getInt(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Please enter a valid integer.")

def addStudent():
    while True:
        roll = getInt("Enter roll number: ")

        if roll in students:
            print(f"Roll number '{roll}' already exists! Original student: {students[roll].name}")
            continue

        name = input("Enter name: ").strip()
        course = input("Enter course: ").strip()

        grades_input = input("Enter grades (comma-separated numbers): ").strip()
        try:
            grades = [int(g.strip()) for g in grades_input.split(",")]
        except ValueError:
            print("Grades must be numbers only (e.g., 85, 90, 78).")
            continue

        student = Student(roll, name, course, grades)
        students[roll] = student
        print(f"Student '{name}' with roll number '{roll}' added successfully.")

        cont = input("Add another student? (y/n): ").strip().lower()
        if cont != 'y':
            break

def printStudents():
    if not students:
        print("No students yet.")
    else:
        print("\n --All students (sorted by roll number):--")
        for roll in sorted(students):
            print(students[roll])


def searchStudent():
    roll = getInt("Enter the roll number you want to search: ")
    if roll in students:
        print(students[roll])
    else:
        print(f"Student with roll number {roll} not found.\n")

def updateStudent():
    roll = getInt("Enter the roll number you want to update: ")
    if roll in students:
        student = students[roll]
        print("What do you want to update:")
        print("1. Name")
        print("2. Course")
        print("3. Grades")
        value = input("Enter choice (1-3): ").strip()

        if value == "1":
            student.name = input("Enter new name: ").strip()
        elif value == "2":
            student.course = input("Enter new course: ").strip()
        elif value == "3":
            grades = input("Enter new grades (comma-separated numbers): ").strip()
            try:
                student.grades = [int(g.strip()) for g in grades.split(',')]
                # re-calculate avg after updating grades
                total = sum(student.grades)
                count = len(student.grades)
                student.avg = total / count if count > 0 else 0
            except ValueError:
                print("Grades must be numbers only.")
                return
        else:
            print("Invalid choice. Try again.")
            return

        print(" Updated Successfully.")
        print(" Updated Record:")
        print(students[roll])
    else:
        print("Student not found.")

def deleteStudent():
    roll = getInt("Enter the roll number you want to delete: ")
    if roll in students:
        students.pop(roll)
        print(f"Student with roll number {roll} deleted successfully.")
    else:
        print("Student not found.")

# --- merge sort to sort by average ---
def mergeSort(arr, key=lambda x: x, reverse=False):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergeSort(arr[:mid], key, reverse)
    right = mergeSort(arr[mid:], key, reverse)

    return merge(left, right, key, reverse)

def merge(left, right, key, reverse):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if (key(left[i]) > key(right[j])) if reverse else (key(left[i]) < key(right[j])):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# --- show students sorted by average ---
def topScorerFinder():
    if not students:
        print("No students yet.")
        return

    all_students = list(students.values())# get all student objects
    sorted_students = mergeSort(all_students, key=lambda s: s.avg, reverse=True)

    print("\n-- Top 3 Scorers (Sorted by Average): --")
    for student in sorted_students[:3]:
        print(student)

# -------- Ranking System --------

def getRanking():
    if not students:
        print("No students to rank.")
        return

    student_list = list(students.values())
    sorted_by_avg = mergeSort(student_list, key=lambda s: s.avg, reverse=True)

    print("\n-- Student Rankings (1 = Topper): --")
    for i, student in enumerate(sorted_by_avg):
        print(f"Rank {i+1}: {student.name} (Roll: {student.rollNumber}) - Avg: {student.avg:.2f}")


# === Main Loop ===
while True:
    print("\n=== Student Record System ===")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Print All Students")
    print("5. Delete Student")
    print("6. Top Scorers")
    print("7. Ranking")
    print("8. Exit")
    choice = input("Enter your choice (1-8 .): ").strip()

    if choice == '1':
        addStudent()
    elif choice == '2':
        searchStudent()
    elif choice == '3':
        updateStudent()
    elif choice == '4':
        printStudents()
    elif choice == '5':
        deleteStudent()
    elif choice == '6':
        topScorerFinder()
    elif choice == '7':
        getRanking()
    elif choice == '8':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.\n")

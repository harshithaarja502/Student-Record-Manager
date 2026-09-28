import re
import json
import os
import time

FILE_NAME = "students.json"


# ==============================
# 3D STYLE UI
# ==============================

def line():
    print("╔══════════════════════════════════════════════════╗")


def bottom():
    print("╚══════════════════════════════════════════════════╝")


def title():
    print()
    line()
    print("║        🌐  S T U D E N T   S P H E R E  🌐       ║")
    print("║              3D RECORD MANAGER                  ║")
    bottom()
    print()


# ==============================
# LOAD STUDENTS
# ==============================

def load_students():
    try:
        if not os.path.exists(FILE_NAME):
            return []

        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print("\n⚠️  Error: Student data file is corrupted.")
        return []

    except Exception as e:
        print("\n⚠️  File Error:", e)
        return []


# ==============================
# SAVE STUDENTS
# ==============================

def save_students(students):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(students, file, indent=4)

        return True

    except Exception as e:
        print("\n⚠️  Unable to save data:", e)
        return False


# ==============================
# EMAIL VALIDATION
# ==============================

def validate_email(email):

    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    return re.match(pattern, email) is not None


# ==============================
# ADD STUDENT
# ==============================

def add_student():

    students = load_students()

    print("\n╭─────────────── 👤 ADD STUDENT ───────────────╮")

    try:

        student_id = input("│ Student ID       : ").strip()

        if not student_id:
            raise ValueError("Student ID cannot be empty.")

        # Check duplicate ID
        for student in students:
            if student["id"] == student_id:
                raise ValueError("Student ID already exists.")

        name = input("│ Student Name     : ").strip()

        if not name:
            raise ValueError("Student name cannot be empty.")

        if not name.replace(" ", "").isalpha():
            raise ValueError("Name should contain only alphabets.")

        email = input("│ Email Address    : ").strip()

        if not validate_email(email):
            raise ValueError("Invalid email format.")

        course = input("│ Course           : ").strip()

        if not course:
            raise ValueError("Course cannot be empty.")

        student = {
            "id": student_id,
            "name": name,
            "email": email,
            "course": course
        }

        students.append(student)

        if save_students(students):

            print("\n╰───────────────────────────────────────────────╯")
            print("        ✨ STUDENT ADDED SUCCESSFULLY ✨")
            print("        🌟 Welcome to StudentSphere!")
            print()

    except ValueError as e:

        print("\n❌ Invalid Input:", e)

    except Exception as e:

        print("\n❌ Unexpected Error:", e)


# ==============================
# DISPLAY STUDENTS
# ==============================

def view_students():

    students = load_students()

    print("\n╭──────────── 📚 STUDENT DATABASE ─────────────╮")

    if not students:
        print("│        No student records available.         │")
        print("╰──────────────────────────────────────────────╯")
        return

    for i, student in enumerate(students, start=1):

        print(f"""
│
│  ╭─────── 🎓 STUDENT {i} ───────╮
│  │ ID     : {student['id']}
│  │ Name   : {student['name']}
│  │ Email  : {student['email']}
│  │ Course : {student['course']}
│  ╰────────────────────────────╯
│
""")

    print("╰──────────────────────────────────────────────╯")


# ==============================
# SEARCH STUDENT
# ==============================

def search_student():

    students = load_students()

    print("\n╭────────────── 🔍 SEARCH ──────────────╮")

    try:

        search = input("│ Enter Student ID or Name: ").strip().lower()

        if not search:
            raise ValueError("Search value cannot be empty.")

        found = False

        for student in students:

            if (search == student["id"].lower()
                    or search in student["name"].lower()):

                print("\n│ ✨ Student Found!")
                print("│")
                print("│ ID     :", student["id"])
                print("│ Name   :", student["name"])
                print("│ Email  :", student["email"])
                print("│ Course :", student["course"])

                found = True

        if not found:
            print("\n│ ❌ Student not found.")

    except ValueError as e:
        print("\n│ ⚠️", e)

    print("╰───────────────────────────────────────╯")


# ==============================
# DELETE STUDENT
# ==============================

def delete_student():

    students = load_students()

    print("\n╭────────────── 🗑️ DELETE STUDENT ──────────────╮")

    try:

        student_id = input("│ Enter Student ID: ").strip()

        if not student_id:
            raise ValueError("Student ID cannot be empty.")

        new_students = [
            student for student in students
            if student["id"] != student_id
        ]

        if len(new_students) == len(students):

            print("│ ❌ Student ID not found.")

        else:

            save_students(new_students)

            print("│ ✅ Student deleted successfully.")

    except ValueError as e:

        print("│ ⚠️", e)

    print("╰───────────────────────────────────────────────╯")


# ==============================
# DASHBOARD
# ==============================

def dashboard():

    students = load_students()

    print("\n╭────────────── 📊 3D DASHBOARD ──────────────╮")

    print(f"│ 👨‍🎓 Total Students : {len(students)}")

    if students:

        courses = set(student["course"] for student in students)

        print(f"│ 📚 Total Courses  : {len(courses)}")

        print("│")

        print("│ Available Courses:")

        for course in courses:
            print(f"│   🔹 {course}")

    else:

        print("│ 📚 Total Courses  : 0")

    print("╰──────────────────────────────────────────────╯")


# ==============================
# MAIN MENU
# ==============================

def main():

    while True:

        title()

        print("        ╭──────────────────────────────╮")
        print("        │        🌟 MAIN MENU 🌟       │")
        print("        ├──────────────────────────────┤")
        print("        │  1️⃣  Add Student             │")
        print("        │  2️⃣  View Students            │")
        print("        │  3️⃣  Search Student           │")
        print("        │  4️⃣  Delete Student           │")
        print("        │  5️⃣  Dashboard                │")
        print("        │  6️⃣  Exit                     │")
        print("        ╰──────────────────────────────╯")

        try:

            choice = input("\n        🚀 Enter your choice: ").strip()

            if choice == "1":

                add_student()

            elif choice == "2":

                view_students()

            elif choice == "3":

                search_student()

            elif choice == "4":

                delete_student()

            elif choice == "5":

                dashboard()

            elif choice == "6":

                print("\n        🌐 Closing StudentSphere...")
                time.sleep(1)
                print("        👋 Thank you!")
                break

            else:

                raise ValueError(
                    "Please choose a number between 1 and 6."
                )

        except ValueError as e:

            print("\n        ❌ Invalid Input:", e)

        except KeyboardInterrupt:

            print("\n\n        👋 Program stopped.")
            break

        except Exception as e:

            print("\n        ⚠️ Unexpected Error:", e)


# ==============================
# PROGRAM START
# ==============================

if __name__ == "__main__":
    main()
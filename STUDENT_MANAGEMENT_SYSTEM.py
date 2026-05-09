# STUDENT MANAGEMENT SYSTEM 
STUDENTS = []

print("\n")
print("     =====================================================")
print("     💻 WELCOME! to ADVANCED STUDENT MANAGEMENT SYSTEM 💻")
print("     =====================================================")

while True:

    print('''
        ==============================================
        ||         STUDENT MANAGEMENT SYSTEM        ||
        ==============================================
        ||      1. Add Student                      ||
        ||      2. Show All Students                ||
        ||      3. Search Student                   ||
        ||      4. Update Marks                     ||
        ||      5. Delete Student                   ||
        ||      6. Highest Marks                    ||
        ||      7. Average Marks                    ||
        ||      8. Exit                             ||
        ==============================================
    ''')

    try:
        choice = int(input("Enter any choice (1-8) : "))
    except ValueError:
        print("⚠ Invalid input! Please enter a valid number between 1-8.\n")
        continue

    if choice == 1:
        name = input("Enter student name : ").strip()
        marks = []
        
        while True:
            x = input("Want to add Marks (Y/N OR 1/0) : ").strip()
            if x.lower() not in ["y", "1"]:
                print("Marks entry finished. Returning to main menu...\n")
                break
            try:
                mark = int(input("Enter Marks (0-100) : "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    print("Marks added successfully!")
                else:
                    print("⚠ Marks must be between 0 and 100!")
            except ValueError:
                print("Please enter numeric marks only!")

        STUDENTS.append({
            "Name": name.title(),
            "Marks": marks
        }) 
        print(f"Student '{name.title()}' added successfully!\n")

    elif choice == 2:
        if not STUDENTS:
            print("No student records found!\n")
        else:
            print("\nShowing All Students Records:\n")
            for idx, student in enumerate(STUDENTS, 1):
                print(f"   Student #{idx}")
                print(f"   Name  : {student['Name']}")
                print(f"   Marks : {student['Marks']}")
                print("   ----------------------------------------")
            print()

    elif choice == 3:
        name = input("Enter name to search : ").strip()
        found = False
        for student in STUDENTS:
            if student["Name"].lower() == name.lower():
                found = True
                print(f"\n Student Found: {student['Name']}")
                print(f"   Marks: {student['Marks']}\n")
                break

        if not found:
            print(f" Student '{name}' not found!\n")

    elif choice == 4:
        name = input("Enter student name for marks update : ").strip()
        target_found = None
        
        for student in STUDENTS:
            if student["Name"].lower() == name.lower():
                target_found = student
                break

        if target_found:
            print("\n Current Record:")
            print(f"Name  : {target_found['Name']}")
            print(f"Marks : {target_found['Marks']}")

            while True:
                x = input("\nWant to update Marks (Y/N OR 1/0) : ").strip()
                if x.lower() not in ["y", "1"]:
                    print(" Update process ended.\n")
                    break
                
                try:
                    old_mark = int(input("Enter Old Marks : "))
                    new_mark = int(input("Enter New Marks : "))

                    if old_mark in target_found["Marks"]:
                        idx = target_found["Marks"].index(old_mark)
                        target_found["Marks"][idx] = new_mark
                        print(" Mark updated successfully!")
                    else:
                        print("⚠ Old mark not found in record!")
                except ValueError:
                    print("⚠ Please enter valid integer marks!")

            print(f" Updated Record: {target_found['Marks']}\n")

        else:
            print(f" Student '{name}' not found!\n")

    elif choice == 5:
        name = input("Enter student name to delete : ").strip()
        target = None
        
        for student in STUDENTS:
            if student["Name"].lower() == name.lower():
                target = student
                break

        if target:
            STUDENTS.remove(target)
            print(f"🗑 Student '{name.title()}' deleted successfully!\n")
        else:
            print(" No student found with that name!\n")

    elif choice == 6:
        if not STUDENTS:
            print(" No student data to calculate highest marks.\n")
        else:
            highest = 0
            st_name = None
            for st in STUDENTS:
                for mark in st["Marks"]:
                    if mark > highest:
                        highest = mark
                        st_name = st["Name"]
            print(f" Highest Score is {highest} & belongs to {st_name}\n")

    elif choice == 7:
        if not STUDENTS:
            print(" No student data to calculate average marks.\n")
        else:
            print("\n Student Average Marks:\n")
            for st in STUDENTS:
                if st["Marks"]:
                    total = sum(st["Marks"])
                    avg = total / len(st["Marks"])
                    print(f" {st['Name']} : Marks = {st['Marks']} | Average = {avg:.2f}")
                else:
                    print(f" {st['Name']} : No marks available!")
            print()

    elif choice == 8:
        print("\n💖 Thank you for using STUDENT MANAGEMENT SYSTEM!")
        print(" Exiting... Have a great day!\n")
        break

    else: 
        print("⚠ Invalid choice! Please select from 1 to 8.\n")

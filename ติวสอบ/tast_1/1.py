
def show_menu():
    print(f"{'='*50}")
    print("1 Register Employee")
    print("2 Delete Employee")
    print("3 Show Data Employee")
    print("4 Exit Program")
    choice = input("Please select menu[1-3] :")
    print(f"{'='*50}")
    return choice
 
def write_data_to_file(data):
    with open("employee.txt", "a") as file:
        file.write(data + "\n")


def register_employee():
    print(f"{'register employee':^50}")
    print(f"{'='*50}")
    name = input("Enter Name Surname : ")
    frist_name = name.split()[0]  # split ใช้แยกข้อความยาวๆ ออกเป็นข้อความย่อยๆ แล้วเก็บผลลัพธ์ไว้ในรูปแบบ ลิสต์ (List) ตามตัวคั่น (sep) ที่กำหนด
    last_name = name.split()[-1] # -1 ใช้สำหรับดึงข้อความสุดท้ายจากลิสต์

    id_card = input("Enter ID card [13 digits]: ")
    while True:
        if len(id_card) != 13 or not id_card.isdigit(): # isdigit ตรวจสอบว่าเป็นตัวเลขทั้งหมดหรือไม่
            print("Invalid ID card number. Please enter a 13-digit number.")
            id_card = input("Enter ID card [13 digits]: ")
        else:
            break

    username = f"{frist_name.lower()}.{last_name[0].lower()}"
    password = f"{name[1].lower()}{name[3].upper()}{name[2].upper()}{len(name)}{name[4].lower()}"

    write_data_to_file(f"{frist_name:<5} {last_name:<20} {username:<20} {password:<20} {id_card:<15}")

    print("(Register Complete)")

def delete_employee():
    print(f"{'delete employee':^50}")
    print(f"{'='*50}")
    frist_name = input("Enter name employee to delete")
    with open("employee.txt", "r") as file:
        lines = file.readlines()
    while True:
        with open("employee.txt", "w") as file:
            found = False
            for line in lines:
                if frist_name not in line: # ตรวจสอบว่าชื่อพนักงานที่ต้องการลบไม่อยู่ในบรรทัดนั้น 
                    file.write(line)
                else:
                    found = True
            if found:
                print(f"Employee {frist_name} deleted successfully.")
            else:
                print(f"Employee {frist_name} not found.")
            break

def show_data_employee():
    print(f"{'show data employee':^50}")
    print(f"{'='*50}")
    with open("employee.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())

# main program
while True:
    choice = show_menu()
    if choice == "1":
        register_employee()
    elif choice == "2":
        delete_employee()
    elif choice == "3":
        show_data_employee()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please select a valid option.")
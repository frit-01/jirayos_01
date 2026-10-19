name_list = []
id_card_list = []

print(f"{'='*21}{'Welcome Employee System Program':=^31}{'='*21}")

while True:
    print("1 Register Employee")
    print("2 Delete Employee")
    print("3 Show Data Employee")
    print("4 Exit Program")
    
    choice = input("Please select menu[1-3]: ")
    
    if choice not in ['1', '2', '3', '4']:
        print("Incorrect menu!!\n")
        continue
        
    if choice == '1':
        print(f"{'='*73}")
        print("REGISTER EMPLOYEE")
        print(f"{'='*73}")
        while True:
            full_name = input("Enter Name Surname: ")
            if len(full_name.split()) == 2:
                full_name = full_name.lower()
                first_name, last_name = full_name.split()
                
                if len(first_name) < 5:
                    print("Invalid! Name must have at least 5 characters.")
                    continue
                
                while True:
                    id_number = input("Enter ID card [13 digits]: ")
                    if len(id_number) == 13 and id_number.isdigit():
                        name_list.append(full_name)
                        id_card_list.append(id_number)
                        print("Register Complete\n")
                        break
                    else:
                        print("Invalid ID card")
                break
            else:
                print("Invalid format! Please try again.")

    elif choice == '2':
        print(f"{'='*73}")  
        print("DELETE EMPLOYEE")
        print(f"{'='*73}")
        while True:
            del_name = input("Enter name employee to delete: ")
            del_name = del_name.lower()
            
            if del_name in name_list:
                index = name_list.index(del_name)
                name_list.pop(index)
                id_card_list.pop(index)
                print("Delete Complete\n")
                break
            else:
                print("Invalid name !!")

    elif choice == '3':
        print(f"{'='*73}")
        print("All data display")
        print(f"{'='*73}")
        print(f"{'No.':<5}{'Name':<15}{'Surname':<15}{'Username':<15}{'Password':<10}{'ID Card'}")
        
        for i in range(len(name_list)):
            f_name, l_name = name_list[i].split()
            usr = f"{f_name}.{l_name}"
            pwd = f"{f_name.lower()}{f_name.upper()}{f_name.upper()}{len(name_list[i])}{f_name.lower()}"
            print(f"{i+1:<5}{f_name:<15}{l_name:<15}{usr:<15}{pwd:<10}{id_card_list[i]}")
        print()

    elif choice == '4':
        print(f"{'='*73}")
        print("Program exit.")
        print(f"{'='*73}")
        break

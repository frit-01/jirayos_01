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
        print(f"{'REGISTER EMPLOYEE':^73}")
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
                        print("Register Complete")
                        print(f"{'='*73}")
                        break
                    else:
                        print("Invalid ID card")
                break
            else:
                print("Invalid format! Please try again.")

    elif choice == '2':
        print(f"{'='*73}")
        print(f"{'DELETE EMPLOYEE':^73}")
        print(f"{'='*73}")
        while True:
            del_name = input("Enter name employee to delete : ")
            del_name = del_name.lower()
            
            found_index = -1
            for i in range(len(name_list)):
                if name_list[i].split()[0] == del_name:
                    found_index = i
                    break
            
            if found_index != -1:
                name_list.pop(found_index)
                id_card_list.pop(found_index)
                print("Delete Complete")
                print(f"{'='*73}")
                break
            else:
                print("Invalid name !!")

    elif choice == '3':
        print(f"{'='*73}")
        print(f"{'All data display':^73}")
        print(f"{'='*73}")
        print(f"{'No.':<5}{'Name':<15}{'Surname':<15}{'Username':<15}{'Password':<10}{'ID Card'}")
        
        for i in range(len(name_list)):
            f_name, l_name = name_list[i].split()
            
            usr = f"{f_name}.{l_name[0]}"
            
            char2 = f_name[1].lower()
            char4 = f_name[3].upper()
            char3 = f_name[2].upper()
            total_len = len(name_list[i])
            char5 = f_name[4].lower()
            pwd = f"{char2}{char4}{char3}{total_len}{char5}"
            
            print(f"{i+1:<5}{f_name:<15}{l_name:<15}{usr:<15}{pwd:<10}{id_card_list[i]}")
        print(f"{'='*73}")

    elif choice == '4':
        print(f"{'='*73}")
        print("Program exit.")
        print(f"{'='*73}")
        break

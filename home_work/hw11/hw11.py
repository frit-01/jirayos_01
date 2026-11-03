name_list = []
surname_list = []
id_card_list = []

LINE = "=" * 80


def show_title(title):
    print(LINE)
    print(title.center(80))
    print(LINE)


def make_username(name, surname):
    return name + "." + surname[0]


def make_password(name, surname):
    full_name = name + " " + surname
    return name[1].lower() + name[3].upper() + name[2].upper() + str(len(full_name)) + name[4].lower()


print("Welcome Employee System Program".center(80, "="))

while True:
    print("1 Register Employee")
    print("2 Delete Employee")
    print("3 Show Data Employee")
    print("4 Exit Program")
    choice = input("Please select menu[1-3] : ")

    if choice == "1":
        show_title("REGISTER EMPLOYEE")

        while True:
            parts = input("Enter Name Surname : ").lower().split()
            if len(parts) != 2:
                print("Invalid name surname")
            elif len(parts[0]) < 5:
                print("Name must have at least 5 characters")
            else:
                break

        id_prompt = "Enter ID card [13 digits]: "
        while True:
            id_card = input(id_prompt)
            if len(id_card) == 13 and id_card.isdigit():
                break
            print("Invalid ID card")
            id_prompt = "Enter ID card : "

        name_list.append(parts[0])
        surname_list.append(parts[1])
        id_card_list.append(id_card)
        print("Register Complete")
        print(LINE)

    elif choice == "2":
        show_title("DELETE EMPLOYEE")

        while True:
            del_name = input("Enter name employee to delete : ").lower()
            if del_name in name_list:
                index = name_list.index(del_name)
                name_list.pop(index)
                surname_list.pop(index)
                id_card_list.pop(index)
                print("Delete Complete")
                break
            print("Invalid name !!")
        print(LINE)

    elif choice == "3":
        show_title("SHOW DATA EMPLOYEE")
        print(f"{'No.':<7}{'Name':<13}{'Surname':<19}{'Username':<13}{'Password':<13}{'ID Card'}")

        index = 0
        while index < len(name_list):
            name = name_list[index]
            surname = surname_list[index]
            username = make_username(name, surname)
            password = make_password(name, surname)
            print(f"{index + 1:<7}{name:<13}{surname:<19}{username:<13}{password:<13}{id_card_list[index]}")
            index += 1
        print(LINE)

    elif choice == "4":
        print("Exit Program".center(80, "="))
        break

    else:
        print("Incorrect menu!!")
        print(LINE)

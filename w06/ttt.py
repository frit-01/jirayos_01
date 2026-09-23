print("1. บวก\n2. ลบ\n3. คูณ\n4. หาร\n0. ออก")

while True:
    menu = int(input("Please select a menu option: "))
    while menu < 1 and menu > 4:
        print("Invalid menu")
        menu = int(input("Please select a menu option: "))

    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
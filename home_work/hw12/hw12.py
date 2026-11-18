WIDTH = 50
PI = 22 / 7


def show_menu():
    print("-" * WIDTH)
    print("Menu".center(WIDTH))
    print("-" * WIDTH)
    print(" C : Circle Area")
    print(" T : Triangle Area")
    print(" R : Rectangle Area")
    print(" E : Exit")
    print("-" * WIDTH)


def circle_area(radius):
    return PI * radius * radius


def triangle_area(base, height):
    return 0.5 * base * height


def rectangle_area(width, length):
    return width * length


def show_result(shape, area):
    print("=" * WIDTH)
    print(f"Output of {shape}".center(WIDTH))
    print("-" * WIDTH)
    print()
    print(f"Area of {shape} = {area:.2f}".center(WIDTH))
    print("=" * WIDTH)


while True:
    show_menu()
    menu = input("Enter menu : ").upper()

    if menu == "C":
        radius = float(input("Enter radius : "))
        show_result("Circle", circle_area(radius))
    elif menu == "T":
        base = float(input("Enter base : "))
        height = float(input("Enter height : "))
        show_result("Triangle", triangle_area(base, height))
    elif menu == "R":
        width = float(input("Enter width : "))
        length = float(input("Enter length : "))
        show_result("Rectangle", rectangle_area(width, length))
    elif menu == "E":
        break
    else:
        print("ERROR!!!")

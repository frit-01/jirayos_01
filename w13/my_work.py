def getdata():
    employees = []

    with open("profile.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            employee_id, first_name, last_name, employee_type, salary, sales = line.split()
            salary = int(salary)
            sales = int(sales)
            net_income = salary + (sales * 0.1)

            employees.append({
                "id": employee_id,
                "name": first_name,
                "surname": last_name,
                "type": employee_type,
                "salary": salary,
                "sale": sales,
                "income": int(net_income)
            })

    return employees


def write_employee_file(filename, employee_type, employees):
    selected = [emp for emp in employees if emp["type"] == employee_type]
    total_income = sum(emp["income"] for emp in selected)
    label = "FULLTIME" if employee_type == "F" else "PARTTIME"
    separator = "-" * 55

    lines = []
    lines.append(f"1 | SHOW INCOME EMPLOYEE {label}")
    lines.append("2 | NAME SURNAME SALARY SALE INCOME")
    lines.append(f"3 | {separator}")

    for index, emp in enumerate(selected, start=4):
        lines.append(
            f"{index} | {emp['name']} {emp['surname']} {emp['salary']} {emp['sale']} {emp['income']}"
        )

    line_number = len(selected) + 4
    lines.append(f"{line_number} | {separator}")
    lines.append(f"{line_number + 1} | Total Income = {total_income}")

    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n".join(lines) + "\n")


def writedata2file():
    employees = getdata()
    write_employee_file("fulltime.txt", "F", employees)
    write_employee_file("parttime.txt", "P", employees)


if __name__ == "__main__":
    writedata2file()
    print("Saved fulltime.txt and parttime.txt")


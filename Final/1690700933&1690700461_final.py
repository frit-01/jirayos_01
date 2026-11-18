DATA_FILE = "transactions.txt"
INCOME = "รายรับ"
EXPENSE = "รายจ่าย"


def is_valid_date(value):
    if len(value) != 10:
        return False

    for index in range(len(value)):
        if index == 4 or index == 7:
            if value[index] != "-":
                return False
        elif value[index] < "0" or value[index] > "9":
            return False
    return True


def is_valid_amount(value):
    dot_count = 0
    digit_count = 0

    for character in value:
        if character == ".":
            dot_count += 1
        elif character >= "0" and character <= "9":
            digit_count += 1
        else:
            return False

    if digit_count == 0 or dot_count > 1:
        return False
    return True


def load_transactions():
    transactions = []
    data_file = open(DATA_FILE, "a", encoding="utf-8")
    data_file.close()

    data_file = open(DATA_FILE, "r", encoding="utf-8")
    lines = data_file.readlines()
    data_file.close()

    if len(lines) % 4 != 0:
        print("ไฟล์ข้อมูลไม่ครบถ้วน กรุณาตรวจสอบ transactions.txt")
        return None

    line_number = 0
    transaction_number = 1

    while line_number < len(lines):
        transaction_date = lines[line_number].strip()
        transaction_type = lines[line_number + 1].strip()
        category = lines[line_number + 2].strip()
        amount_text = lines[line_number + 3].strip()

        if not is_valid_date(transaction_date):
            print(f"วันที่ในรายการที่ {transaction_number} ไม่ถูกต้อง")
            return None
        if transaction_type != INCOME and transaction_type != EXPENSE:
            print(f"ประเภทในรายการที่ {transaction_number} ไม่ถูกต้อง")
            return None
        if category == "":
            print(f"หมวดหมู่ในรายการที่ {transaction_number} ว่างเปล่า")
            return None
        if not is_valid_amount(amount_text):
            print(f"จำนวนเงินในรายการที่ {transaction_number} ไม่ถูกต้อง")
            return None
        if float(amount_text) <= 0:
            print(f"จำนวนเงินในรายการที่ {transaction_number} ต้องมากกว่า 0")
            return None

        transaction = (
            transaction_date,
            transaction_type,
            category,
            float(amount_text),
        )
        transactions.append(transaction)
        line_number += 4
        transaction_number += 1

    return transactions


def save_transactions(transactions):
    data_file = open(DATA_FILE, "w", encoding="utf-8")

    for transaction in transactions:
        data_file.write(transaction[0] + "\n")
        data_file.write(transaction[1] + "\n")
        data_file.write(transaction[2] + "\n")
        data_file.write(f"{transaction[3]:.2f}\n")

    data_file.close()


def read_date():
    while True:
        transaction_date = input("วันที่ (YYYY-MM-DD): ").strip()
        if is_valid_date(transaction_date):
            return transaction_date
        print("กรุณากรอกวันที่รูปแบบ YYYY-MM-DD")


def read_category():
    while True:
        category = input("หมวดหมู่: ").strip()
        if category != "":
            return category
        print("หมวดหมู่ห้ามเว้นว่าง")


def read_amount():
    while True:
        amount_text = input("จำนวนเงิน: ").strip()
        if not is_valid_amount(amount_text):
            print("กรุณากรอกจำนวนเงินเป็นตัวเลข")
        elif float(amount_text) <= 0:
            print("จำนวนเงินต้องมากกว่า 0")
        else:
            return float(amount_text)


def create_transaction(transaction_type):
    print(f"\nเพิ่ม{transaction_type}")
    transaction_date = read_date()
    category = read_category()
    amount = read_amount()
    return (transaction_date, transaction_type, category, amount)


def show_transactions(transactions):
    if len(transactions) == 0:
        print("\nยังไม่มีรายการ")
    else:
        print("\nลำดับ | วันที่      | ประเภท | หมวดหมู่ | จำนวนเงิน")
        print("-" * 60)

        number = 0
        while number < len(transactions):
            transaction = transactions[number]
            print(
                f"{number + 1} | {transaction[0]} | {transaction[1]} | "
                f"{transaction[2]} | {transaction[3]:.2f}"
            )
            number += 1


def show_summary(transactions):
    total_income = 0
    total_expense = 0
    expense_categories = []
    expense_totals = []

    for transaction in transactions:
        if transaction[1] == INCOME:
            total_income += transaction[3]
        else:
            total_expense += transaction[3]
            category_index = 0

            while category_index < len(expense_categories):
                if expense_categories[category_index] == transaction[2]:
                    expense_totals[category_index] += transaction[3]
                    break
                category_index += 1

            if category_index == len(expense_categories):
                expense_categories.append(transaction[2])
                expense_totals.append(transaction[3])

    print("\nสรุปบัญชี")
    print(f"รายรับรวม: {total_income:.2f} บาท")
    print(f"รายจ่ายรวม: {total_expense:.2f} บาท")
    print(f"เงินคงเหลือ: {total_income - total_expense:.2f} บาท")

    print("\nรายจ่ายแยกตามหมวดหมู่")
    if len(expense_categories) == 0:
        print("ยังไม่มีรายการรายจ่าย")
    else:
        category_index = 0
        highest_index = 0

        while category_index < len(expense_categories):
            print(
                f"{expense_categories[category_index]}: "
                f"{expense_totals[category_index]:.2f} บาท"
            )
            if expense_totals[category_index] > expense_totals[highest_index]:
                highest_index = category_index
            category_index += 1

        print(
            f"หมวดหมู่ที่ใช้จ่ายมากที่สุด: {expense_categories[highest_index]} "
            f"({expense_totals[highest_index]:.2f} บาท)"
        )


def read_transaction_number(transaction_count):
    while True:
        value = input("กรอกเลขรายการที่ต้องการลบ (0 เพื่อยกเลิก): ").strip()
        is_number = value != ""

        for character in value:
            if character < "0" or character > "9":
                is_number = False

        if not is_number:
            print("กรุณากรอกเลขลำดับเป็นจำนวนเต็ม")
        elif int(value) == 0:
            return None
        elif int(value) >= 1 and int(value) <= transaction_count:
            return int(value) - 1
        else:
            print(f"กรุณากรอกเลขระหว่าง 1 ถึง {transaction_count} หรือ 0 เพื่อยกเลิก")


def main():
    transactions = load_transactions()
    if transactions is None:
        return

    while True:
        print("\n=== ระบบจดบัญชีรายรับรายจ่าย ===")
        print("1. เพิ่มรายรับ")
        print("2. เพิ่มรายจ่าย")
        print("3. แสดงรายการทั้งหมด")
        print("4. ลบรายการ")
        print("5. สรุปบัญชี")
        print("0. ออกจากโปรแกรม")
        choice = input("เลือกเมนู: ").strip()

        if choice == "1":
            transaction = create_transaction(INCOME)
            transactions.append(transaction)
            save_transactions(transactions)
            print("บันทึกรายการเรียบร้อย")
        elif choice == "2":
            transaction = create_transaction(EXPENSE)
            transactions.append(transaction)
            save_transactions(transactions)
            print("บันทึกรายการเรียบร้อย")
        elif choice == "3":
            show_transactions(transactions)
        elif choice == "4":
            if len(transactions) == 0:
                print("\nยังไม่มีรายการให้ลบ")
            else:
                show_transactions(transactions)
                number = read_transaction_number(len(transactions))
                if number is not None:
                    transactions.pop(number)
                    save_transactions(transactions)
                    print("ลบรายการเรียบร้อย")
        elif choice == "5":
            show_summary(transactions)
        elif choice == "0":
            print("ปิดโปรแกรม")
            break
        else:
            print("ไม่มีเมนูนี้ กรุณาเลือกใหม่")


main()
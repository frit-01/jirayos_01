from pathlib import Path

SOURCE_FILE = Path("student_data.txt")
MALE_FILE = Path("male.txt")
FEMALE_FILE = Path("female.txt")

if not SOURCE_FILE.exists():
    print(f"ไม่พบไฟล์ {SOURCE_FILE}")
else:
    male_count = 0
    female_count = 0
    skipped_lines = 0

    with open(SOURCE_FILE, "r", encoding="utf-8") as source:
        with open(MALE_FILE, "a", encoding="utf-8") as male_file:
            with open(FEMALE_FILE, "a", encoding="utf-8") as female_file:
                while True:
                    line = source.readline()

                    if line == "":
                        break

                    clean_line = line.strip()

                    if clean_line == "":
                        skipped_lines += 1
                        continue

                    parts = clean_line.split(" ")

                    if len(parts) != 7:
                        skipped_lines += 1
                        continue

                    gender = parts[6].upper()

                    if gender == "M":
                        male_file.write(clean_line + "\n")
                        male_count += 1
                    elif gender == "F":
                        female_file.write(clean_line + "\n")
                        female_count += 1
                    else:
                        skipped_lines += 1

    print(f"male.txt   : {male_count} records")
    print(f"female.txt : {female_count} records")
    print(f"skipped    : {skipped_lines} lines")

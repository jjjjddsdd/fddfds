def read_from_files(f) -> list[str]:
    file = open(f, "r", encoding="utf8")
    file_lines = file.readlines()
    return file_lines


def parse_report_lines(lines) -> list[dict[str, str]]:
    data = []
    for l in lines:
        data.append(l[:-1].split("\t"))
    keys, values = data[0], data[1:]
    parsed_lines = []
    for v in values:
        parsed_lines.append(dict(zip(keys, v)))
    return parsed_lines


def calculate_expenses(parsed_lines) -> dict[str, float]:
    total_expenses = 0
    for e in parsed_lines:
        total_expenses += float(e["Сума"])

    expenses_by_kiosks = {"Сума": total_expenses}
    return expenses_by_kiosks


def main():
    file_lines = read_from_files("kiosk2.txt")
    expenses = parse_report_lines(file_lines)
    expenses_by_kiosks = calculate_expenses(expenses)
    print(expenses_by_kiosks)


main()

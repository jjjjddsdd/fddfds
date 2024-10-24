def main() -> None:
    time = convert(input("Enter time: "))
    if 7 <= time <= 8.5:
        print("Зараз сніданок")
    elif 12 <= time <= 13:
        print("Зараз обід")
    elif 18 <= time <= 19:
        print("Зараз вечеря")


def convert(time: str) -> float:
    try:
        h, m = time.split(":")
        if len(m) != 2:
            raise ValueError
        h, m = int(h), int(m)
        m = m / 60
        if 0 <= m <= 1:
            return h+m
        raise ValueError
    except ValueError:
        return 0


if __name__ == "__main__":
    while True:
        main()
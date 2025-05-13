from delivery import calculate_price


def main():
    print("Давайте посчитаем доставку")
    result = calculate_price()
    print("Доставка равна ", result)


if __name__ == "__main__":
    main()

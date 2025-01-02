def two_sum_hashed(lst, target):
    mas = {}

    for i, num in enumerate(lst):
        complement = target - num
        if complement in mas:
            return [mas[complement], i]
        mas[num] = i

    return None


# Пример использования
def main():
    lst = [2, 7, 11, 15]
    target = 9
    print(two_sum_hashed(lst, target))  # Вывод: [0, 1]

if __name__ == "__main__":
    main()
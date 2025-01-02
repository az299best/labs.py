def two_sum(lst, target):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                return (min(i, j), max(i, j))
def main():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 8
    result = two_sum(lst, target)
    print(result)
if __name__ == "__main__":
    main()
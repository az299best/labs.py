def guess_number(number, low, high):
    count = 0
    while low <= high:
        mid = (low + high) // 2
        count += 1
        if mid == number:
            return mid, count
        elif mid < number:
            low = mid + 1
        else:
            high = mid - 1


number = 42
low = 1
high = 100

guessed_number, attempts = guess_number(number, low, high)

print(f"Загаданное число: {number}")
print(f"Угаданное число: {guessed_number}")
print(f"Количество попыток: {attempts}")
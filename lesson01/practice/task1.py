def even_numbers(n):
    list_numbers = [number for number in range(n + 1)]
    return list_numbers[::2]

print(even_numbers(30))
print(even_numbers(19))

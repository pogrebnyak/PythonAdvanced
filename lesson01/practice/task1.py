def even_numbers(n):
    return [number for number in range(n + 1)][::2]

print(even_numbers(30))
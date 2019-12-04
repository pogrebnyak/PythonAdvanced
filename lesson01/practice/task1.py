def even_nambers(n):
    return [even_namber for even_namber in range(n + 1)][::2]

print(even_nambers(30))
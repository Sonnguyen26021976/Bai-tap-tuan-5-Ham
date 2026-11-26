def swap(a, b) -> Tuple[int, int]:
    a = a ^ b
    b = a ^ b
    a = a^ b
    return a, b

a = 9
b = 6
print(swap(a, b))
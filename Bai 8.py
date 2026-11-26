def khoang_cach_Hamming(x, y):
    a = bin(x)[2:]
    b = bin(y)[2:]
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    khoang_cach = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            khoang_cach += 1
    return khoang_cach


x = int(input())
y = int(input())
print(khoang_cach_Hamming(x, y))
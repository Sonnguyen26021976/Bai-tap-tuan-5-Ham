def tim_vi_tri(lst, k):
    for i in range(len(lst)):
        if lst[i] == k:
            return i
    return -1

lst = list(map(int, input().split()))
k = int(input())
print(tim_vi_tri(lst, k))
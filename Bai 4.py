def Kiem_tra_so_hoan_hao(n) :
    sum = 0
    for i in range(1,n) :
        if n % i == 0 :
            sum = sum + i
    if sum == n :
        return "La so_hoan_hao"
    else :
        return "Khong La so_hoan_hao"


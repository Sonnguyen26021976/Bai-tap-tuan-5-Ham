def Kiem_tra_so_nguyen_to(n) :
    so_lan = 0
    for i in range(1,n+1) :
        if n % i == 0 :
            so_lan = so_lan + 1
    if so_lan == 2 :
        return "La so nguyen to"
    else :
        return "Khong la so nguyen to "

a = 5
print(Kiem_tra_so_nguyen_to(a))
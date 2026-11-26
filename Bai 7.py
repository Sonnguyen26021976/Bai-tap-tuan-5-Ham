def may_tinh(num1, num2, operat):
    if operat == '+':
        return  num1 + num2
    elif operat == '-':
        return   num1 - num2
    elif operat == '*':
        return  num1 * num2
    elif operat == '/':
        if num2 == 0:
            return "Loi chia cho 0"
        res = num1 / num2
    else:
        return "Toan tu khong hop le"

    return round(res, 2)

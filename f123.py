

def fun(n):
    if n < 0:
        return "Hisoblanmaydi"
    elif n == 0:
        return 1
    else:
        s = 1
        for i in range(1, n + 1):
            s =s * i
        return s
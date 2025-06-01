def f(n):
    if n < 0:
        return "Hisoblanmaydi"
    elif n == 0:
        return 1
    else:
        s = 1
        for i in range(1, n + 1):
            s =s * i
        return s
print('C(n,k)')

i=input('input n,k: ')
n=int(i[0])
k=int(i[2])
print(f(n)/(f(k)*f(n-k)))
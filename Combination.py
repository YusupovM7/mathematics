from f123 import fun
print('C(n,k)')

i=input('input n,k: ')
n=int(i[0])
k=int(i[2])
print(fun(n)/(fun(k)*fun(n-k)))
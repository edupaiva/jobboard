tvalor = 0
#valor = int(input('Digite um valor'))
i=0

while i < 20 :
    valor = int(input('Digite um valor'))
    
    if valor == -1:
        break

    tvalor = tvalor+valor
    i += 1

print(tvalor)
print("="*30)

inicio = 10
fim    = 20
passo  = 3
for i in range(inicio, fim, passo):
    print( i )
print("="*30)

primos = [2, 3, 5, 7, 11, 13]
for i in range(len(primos)):
    print( "%d: %d"%(i,primos[i]) )

v1 = 
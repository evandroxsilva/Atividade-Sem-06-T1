def notas(x, y, z):
    nota1=x
    nota2=y
    nota3=z
    media=(x+y+z)/3
    if z >8:
        return media+1
    else:
        return media


n1=int(input())
n2=int(input())
n3=int(input())

if notas(n1, n2, n3)>10:
    print('10')
else:
        print(notas(n1, n2, n3))

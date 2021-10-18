def sexo(n):
    if n == 1:
        return 'Ilmo Sr.'
    elif n ==2:
        return 'Ilma Sra.'


nome=input()
inf_sex=int(input())
result=sexo(inf_sex)
print(f'{result} {nome}')

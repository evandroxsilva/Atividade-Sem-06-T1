def cor(n):
    if n.upper()=='V':
        return 'Siga'
    elif n.upper()=='A':
        return 'Atenção'
    elif n.upper()=='E':
        return 'Pare'


sinal=input()
result=cor(sinal)
print(result)
    

import re

def infixa_para_posfixa(expressao):

    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0} 

    pilha = []  
    saida = []
    
    tokens = re.findall(r'[a-zA-Z]+|[()+\-*/]', expressao) 
    for token in tokens:
        if token.isalpha(): 
            saida.append(token)
        elif token == '(': 
            pilha.append(token)
        elif token == ')': 
            while pilha and pilha[-1] != '(':
                saida.append(pilha.pop())
            pilha.pop()           

        else:                                                 
            while pilha and precedencia[pilha[-1]] >= precedencia[token]:
                saida.append(pilha.pop())
            pilha.append(token)
    while pilha:
        saida.append(pilha.pop())
    return ' '.join(saida)

expressao = "(a + b) * c "
resultado = infixa_para_posfixa(expressao)
print(resultado)
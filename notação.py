import re

def infixa_para_posfixa(expressao):
    
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0} 
    
    pilha = []  
    saida = []

    # Divide a expressão em tokens

    tokens = re.findall(r'[a-zA-Z]+|[()+\-*/]', expressao)  # Regex para capturar operandos e operadores

    for token in tokens:
        if token.isalpha():             # Se for operando, adiciona à saída
            saida.append(token)

        elif token == '(':               # Se for '(', empilha
            pilha.append(token)


        elif token == ')':                             # Se for ')', desempilha até encontrar '('
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

# Testando a função com a expressão fornecida
expressao = "a + b * c - (d + e * f) * g"
resultado = infixa_para_posfixa(expressao)
print(resultado)   

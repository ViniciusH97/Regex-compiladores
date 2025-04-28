import re
import os

def infixa_para_posfixa_passo_a_passo(expressao):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    
    pilha = []   
    saida = []  
    
    print(f"Expressão: {expressao}")
    
    input("Pressione Enter para começar")
    os.system('clear')
    
    print("Tokenizando a expressão\n")
    tokens = re.findall(r'[a-zA-Z]+|[()+\-*/]', expressao) 
    print(f"Tokens: {tokens}")
    input("Pressione Enter para continuar...")
    os.system('clear')
    
    for token in tokens:
        print(f"Tokens: {tokens}")
        print(f"\nToken atual: '{token}'")
        
        if token.isalpha(): 
            saida.append(token)
            print(f"  '{token}' é um operando (letra) -> adicionado diretamente à saída")
            
        elif token == '(': 
            pilha.append(token)
            print(f"  '{token}' é um parêntese aberto -> empilhado")
            
        elif token == ')': 
            print(f"  '{token}' é um parêntese fechado -> desempilhando até encontrar '('")
            while pilha and pilha[-1] != '(':
                operador = pilha.pop()
                saida.append(operador)
                print(f"    Desempilhando '{operador}' para a saída")
            
            if pilha:
                print(f"    Descartando '{pilha[-1]}' (parêntese aberto)")
                pilha.pop()
            else:
                print("    Erro: parêntese não balanceado!")
                    
        else:  
            print(f"  '{token}' é um operador")
            while pilha and pilha[-1] != '(' and precedencia.get(pilha[-1], 0) >= precedencia.get(token, 0):
                operador = pilha.pop()
                saida.append(operador)
                print(f"    '{operador}' tem precedência maior ou igual → desempilhado para a saída")
            
            pilha.append(token)
            print(f"    '{token}' empilhado")
        
        print(f"  Pilha: {pilha}")
        print(f"  Saída: {saida}")
        input("Pressione Enter para continuar...")
        os.system('clear')
    
    print(f"Tokens: {tokens}")
    print("\nProcessando operadores restantes na pilha:")
    
    while pilha:
        operador = pilha.pop()
        saida.append(operador)
        print(f"  Desempilhando '{operador}' para a saída")
        print(f"  Pilha: {pilha}")
        print(f"  Saída: {saida}")
        input("Pressione Enter para continuar...")
        os.system('clear')
    
    resultado = ' '.join(saida)
    print(f"\nResultado final (notação pós-fixa): {resultado}")
    
    return resultado

def main():
    
    while True:
        expressao = input("\nDigite uma expressão em notação infixa digite ou sair para encerrar: ")
        
        if expressao.lower() == 'sair':
            break
            
        if not expressao.strip():
            print("Expressão vazia! Tente novamente.")
            continue
            
        else:
            os.system('clear')
            infixa_para_posfixa_passo_a_passo(expressao)
        

if __name__ == "__main__":
    main()
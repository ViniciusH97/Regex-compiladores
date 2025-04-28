# Regex

Regex, ou expressão regular, é uma sequência de caracteres que define um padrão de busca. Em outras palavras, é uma "linguagem" usada para encontrar, validar ou manipular textos que seguem um padrão específico, como números de telefone, endereços de e-mail, datas etc.

Nos compiladores, Regex é muito útil na fase de análise léxica, quando o código fonte é dividido em partes menores chamadas "tokens". Esses tokens representam palavras-chave, identificadores, números, operadores, etc. Usando expressões regulares, os compiladores conseguem reconhecer padrões de forma rápida e precisa.

## Como a Regex funciona - exemplos práticos

Uma Regex funciona comparando uma string de texto com um padrão predefinido. Veja alguns exemplos:

1. Validar um e-mail: `/^[\w.-]+@[\w.-]+\.\w{2,}$/`
2. Encontrar datas no formato dia/mês/ano: `/\b\d{2}\/\d{2}\/\d{4}\b/`
3. Verificar um CPF: `/^\d{3}\.\d{3}\.\d{3}-\d{2}$/`

## Cada símbolo tem um significado:
- `\w` : qualquer letra maiúscula ou minúscula, digitos numéricos (0-9) e underline `_`.
- `\d` : representa um dígito (0-9).
-  `+` : significa "uma ou mais ocorrências".
-  `.`  : representa qualquer caractere.
-  `\` : é usado para "escapar" caracteres especiais.

## Expressão Regular para Reconhecimento de Número de Telefone no Formato Brasileiro
### Descrição do que foi feito

Neste trabalho desenvolvemos uma página web que realiza uma verificação de número de telefone no formato brasileiro, ou seja, ele deve respeitar o código de discagem +55, o DDD (Discagem Direta à Distância) com o uso dos parênteses, os espaços, o 9 obrigatório para celular seguido dos oitos dígitos separados por um hífen . Então, o código deve validar o formato do núemro, retornando se é válido ou inválido, essa verificação foi realizada utilizando o seguinte Regex (expressão regular):

Regex: `/^\+55\s\(\d{2}\)\s9\d{4}-\d{4}$/`

**Explicando a regex:**

- `^` = Início da string.
- `\+55` = Texto literal `+55`.
- `\s` = Um espaço.
- `\(\d{2}\)` = Dois dígitos dentro de parênteses (DDD).
- `\s` = Mais um espaço.
- `9\d{4}` = O dígito 9 seguido de quatro dígitos.
- `-` = Um traço.
- `\d{4}`= Quatro dígitos.
- `$` = Fim da String.

### O que a função validartelefone faz?

1. Pega o valor digitado pelo usuário.
2. Cria a expressão regular que define o formato aceito.
3. Testa se o número e bate com o padrão.
4. Exibe uma mensagem em verde ou vermelho dependendo do resultado.

Exemplo de número válido: `+55 (11) 91234-5678`

Exemplos de números inválidos: `+55 (35)99135-3452`; `+55 35 94721-2345`; `(11) 991064-3453`.

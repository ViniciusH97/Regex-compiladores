# Regex

Regex, ou expressão regular, é uma sequência de caracteres que define um padrão de busca. Em outras palavras, é uma "linguagem" usada para encontrar, validar ou manipular textos que seguem um padrão específico, como números de telefone, endereços de e-mail, datas etc.

Nos compiladores, Regex é muito útil na fase de análise léxica, quando o código fonte é dividido em partes menores chamadas "tokens". Esses tokens representam palavras-chave, identificadores, números, operadores, etc. Usando expressões regulares, os compiladores conseguem reconhecer padrões de forma rápida e precisa.

## Como a Regex funciona - exemplos práticos

Uma Regex funciona comparando uma string de texto com um padrão predefinido. Veja alguns exemplos:

1. Validar um e-mail: `/^[\w.-]+@[\w.-]+\.\w{2,}$/`
2. Encontrar datas no formato dia/mês/ano: `/\b\d{2}\/\d{2}\/\d{4}\b/`
3. Verificar um CPF: `/^\d{3}\.\d{3}\.\d{3}-\d{2}$/`

## Cada símbolo tem um significado:

- `\d` : representa um dígito (0-9).
-  `+` : significa "uma ou mais ocorrências".
-  `.`  : representa qualquer caractere.
-  `\` : é usado para "escapar" caracteres especiais.

## Descrição do que foi feito

Foi criada uma página web em HTML com um campo de entrada para digitar um número de telefone no padrão brasileiro. Para validar o telefone, foi utilizada a seguinte expressão regular:

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

O usuário digita o número, clica no botão e o sistema informa se o formato é válido ou inválido, de forma simples e didática.

Exemplo de número válido: `+55 (11) 91234-5678`

Essa implementação mostra, na prática, como uma Regex pode ser usada para validar formatos específicos de texto, facilitando o tratamento de dados em aplicações web e sistemas em geral.

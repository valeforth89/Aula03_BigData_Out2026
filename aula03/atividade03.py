# input = entrada
# print = saída
# print (f) = concatenar saída de texto com variável
# int () = converte entrada para int (Inteiro)
# type = retorna o tipo da variável
# variavel:.2f = limita a saída dos caracteres para, no exemplo, 2 casas decimais

# Tipos de variáveis:
    # int = número inteiro (ex.: idade = 18)
    # float = número real/fracionário (ex.: Altura = 1.79)
    # str = string texto (ex.: "TEXTO")
    # boolean = válores lógicos (ex.: TRUE ou FALSE)

# Calculadora
#Crie um algoritmo que receba dois números e apresente na tela os resultados das operações de soma, subtração, multiplicação e divisão. 

# Entrada
num1 = float(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

#Processamento
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

# Saída
print (f"\nSoma: {soma} \nSubtração: {subtracao} \nMultiplicação: {multiplicacao} \nDivisão: {divisao}")
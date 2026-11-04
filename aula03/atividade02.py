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

# Boletim Escolar
#Crie um algoritmo que receba duas notas de um aluno, calcule a média final e apresente na tela as duas notas e a média obtida. 

# Entrada
nota1 = float(input("Informe a nota 1: "))
nota2 = int(input("Informe a nota 2: "))

#Processamento
media = (nota1 + nota2) / 2

# Saída
print (f"\nA nota 1 foi: {nota1} \nA nota 2 foi: {nota2} \nA média das noas foi: {media}")
#codigos para inciciar github
    # git init
    # git config user.name valeforth89
    # git config user.email miguelcrdia@gmail.com   
    # git remote add origin https://github.com/valeforth89/Aula03_BigData_Out2026.git
    # git branch -M main
    # git status | obs.: conteúdo em vermelho é não reconhecido / não encontrado
    # git add . > adiciona tudo o que está no diretório
    # git commit | -m indica que vai colocar uma mensagem
    # $ git push origin main | origin indica que é na internet/nuvem

# Cálculo de aumento salarial


# Entrada
sal_atual = float(input("Informe o salário atual: "))
aumento_perc = float(input("Informe o percentual do aumento: "))


# Processamento
aumento_perc = aumento_perc / 100
aumento = float(sal_atual * aumento_perc)
novo_sal = float(sal_atual + aumento)

# Saída
print (f"\nSalário atual: R$ {sal_atual} \nCom o aumento de: R$ {aumento:.2f} \nO novo salário será: R$ {novo_sal:.2f}")
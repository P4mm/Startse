prova1 = int(input("Digite a nota da prova 1:"))
trab = int(input("Digite a nota do trabalho:"))
prova2 = int(input("Digite a nota da prova 2:"))

media = ((prova1 * 2) + trab + (prova2 * 2)) / 5

if media >= 6:
    print("Aluno Aprovado!")
else:
    if media >= 3:
        print("Aluno em Recuperação")
    else:
        print("Aluno Reprovado!")

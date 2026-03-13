nota_prova = float(input("Digite sua nota na prova: "))
nota_trabalho = float(input("Digite sua nota no trabalho: "))

media = (nota_prova + nota_trabalho) / 2

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")
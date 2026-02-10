# Inicialização de variáveis
notas = []
soma = 0

# Entrada da primeira nota
nota_aluno = float(input("Digite a nota (-1 para encerrar): "))

# Loop de repetição (até digitar -1)
while nota_aluno != -1:

# Bloco de validação da nota
    if nota_aluno < 0 or nota_aluno > 10:
        print("Inválido")
    else:
        notas.append(nota_aluno)
        soma += nota_aluno

    nota_aluno = float(input("Digite a nota (-1 para encerrar): "))

# Bloco final de processamento
if len(notas) == 0:
    print("Nenhuma nota válida registrada")
else:
    media = soma / len(notas)

    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")


# Relatório final
print("Notas", notas)
print("Média {:.1f}".format(media))
print("Maior nota", max(notas))
print("Menor nota", min(notas))
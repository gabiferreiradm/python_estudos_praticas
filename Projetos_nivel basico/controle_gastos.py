lista = []
soma = 0

valor_gasto = float(input("Digite um valor de gasto (0 para encerrar): "))

# Loop principal: continua até o usuário digitar 0
while valor_gasto != 0:

    # Verifica se o valor informado é válido, maior que zero
    if valor_gasto > 0:
        lista.append(valor_gasto)
        soma += valor_gasto
    # Valores negativos são ignorados
    else: 
        print("Valor inválido")

    valor_gasto = float(input("Digite um valor de gasto (0 para encerrar): "))

# Verifica se houve ao menos um gasto válido registrado
if len(lista) == 0:
    print("Nenhum gasto registrado")
else:
    media = soma / len(lista)

    # Relatório final
    print("Gastos registrados:", len(lista))
    print("Total gasto:", soma)
    print("Menor valor:", min(lista))
    print("Maior valor:", max(lista))
    print("Media:", media)
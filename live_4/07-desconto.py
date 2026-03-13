valores = [19.50, 49.00, 100.00, 15.90, 31.49]

for valor in valores:
    if valor >= 40:
        desconto = valor * 0.05 # 5% de desconto
        valor_com_desconto = valor - desconto
        print(f'Valor original: R$ {valor:.2f} - Valor com desconto: R${valor_com_desconto:.2f}')
    else:
        print(f'Valor original: R$ {valor:.2f} - Sem desconto')
vlr_prod = float(input('Digite o valor do produto: R$'))
vlr_desc = vlr_prod - ((vlr_prod * 5) / 100)
print('O valor era R${:.2f} após o desconto de 5% será de R${:.2f}'.format(vlr_prod, vlr_desc))

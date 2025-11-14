vlr_sal_atual = float(input('Valor do salário atual: R$'))
desc = 15
vlr_sal_aum =vlr_sal_atual + ((vlr_sal_atual * desc) / 100)
print('O salário atual é R${:.2f} com {}% de aumento irá para R${:.2f}.'
      .format(vlr_sal_atual,desc, vlr_sal_aum))
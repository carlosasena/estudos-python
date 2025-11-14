alt = float(input('Digite a altura: '))
lar = float(input('Digite a largura:' ))
area = alt * lar
lit = area / 2
print('altura {:.2f} largura {:.2f} tem uma área de {:.2f}m², necessario de {:.2f}L de trinta.'
      .format(alt, lar, area, lit) )
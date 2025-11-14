#/entrada de dados
vlr = input('Digite um valor qualquer: ')

#/processamento de dados

#/saída de dados
print('O tipo primitivo desse valor é', vlr.isdecimal())
print('Só tem espaço',vlr.isspace())
print('È um número?', vlr.isnumeric())
print('É alfabético?', vlr.isalpha())
print('É alfanumérico?', vlr.isalnum())
print('Está em maiúsculas?', vlr.isupper())
print('Está em minúscula?', vlr.islower())
print('Está capitalizada?', vlr.istitle())


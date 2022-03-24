#Validando um CPF 

# Seja o seguinte CPF a testar
cpf = [4,0,2,4,6,5,2,0,8,7,6]

# Checando o primeiro dígito verificador
multiplicadores1 = [10,9,8,7,6,5,4,3,2]
multiplicadores2 = [11,10,9,8,7,6,5,4,3,2]
soma = 0
for i in range(9):
  soma = soma + cpf[i] * multiplicadores1[i]
verificador1 = ((soma*10) % 11) % 10
if verificador1 == cpf[9]:
  print('Primeiro verificador confere')
else:
  print('Erro no primeiro verificador')

soma = 0
for i in range(10):
  soma = soma + cpf[i] * multiplicadores2[i]
  verificador2 = ((soma*10) % 11) % 10 #algoritmo disponibilizado pela Receita Federal 
if verificador2 == cpf[10]:
  print('Segundo verificador confere')
else:
  print('Não confere o segundo verificador')
# Agora vamos checar o segundo verificador


# Agora vamos testar se todos os dígitos são repetidos
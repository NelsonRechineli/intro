#soma de inteiros
n1 = 5
n2 = 5
print(n1+n2)
print(f"A soma de n1 e n2 é {n1+n2}")

#concatenação de strings
n3 = input("Digite um número: ")
n4 = input("Digite outro número: ")
print (n3+n4)
print(f"A 'soma' vai dar {n3+n4}")

#convertendo string em float
n5 = float(input("Digite um número: "))
n6 = float(input("Digite outro número: "))
print(n5+n6)
print(f"A soma vai dar {n5+n6}")

#uso do float pra números com vírgula. Usar o ponto nolugar da vírgula
altura = float(input("Digite sua altura em metros e centímetros"))
print(f"Sua altura é {altura}")

#uso de string, uma ou duas aspas dá certo
nome = 'Nelson'
nome2 = "Nelson"
print(nome)
print(nome2)
print(nome+nome2)

#recebendo e mostrando uma string
nome3 = input("Qual seu nome?")
print(f"Olá {nome3}")


n7 = float(input("Digite um numero: "))
if n7 > 0:
  print("Numero positivo")
elif n7 < 0:
  print("Numero negativo")
else:
  print("Numero é 0")

#autorização if condição compostapra usuario e senha pra entrar
usuario = input("Usuário: ")
senha = input("Senha: ")

if usuario.lower() == 'nelson' and senha == '1234':
  print("bem vindo {usuario}")
else:
  print("usuario E senha inválidos")


#autorização ifcondições compostas pra usuario e senha pra entrar com and
chocolate1 = input("Chocolate1: ")
chocolate2 = input("Chocolate2: ")
if chocolate1.lower == 'sonho de valsa' or chocolate2 == 'ouro branco':
  print("entre {chocolate1} OU {chocolate2} tanto faz, adoro os dois")
else:
  print("usuario e senha inválidos")

# Exemplo com condições compostas
carteira = 500
compra = 600
cartao_ativo = True

if not (carteira >= compra and cartao_ativo):
  # Compra não autorizada. pouco dinheiro na carteira e cartao nao ta ativo  
  print("Compra não autorizada.") 
else:
    print("Compra autorizada.")


x = 10

if not x > 20:
    print("x não é maior que 20")  
else:
    print("x é maior que 20")

#DESAFIO DIO- CRIANDO UM SISTEMA BANCARIO COM PYTHON
#SISTEMA POR THIAGO NEVES

menu = """
----------------
1 - DEPOSITAR
2 - SACAR
3 - EXTRATO
4 - SAIR
----------------
"""

saldo = 0
extrato = ""
limite_por_saque = 500
LIMITE_DE_SAQUES = 3

#DEPOSITO
def depositar(valor):
	global saldo
	global extrato
	if valor > 0:
		saldo += valor
		extrato += f"Depósito: R${valor:.2f}\n"
		return f"Depósito de R${valor:.2f} realizado com sucesso!"
	else:
		return "Valor de depósito inválido!"

#SAQUE
def sacar(valor):
	global saldo
	global LIMITE_DE_SAQUES
	global extrato
	if valor <= 0:
		return "Valor de saque inválido!"
	if LIMITE_DE_SAQUES <= 0:
		return "Limite de saques excedido!"
	if valor > saldo:
		return "Saldo insuficiente!"
	if valor > limite_por_saque:
		return "Valor do saque excede o limite permitido!"
	
	saldo -= valor
	LIMITE_DE_SAQUES -= 1
	extrato += f"Saque: R${valor:.2f}\n"
	return f"Saque de R${valor:.2f} realizado com sucesso!"

#EXTRATO
def extrato_bancario():
	global extrato
	return f"""
	----------------------------
	EXTRATO
	----------------------------
	{extrato}
	----------------------------
	Saldo Atual: R${saldo:.2f}
	----------------------------
	"""

#MENU
while True:
	print(menu)
	opcao = input("Escolha uma opção: ")
	if opcao == "1":
		valor = float(input("Digite o valor de deposito: "))
		mensagem = depositar(valor)
		print(mensagem)
	elif opcao == "2":
		valor = float(input("Digite o valor de saque: "))
		mensagem = sacar(valor)
		print(mensagem)
	elif opcao == "3":
		print(extrato_bancario())
	elif opcao == "4":
		print("Saindo do sistema...")
		break
	else:
		print("Opção inválida!")

print("Obrigado!")

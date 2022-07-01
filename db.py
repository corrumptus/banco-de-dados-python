import os

def menu_nCad():
	print('1 - Entrar em uma conta')
	print('2 - Entrar como administrador')
	print('3 - Contatos')
	print('4 - Cadastrar uma conta')
	print('5 - Suporte')
	print('0 - Fechar o programa')
	opcao = int(input('Digite a opção desejada\n'))
	return opcao

def menu_Cad():
	print('1 - Ver todo o arquivo')
	print('2 - Ver só os avisos/lembretes')
	print('3 - Ver só o texto')
	print('4 - Editar avisos')
	print('5 - Editar texto')
	print('6 - Entrar na área secreta')
	print('7 - Trocar nome de usuário/senha')
	print('8 - Apagar conta')
	print('9 - Voltar ao menu principal')
	opcao = int(input('Digite a opção desejada\n'))
	return opcao

def menu_Adm():
	print('1 - Ver quantas pessoas estão cadastradas')
	print('2 - Listar pessoas cadastradas')
	print('3 - Adicionar um aviso para todos os usuários')
	print('4 - Modificar o usuário/senha de um usuário')
	print('5 - Remover uma conta')
	print('0 - Sair para o menu principal')
	opcao = int(input('Digite a opção desejada\n'))
	return opcao

def Contatos():
	print('#contato do github')
	print('email: surx42@gmail.com')
	print('telefone: (12) 93456-7810')
	return

def Logar_usuario():

	return

def Cadastra_conta():
	nome = input('Digite o seu nome de usuários\n') #n diferencia letra maiuscula de minuscula, checar existencia do usuário
	if Checa_usu(nome) == False:
		senha = input('Digite a sua senha(não se esqueça dela)\n')
		if len(senha) >= 6:
			senha2 = input('Digite a sua senha novamente(não se esqueça dela)\n')
			if senha == senha2:
				nome_arquivo = nome+','+senha+'.txt'
				arq = open(nome_arquivo, 'w')
				arq.write('-------Avisos/Lembretes-------\n')
				arq.write('------------Texto-------------\n')
				arq.write('---------Área secreta---------\n')
				arq.close()
				tipo = input('Digite um tipo de contato para segurança(email, telefone...)\n')
				contato = input('Digite um contato de segurança\n')
				Adiciona_nome(nome_arquivo, contato, tipo)
			else:
				print('Senhas diferentes, tente novamente')
		else:
			print('Senha muito fraca, tente novamente')
	else:
		print('Esse usuário já existe, tente novamente')
	return

def Carrega_ADM():
	arq = open(arq_adm, 'r')
	arquivo = []
	for i in arq:
		arquivo.append(i.replace('\n',''))
	for i in range(len(arquivo)):
		if arquivo[i] == '-------Contas-------':
			n = i
		if arquivo[i] == '-------Log-------':
			n2 = i
	return arquivo, n, n2

def Checa_usu(nome):
	arq_ADM, n, n2 = Carrega_ADM()
	for i in range(n+1, n2):
		n3 = arq_ADM[i].find(',')
		if arq_ADM[i][0:n3] == nome:
			return True
	return False 

def Suporte():
	usuario = input('Digite o seu nome de usuário\n') #checar se existe
	contato = input('Digite o seu contato cadastrado\n') #checar validade
	a_ADM, n, n2 = Carrega_ADM()
	arq_ADM = open(arq_adm, 'w')
	for i in range(n):
		arq_ADM.write(a_ADM[i])
	arq_ADM.write('o usuário ' + usuario + 'perdeu sua senha. Entrar em contato com o mesmo via: ' + contato + '(' + tipo + ')')
	for i in range(n, len(a_ADM)+1):
		arq_ADM.write(a_ADM[i])
	return

def Adiciona_nome(nome, contato, tipo):
	arq_ADM, n, n2= Carrega_ADM()
	arq = open(arq_adm, 'w')
	for i in range(n):
		arq.write(arq_ADM[i])
	for i in range(n, n2):
		arq.write(arq_ADM[i])
	arq.write(nome + ' || ' + contato + ' || ' + tipo)
	for i in range(n2, len(arq_ADM)+1):
		arq.write(arq_ADM[i])


arq_adm = 'AdminAdmin.txt'
opcao = 1
while opcao != 0:
	opcao = menu_nCad()
	if opcao == 1:
		op = 1
		while op != 0:
			op = menu_Cad()
	elif opcao == 2:
		op = 1
		while op != 0:
			op = menu_Adm()
	elif opcao == 3:
		Contatos()
	elif opcao == 4:
		Cadastra_conta()
	elif opcao == 5:
		Suporte()

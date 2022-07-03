import os

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

def Cadastra_conta():
	nome = input('Digite o seu nome de usuários\n').lower().strip()
	if Checa_usu(nome) == False:
		senha = input('Digite a sua senha(não se esqueça dela)\n').lower().strip()
		if len(senha) >= 6:
			senha2 = input('Digite a sua senha novamente(não se esqueça dela)\n').lower().strip()
			if senha == senha2:
				arq = open(nome + ',' + senha + '.txt', 'w', encoding='utf8')
				arq.write('-------Avisos/Lembretes-------\n')
				arq.write('------------Texto-------------\n')
				arq.write('---------Área secreta---------\n')
				arq.close()
				tipo = input('Digite um tipo de contato para segurança(email, telefone...)\n').strip()
				contato = input('Digite um contato de segurança\n').strip()
				Adiciona_nome(nome + ',' + senha + '.txt', contato, tipo)
			else:
				print('Senhas diferentes, tente novamente')
		else:
			print('Senha muito fraca, tente novamente')
	else:
		print('Esse usuário já existe, tente novamente')
	return

def Carrega_ADM():
	arq = open('AdminAdmin.txt', 'r')
	arquivo = []
	for i in arq:
		arquivo.append(i.replace('\n',''))
	for i in range(len(arquivo)):
		if arquivo[i] == '-------Contas-------':
			n = i
		if arquivo[i] == '-------Log-------':
			n2 = i
	arq.close()
	return arquivo, n, n2

def Checa_usu(nome):
	arq_ADM, n, n2 = Carrega_ADM()
	for i in range(n+1, n2):
		n3 = arq_ADM[i].find(',')
		if arq_ADM[i][0:n3] == nome:
			return True
	return False

def Checa_senha(nome, senha):
	arq_ADM, n, n2 = Carrega_ADM()
	for i in range(n+1, n2):
		n3 = arq_ADM[i].find(',')
		n4 = arq_ADM[i].find('.txt')
		if arq_ADM[i][0:n3] == nome and arq_ADM[i][n3+1:n4] == senha:
			return True
	return False

def Suporte():
	usuario = input('Digite o seu nome de usuário\n').strip() #checar se existe
	contato = input('Digite o seu contato cadastrado\n').strip() #checar validade
	a_ADM, n, n2 = Carrega_ADM()
	arq_ADM = open('AdminAdmin.txt', 'w')
	for i in range(n):
		arq_ADM.write(a_ADM[i])
	arq_ADM.write('o usuário ' + usuario + 'perdeu sua senha. Entrar em contato com o mesmo via: ' + contato + '(' + Acha_tipo(usuario) + ')')
	for i in range(n, len(a_ADM)+1):
		arq_ADM.write(a_ADM[i])
	arq_ADM.write('O usuario ' + usuario + ' pediu ajuda ao suporte')
	arq_ADM.close()
	return

def Adiciona_nome(nome, contato, tipo):
	arq_ADM, n, n2= Carrega_ADM()
	arq = open('AdminAdmin.txt', 'w', encoding='utf8')
	for i in range(n):
		arq.write(arq_ADM[i]+'\n')
	for i in range(n, n2):
		arq.write(arq_ADM[i]+'\n')
	arq.write(nome + ' || ' + contato + ' || ' + tipo + '\n')
	for i in range(n2, len(arq_ADM)):
		arq.write(arq_ADM[i]+'\n')
	arq.write('Novo usuário criado: ' + nome + '\n')
	arq.close()
	log = open('Logs.txt', 'a', encoding='utf8')
	log.write('Novo usuário criado: ' + nome + '\n')
	log.close()

def Acha_tipo(nome):
	arq_ADM, n, n2 = Carrega_ADM()
	for i in range(n+1,n2):
		n3 = arq_ADM[i].find(',')
		if arq_ADM[i][0:n3] == nome:
			for j in range(len(arq_ADM[i])-1, 0, -1):
				if arq_ADM[i][j] == ' ':
					return arq_ADM[i][j+1:]

def Exibir(nome, sec1, sec2, sec3):
	arq = open(nome, 'r')
	arquivo = []
	for i in arq:
		arquivo.append(i.replace('\n',''))
	for i in range(len(arquivo)):
		if arquivo[i] == '------------Texto-------------':
			n = i
		if arquivo[i] == '---------Área secreta---------':
			n2 = i
	for i in range(0*sec1, n*sec1):
		print(arquivo[i])
	for i in range(n*sec2, n2*sec2):
		print(arquivo[i])
	for i in range(n2*sec3, len(arquivo)*sec3):
		print(arquivo[i])
	return

def main():
	opcao = 1
	while opcao != 0:
		print('1 - Entrar em uma conta')
		print('2 - Entrar como administrador')
		print('3 - Contatos')
		print('4 - Cadastrar uma conta')
		print('5 - Suporte')
		print('0 - Fechar o programa')
		opcao = int(input('Digite a opção desejada\n'))
		if opcao == 1:
			main_logar()
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
	return

def main_logar():
	nome = input('Digite o seu nome de usuário\n').strip().lower()
	senha = input('Digite a sua senha\n').strip().lower()
	if Checa_senha(nome, senha) == True:
		opcao = 1
		arquivo = nome + ',' + senha + '.txt'
		while opcao != 0:
			print('1 - Ver todo o arquivo')
			print('2 - Ver só os avisos/lembretes')
			print('3 - Ver só o texto')
			print('4 - Editar avisos') ##
			print('5 - Editar texto') ##
			print('6 - Entrar na área secreta')
			print('7 - Solicitar suporte') ##
			print('8 - Trocar nome de usuário/senha')
			print('9 - Apagar conta') 
			print('10 - Ver tutorial') ##
			print('11 - Voltar ao menu principal')
			opcao = int(input('Digite a opção desejada\n'))
			if opcao == 1:
				Exibir(arquivo, 1, 1, 0)
			elif opcao == 2:
				Exibir(arquivo, 1, 0, 0)
			elif opcao == 3:
				Exibir(arquivo, 0, 1, 0)
			elif opcao == 4:
				Editar()
	else:
		print('Usuario e/ou senha incorreto(s), tente novamente')
	return

main()
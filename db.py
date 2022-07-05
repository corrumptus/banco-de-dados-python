import os

#------------------Sessão de menus------------------
def main():
	opcao = 1
	while opcao != 0:
		print('1 - Entrar em sua conta')
		print('2 - Entrar como administrador')
		print('3 - Contatos')
		print('4 - Cadastrar uma conta')
		print('5 - Suporte')
		print('6 - Vert tutorial')
		print('0 - Fechar o programa')
		opcao = int(input('Digite a opção desejada\n'))
		if opcao == 1:
			main_logar()
		elif opcao == 2:
			nome = input('Digite o nome de usuário\n')
			senha = input('Digite a senha\n')
			if nome and senha == 'Admin':
				main_Adm()
			else:
				print('login invalido')
		elif opcao == 3:
			Contatos()
		elif opcao == 4:
			Cadastra_conta()
		elif opcao == 5:
			Suporte()
		elif opcao == 6:
			tutorial(1)
	return

def main_logar():
	nome = input('Digite o seu nome de usuário\n').strip().lower()
	senha = input('Digite a sua senha\n').strip().lower()
	if Checa_senha(nome, senha) == True:
		opcao = 1
		arquivo = nome + ',' + senha + '.txt'
		while opcao != 10:
			print('1 - Ver todo o arquivo')
			print('2 - Ver só os avisos/lembretes')
			print('3 - Ver só o texto')
			print('4 - Editar arquivo')
			print('5 - Entrar na área secreta')
			print('6 - Solicitar suporte')
			print('7 - Trocar nome de usuário/senha')
			print('8 - Apagar conta')
			print('9 - Ver tutorial')
			print('10 - Voltar ao menu principal')
			opcao = int(input('Digite a opção desejada\n'))
			if opcao == 1:
				Exibir(arquivo, 1, 1, 0)
			elif opcao == 2:
				Exibir(arquivo, 1, 0, 0)
			elif opcao == 3:
				Exibir(arquivo, 0, 1, 0)
			elif opcao == 4:
				main_edicao(arquivo)
			elif opcao == 5:
				main_secreta()
			elif opcao == 6:
				mensagem = input('Digite a mensagem\n')
				Escrever(arquivo, mensagem, [1,0,0], [0,0,1])
			elif opcao == 7:
				trocar()
			elif opcao == 8:
				Apagar()
			elif opcao == 9:
				tutorial(2)
	else:
		print('Usuario e/ou senha incorreto(s), tente novamente')
	return

def main_Adm():
	opcao = 1
	while opcao != 7:
		print('1 - Ver quantas pessoas estão cadastradas')
		print('2 - Listar pessoas cadastradas')
		print('3 - Adicionar um aviso para todos os usuários')
		print('4 - Modificar o nome/senha de um usuário')
		print('5 - Remover uma conta')
		print('6 - Ver tutorial')
		print('7 - Voltar ao menu principal')
		opcao = int(input('Digite a opção desejada\n'))
		if opcao == 1:
			Cadastrados(1)
		elif opcao == 2:
			Cadastrados(2)
		elif opcao == 3:
			Avisar_todos()
		elif opcao == 4:
			qual = input('Digite o que será trocado(nome/senha)\n')
			if qual == 'nome':
				qual = input('Digite o nome do usuário\n')
				trocar(qual)
			elif qual == 'senha':
				qual = input('Digite o nome do usuário\n')
				qualsenha = input('Digite a senha do usuário\n')
				trocar_senha(qual, qualsenha)
		elif opcao == 5:
			nome = input('Digite o nome do usuário\n')
			Remove(nome)
		elif opcao == 6:
			tutorial(3)
	return

def Contatos():
	print('https://github.com/corrumptus')
	print('email: surx42@gmail.com')
	print('telefone: (12) 93456-7810')
	return

def main_edicao():

	return

def main_secreta():

	return

def tutorial(k):
	if k == 1:
		print('Bem vindo ao tutorial do menu principal')
		print('Toda vez que você entrar no sistema, verá as opções do menu principal, onde deverá dizer o que deseja fazer.')
		print('Quando descidir o que quer fazer, você será redirecionado para outro lugar, onde fará o que o sistema disponibilizar.')
		print('Caso você tenha perdido a sua senha, não se preocupe, pois você pode solicitar ao suporte que te reenvie a sua senha para o seu contato de segurança.')
		print('Caso tenha se esquecido de como as coisas funcinam é só entrar nessa sessão novamente.')
	elif k == 2:
		print('Bem vindo ao tutorial do menu do usuário')
		print('Toda vez que você se cadastra no nosso sistema você ganha um arquivo só seu, que possui 3 sessões de texto: Avisos/lembretes, Texto e Área secreta.')
		print('Além de você ter a liberdade de escrever o que quiser, nós te garantimos que ninguém pode ler o que está escrito. Segurança total e irrestrita.')
		print('Na primeira sessão(avisos e lembretes), você pode deixar um lembrete ou receber um aviso vindo do suporte.')
		print('Na segunda sessão(texto), você pode escrever qualquer coisa, sendo esse o texto visível que só você pode editar.')
		print('Na terceira sessão(área secreta), você pode escrever qualquer coisa, onde só você pode editar e VER. (mas lembre-se, para acessála você deve entrar nessa sessão).')
		print('Além dessas funcionalidades, você também pode trocar a sua senha e o seu nome de usuário(para um que não esteja sendo usuado).')
		print('Na pior das hipóteses, se você se cansar dos nossos serviços, você tem a opção de excluir permanentemente sua conta.')
		print('Caso tenha se esquecido de como as coisas funcinam é só entrar nessa sessão novamente.')
	elif k == 3:
		print('Bem vindo ao menu de administrador')
		print('Com o cargo de administrador você obtem grande poder sobre o sistema podendo obter informações dele ou informando os nossos usuário.')
		print('Você pode até mesmo mudar o nome de usuário de alguém ou ser o juiz excluindo a conta de alguém.')
		print('Use o seu poder com responsabilidade. não se esqueça que pessoas podem ser inocentes no fim das contas.')
		print('Caso tenha se esquecido de como as coisas funcinam é só entrar nessa sessão novamente.')
	return

#------------------Sessão de processamento------------------
def Cadastra_conta():
	nome = input('Digite o seu nome de usuários\n').lower().strip()
	if Checa_usu(nome) == False:
		senha = input('Digite a sua senha(não se esqueça dela)\n').lower().strip()
		if len(senha) >= 6:
			senha2 = input('Digite a sua senha novamente(não se esqueça dela)\n').lower().strip()
			if senha == senha2:
				arq = open(nome + ',' + senha + '.txt', 'w', encoding ='utf8')
				arq.write('-------Avisos/Lembretes-------\n')
				arq.write('------------Texto-------------\n')
				arq.write('---------Área secreta---------\n')
				arq.close()
				tipo = input('Digite um tipo de contato para segurança(email, telefone...)\n').strip().lower()
				contato = input('Digite um contato de segurança\n').strip()
				if ' || ' not in nome or senha or contato or tipo:
					Adiciona_nome(nome + ',' + senha + '.txt', contato, tipo) #### Log
				else:
					print('Algo possui um elemento " || ", o que não pode, tente novamente')
			else:
				print('Senhas diferentes, tente novamente')
		else:
			print('Senha muito fraca, tente novamente')
	else:
		print('Esse usuário já existe, tente novamente')
	return

def Suporte():
	usuario = input('Digite o seu nome de usuário\n').strip().lower()
	if Checa_usu(usuario) == True:
		contato = input('Digite o seu contato cadastrado\n').strip().lower()
		if Checa_contato(usuario) == contato:
			a_ADM, n, n2 = Carrega_arq('AdminAdmin.txt')
			arq_ADM = open('AdminAdmin.txt', 'w')
			for i in range(n):
				arq_ADM.write(a_ADM[i])
			arq_ADM.write('o usuário ' + usuario + 'perdeu sua senha. Entrar em contato com o mesmo via: ' + contato + '(' + Acha_tipo(usuario) + ')')
			for i in range(n, len(a_ADM)+1):
				arq_ADM.write(a_ADM[i])
			arq_ADM.write('O usuario ' + usuario + ' pediu ajuda ao suporte')
			arq_ADM.close() ##### Log
			return

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

def Escrever(nome, mensagem, listasec1, listasec2):
	arq1, n, n2 = Carrega_arq(nome)
	arq2 = open(nome, 'w', encoding = 'utf8')
	for i in range(0*listasec1[0] + n*listasec1[1] + n2*listasec1[2], n*listasec1[0] + n2*listasec1[1] + len(arq1)*listasec1[2]):
		arq2.write(arq1[i])
	arq2.write(mensagem)
	for i in range(0*listasec2[0] + n*listasec2[1] + n2*listasec2[2], n*listasec2[0] + n2*listasec2[1] + len(arq1)*listasec2[2]):
		arq2.write(arq1[i])
	arq1.close()
	arq2.close()
	return

def Apagar():

	return

def trocar():

	return

def trocar_senha():

	return

def Cadastrados(k):
	arq, n, n2 = Carrega_arq('AdminAdmin.txt')
	if k == 1:
		print('Existem ' + str(n2-n-1) + 'contas cadastradas')
	elif k == 2:
		for i in range(n, n2):
			print(arq[i])
	return

def Avisar_todos():
	arq_ADM, n, n2 = Carrega_arq('AdminAdmin.txt')
	mensagem = input('Digite a mensagem\n')
	for i in range(n+1, n2):
		Escrever(arq_ADM[i], mensagem, [1,0,0], [0,0,1])
	return

def Remove():

	return

def aciona_Log(mensagem):
	log = open('Logs.txt', 'a', encoding ='utf8')
	log.write(mensagem + '\n')
	log.close()
	return
#------------------Sessão de processamento suporte------------------
def Carrega_arq(nome):
	arq = open(nome, 'r')
	arquivo = []
	for i in arq:
		arquivo.append(i.replace('\n',''))
	for i in range(len(arquivo)):
		if nome == 'AdminAdmin.txt':
			if arquivo[i] == '-------Contas-------':
				n = i
			if arquivo[i] == '-------Log-------':
				n2 = i
		else:
			if arquivo[i] == '------------Texto-------------':
				n = i
			if arquivo[i] == '---------Área secreta---------':
				n2 = i
	arq.close()
	return arquivo, n, n2

def Checa_usu(nome):
	arq_ADM, n, n2 = Carrega_arq('AdminAdmin.txt')
	for i in range(n+1, n2):
		n3 = arq_ADM[i].find(',')
		if arq_ADM[i][0:n3] == nome:
			return True
	return False

def Checa_senha(nome, senha):
	arq_ADM, n, n2 = Carrega_arq('AdminAdmin.txt')
	for i in range(n+1, n2):
		n3 = arq_ADM[i].find(',')
		n4 = arq_ADM[i].find('.txt')
		if arq_ADM[i][0:n3] == nome and arq_ADM[i][n3+1:n4] == senha:
			return True
	return False

def Acha_tipo(nome):
	arq_ADM, n, n2 = Carrega_arq('AdminAdmin.txt')
	for i in range(n+1,n2):
		n3 = arq_ADM[i].find(',')
		if arq_ADM[i][0:n3] == nome:
			for j in range(len(arq_ADM[i])-1, 0, -1):
				if arq_ADM[i][j] == ' ':
					return arq_ADM[i][j+1:]

def Checa_contato(nome):
	arq_ADM, n, n2 = Carrega_arq('AdminAdmin.txt')
	for i in range(n+1,n2):
		n3 = arq_ADM[i].find(',')
		if arq_ADM[i][0:n3] == nome:
			n3 = arq_ADM[i].find(' || ')
			for j in range(len(arq_ADM[i])-1, 0, -1):
				if arq_ADM[i][j] == ' ':
					return arq_ADM[i][n3+4:j-3]

def Adiciona_nome(nome, contato, tipo):
	arq_ADM, n, n2 = Carrega_arq('AdminAdmin.txt')
	arq = open('AdminAdmin.txt', 'w', encoding ='utf8')
	for i in range(n):
		arq.write(arq_ADM[i]+'\n')
	for i in range(n, n2):
		arq.write(arq_ADM[i]+'\n')
	arq.write(nome + ' || ' + contato + ' || ' + tipo + '\n')
	for i in range(n2, len(arq_ADM)):
		arq.write(arq_ADM[i]+'\n')
	arq.write('Novo usuário criado: ' + nome + '\n')
	arq.close()
	log = open('Logs.txt', 'a', encoding ='utf8')
	log.write('Novo usuário criado: ' + nome + '\n')
	log.close()
	return

main()
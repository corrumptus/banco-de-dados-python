import os

#------------------Sessão de menus------------------
def main():
	opcao = 1
	while opcao != 0:
		print('1 - Entrar em sua conta')
		print('2 - Entrar como administrador')
		print('3 - Contatos')
		print('4 - Cadastrar uma conta')
		print('5 - Solicitar suporte')
		print('6 - Vert tutorial')
		print('0 - Fechar o programa')
		opcao = int(input('Digite a opção desejada\n'))
		if opcao == 1:
			main_logar()
		if opcao == 2:
			main_Adm()
		if opcao == 3:
			Contatos()
		if opcao == 4:
			Cadastra_conta()
		if opcao == 5:
			contato = input('Digite um meio de contato para a ajuda\n')
			mensagem = input('Faça a sua pergunta ao suporte (apenas coisas relevantes, não se esqueça de acessar ao tutorial)\n')
			Escrever('AdminAdmin.txt', 'Ajuda para ' + contato + ': ' + mensagem, 1)
		if opcao == 6:
			tutorial(1)
	return

def main_logar():
	nome = input('Digite o seu nome de usuário\n').strip().lower()
	senha = input('Digite a sua senha\n').strip()
	if Checa_senha(nome, senha) == True:
		opcao = 1
		arquivo = nome + ',' + senha + '.txt'
		aciona_Log('O usuário ' + nome + ' acessou sua conta.')
		while opcao != 11:
			print('1 - Ver todo o arquivo')
			print('2 - Ver só os avisos/lembretes')
			print('3 - Ver só o texto')
			print('4 - Editar arquivo')
			print('5 - Entrar na área secreta')
			print('6 - Solicitar suporte')
			print('7 - Trocar nome de usuário')
			print('8 - Trocar a senha')
			print('9 - Apagar conta')
			print('10 - Ver tutorial')
			print('11 - Voltar ao menu principal')
			opcao = int(input('Digite a opção desejada\n'))
			if opcao == 1:
				Exibir(arquivo, 1, 1, 0)
			if opcao == 2:
				Exibir(arquivo, 1, 0, 0)
			if opcao == 3:
				Exibir(arquivo, 0, 1, 0)
			if opcao == 4:
				main_edicao(arquivo)
			if opcao == 5:
				main_secreta(arquivo)
			if opcao == 6:
				mensagem = input('Faça a sua pergunta ao suporte (apenas coisas relevantes, não se esqueça de acessar ao tutorial)\n')
				Escrever('AdminAdmin.txt', 'Ajuda para ' + Acha_contato(nome) + ': ' + mensagem, 1)
			if opcao == 7:
				Trocar(nome, 1)
			if opcao == 8:
				Trocar(nome, 2)
			if opcao == 9:
				Excluir(nome)
				print('Muito obrigado pela preferencia, até um outro dia.')
				opcao = 11
			if opcao == 10:
				tutorial(2)
	else:
		print('Usuario e/ou senha incorreto(s), tente novamente')
	return

def main_Adm():
	nome = input('Digite o nome de usuário\n')
	senha = input('Digite a senha\n')
	if nome and senha == 'Admin':
		opcao = 1
		while opcao != 12:
			print('1 - Ver quantas pessoas estão cadastradas')
			print('2 - Listar pessoas cadastradas')
			print('3 - Adicionar um novo lembrete')
			print('4 - Apagar um lembrete/aviso')
			print('5 - Ver os últimos logs(100)')
			print('6 - Ver todos os logs')
			print('7 - Adicionar um aviso para todos os usuários')
			print('8 - Modificar o nome de um usuário')
			print('9 - Modificar a senha de um usuário')
			print('10 - Remover uma conta')
			print('11 - Ver tutorial')
			print('12 - Voltar ao menu principal')
			opcao = int(input('Digite a opção desejada\n'))
			if opcao == 1:
				Exibir_2(1)
			if opcao == 2:
				Exibir('AdminAdmin.txt', 0, 1, 0)
			if opcao == 3:
				lembrete = input('Digite o novo lembrete\n')
				Escrever('AdminAdmin.txt', lembrete, 1)
			if opcao == 4:
				Apagar('AdminAdmin.txt', 1)
			if opcao == 5:
				Exibir('AdminAdmin.txt', 0, 0, 1)
			if opcao == 6:
				Exibir_2(2)
			if opcao == 7:
				Avisar_todos()
			if opcao == 8:
				nome = input('Digite o nome do usuário\n').lower()
				Trocar(nome, 1)
			if opcao == 9:
				nome = input('Digite o nome do usuário\n').lower()
				Trocar(nome, 2)
			if opcao == 10:
				nome = input('Digite o nome do usuário\n')
				Excluir(nome)
			if opcao == 11:
				tutorial(3)
	else:
		print('login invalido')
	return

def Contatos():
	print('https://github.com/corrumptus')
	print('email: py.db.suporte@gmail.com')
	print('telefone: (12) 93456-7810')
	return

def main_edicao(arq):
	opcao = 1
	while opcao != 7:
		print('1 - Escrever um novo lembrete')
		print('2 - Escrever uma nova linha de texto')
		print('3 - Excluir um aviso/lembrete')
		print('4 - Excluir uma linha de texto')
		print('5 - Excluir todos os avisos/lembretes')
		print('6 - Excluir todo o texto')
		print('7 - Voltar ao menu de usuário')
		opcao = int(input('Digite a opção desejada\n'))
		if opcao == 1:
			lembrete = input('Digite o novo lembrete\n')
			Escrever(arq, lembrete, 1)
		if opcao == 2:
			texto = input('Digite a nova linha de texto\n')
			Escrever(arq, texto, 2)
		if opcao == 3:
			Apagar(arq, 1)
		if opcao == 4:
			Apagar(arq, 2)
		if opcao == 5:
			Apagar_tudo(arq, 1)
		if opcao == 6:
			Apagar_tudo(arq, 2)
	return

def main_secreta(arq):
	senha = input('Digite a sua senha secreta\n')
	if Checa_senha_secreta(arq, senha) == True:
		opcao = 1
		while opcao != 6:
			print('1 - Ver a área secreta')
			print('2 - Escrever na área secreta')
			print('3 - Apagar uma linha da área secreta')
			print('4 - Apagar toda a área secreta')
			print('5 - Trocar senha secreta')
			print('6 - voltar ao menu de usuário')
			opcao = int(input('Digite a opção desejada\n'))
			if opcao == 1:
				Exibir(arq, 0, 0, 1)
			if opcao == 2:
				mensagem = input('Digite a nova linha secreta\n')
				Escrever(arq, mensagem, 3)
			if opcao == 3:
				if Checa_secreta(arq) == True: ###########################
					Apagar(arq, 3)
			if opcao == 4:
				Apagar_tudo(arq, 3)
			if opcao == 5:
				Trocar_senha_secreta(arq)
	else:
		print('Senha incorreta, tente novamente')

def tutorial(k):
	if k == 1:
		print('Bem vindo ao tutorial do menu principal')
		print('Toda vez que você entrar no sistema, verá as opções do menu principal, onde deverá dizer o que deseja fazer.')
		print('Quando descidir o que quer fazer, você será redirecionado para outro lugar, onde fará o que o sistema disponibilizar.')
		print('Caso você tenha perdido a sua senha, não se preocupe, pois você pode solicitar ao suporte que te reenvie a sua senha para o seu contato de segurança.')
		print('Caso tenha se esquecido de como as coisas funcinam é só entrar nessa sessão novamente.\n')
	elif k == 2:
		print('Bem vindo ao tutorial do menu do usuário')
		print('Toda vez que você se cadastra no nosso sistema você ganha um arquivo só seu, que possui 3 sessões de texto: Avisos/lembretes, Texto e Área secreta.')
		print('Além de você ter a liberdade de escrever o que quiser, nós te garantimos que ninguém pode ler o que está escrito. Segurança total e irrestrita.')
		print('Na primeira sessão(avisos e lembretes), você pode deixar um lembrete ou receber um aviso vindo do suporte.')
		print('Na segunda sessão(texto), você pode escrever qualquer coisa, sendo esse o texto visível que só você pode editar.')
		print('Na terceira sessão(área secreta), você pode escrever qualquer coisa, onde só você pode editar e VER. (mas lembre-se, para acessála você deve entrar nessa sessão).')
		print('Além dessas funcionalidades, você também pode trocar a sua senha e o seu nome de usuário(para um que não esteja sendo usuado).')
		print('Na pior das hipóteses, se você se cansar dos nossos serviços, você tem a opção de excluir permanentemente sua conta.')
		print('Caso tenha se esquecido de como as coisas funcinam é só entrar nessa sessão novamente.\n')
	elif k == 3:
		print('Bem vindo ao menu de administrador')
		print('Com o cargo de administrador você obtem grande poder sobre o sistema podendo obter informações dele ou informando os nossos usuário.')
		print('Você pode até mesmo mudar o nome de usuário de alguém ou ser o juiz excluindo a conta de alguém.')
		print('Use o seu poder com responsabilidade. não se esqueça que pessoas podem ser inocentes no fim das contas.')
		print('Caso tenha se esquecido de como as coisas funcinam é só entrar nessa sessão novamente.\n')
	return

#------------------Sessão de processamento------------------
def Cadastra_conta():
	nome = input('Digite um nome para o seu usuários\n').lower().strip()
	if Checa_usu(nome) == False and (',' and '.txt' and ' || ' and '---------Área secreta---------' and '------------Texto-------------') not in nome:
		senha = input('Digite uma senha(não se esqueça dela)\n').strip()
		if len(senha) >= 6 and ('.txt' and ' || ' and '---------Área secreta---------' and '------------Texto-------------') not in senha:
			senha2 = input('Digite a sua senha novamente(não se esqueça dela)\n').strip()
			if senha == senha2:
				tipo = input('Digite um tipo de contato para segurança(email, telefone...)\n').strip().lower()
				if ('.txt' and ' || ' and '---------Área secreta---------' and '------------Texto-------------') not in tipo:
					contato = input('Digite um contato de segurança\n').strip()
					if ('.txt' and ' || ' and '---------Área secreta---------' and '------------Texto-------------') not in contato:
						arq = open(nome + ',' + senha + '.txt', 'w', encoding ='utf8')
						arq.write('-------Avisos/Lembretes-------\n')
						arq.write('------------Texto-------------\n')
						arq.write('---------Área secreta---------\n')
						arq.write('Senha: ' + input('Digite uma senha para proteger a sua área secreta\n'))
						arq.close()
						Adiciona_nome(nome + ',' + senha + '.txt', contato, tipo)
						aciona_Log('Novo usuário criado: ' + nome + ',' + senha + '.')
						print('Conta criada com sucesso')
					else:
						print('Possui um elemento " || ", o que não pode, tente novamente')
				else:
					print('Possui um elemento " || ", o que não pode, tente novamente')
			else:
				print('Senhas diferentes possui um elemento " || ", o que não pode, tente novamente')
		else:
			print('Senha muito fraca ou possui um elemento " || ", o que não pode, tente novamente')
	else:
		print('Esse usuário já existe ou possui um elemento " || ", o que não pode, tente novamente')
	return

def Exibir(arquivo, sec1, sec2, sec3):
	arq = open(arquivo, 'r', encoding ='utf8')
	Varquivo = []
	for i in arq:
		Varquivo.append(i.replace('\n',''))
	for i in range(len(Varquivo)):
		if Varquivo[i] == '------------Texto-------------':
			n = i
		if Varquivo[i] == '---------Área secreta---------':
			n2 = i
	for i in range(0*sec1, n*sec1):
		print(Varquivo[i])
	for i in range(n*sec2, n2*sec2):
		print(Varquivo[i])
	for i in range(n2*sec3, len(Varquivo)*sec3):
		print(Varquivo[i])
	return

def Escrever(arquivo, mensagem, k):
	arq1, n, n2 = Carrega_arq(arquivo)
	arq2 = open(arquivo, 'w', encoding = 'utf8')
	if k == 1:
		for i in range(n):
			arq2.write(arq1[i]+'\n')
		arq2.write(mensagem+'\n')
		for i in range(n, len(arq1)):
			arq2.write(arq1[i]+'\n')
	if k == 2:
		for i in range(n2):
			arq2.write(arq1[i]+'\n')
		arq2.write(mensagem+'\n')
		for i in range(n2, len(arq1)):
			arq2.write(arq1[i]+'\n')
	if k == 3:
		for i in range(len(arq1)):
			arq2.write(arq1[i]+'\n')
		arq2.write(mensagem+'\n')
	return

def Apagar(arquivo, k):
	arq, n, n2 = Carrega_arq(arquivo)
	if k == 1:
		print(arq[0])
		for i in range(1, n):
			print(str(i) + '. ' + arq[i])
		linha = int(input('Digite a linha a ser excluida\n'))
	if k == 2:
		print(arq[n])
		for i in range(n+1, n2):
			print(str(i-n) + '. ' + arq[i])
		linha = int(input('Digite a linha a ser excluida\n')) + n
	if k == 3:
		print(arq[n2])
		for i in range(n2+2, len(arq)):
			print(str(i-n2) + '. ' + arq[i])
		linha = int(input('Digite a linha a ser excluida\n')) + n2 + 1
	for i in range(linha, len(arq)-1):
		arq[i] = arq[i+1]
	arq.pop()
	arq1 = open(arquivo, 'w', encoding = 'utf8')
	for i in range(len(arq)):
		arq1.write(arq[i] + '\n')
	arq1.close()
	return

def Apagar_tudo(arquivo, k):
	arq, n, n2 = Carrega_arq(arquivo)
	if k == 1:
		for i in range(1, len(arq)-n+1):
			arq[i] = arq[i+n-1]
		for i in range(n-1):
			arq.pop()
	if k == 2:
		for i in range(n+1, len(arq)-n2+n+1):
			arq[i] = arq[i+n2-n-1]
		for i in range(n+1, n2):
			arq.pop()
	if k == 3:
		for i in range(n2+2, len(arq)):
			arq.pop()

def Trocar(nome, k):
	arq_ADM, n, n2 = Carrega_arq('AdminAdmin.txt')
	if k == 1:
		nome2 = input('Digite o novo nome\n')
		for i in range(n+1,n2):
			n3 = arq_ADM[i].find(',')
			if arq_ADM[i][:n3] == nome:
				n4 = arq_ADM[i].find('.txt')
				arq1 = arq_ADM[i][:n4] + '.txt'
				arq_ADM[i] = nome2 + arq_ADM[i][n3:]
				n4 = arq_ADM[i].find('.txt')
				arq2 = arq_ADM[i][:n4] + '.txt'
				os.rename(arq1, arq2)
				aciona_Log('O usuário ' + nome + ' trocou de nome para ' + nome2 + '.')
	if k == 2:
		senha2 = input('Digite a nova senha\n')
		for i in range(n+1, n2):
			n3 = arq_ADM[i].find(',')
			if arq_ADM[i][:n3] == nome:
				n4 = arq_ADM[i].find('.txt')
				arq1 = arq_ADM[i][:n4] + '.txt'
				senha = arq_ADM[i][n3+1:n4]
				arq_ADM[i] = arq_ADM[i][:n3+1] + senha2 + arq_ADM[i][n4:]
				n4 = arq_ADM[i].find('.txt')
				arq2 = arq_ADM[i][:n4] + '.txt'
				os.rename(arq1, arq2)
				aciona_Log('O usuário ' + nome + ' trocou de senha(' + senha + ') para ' + senha2 + '.')
	arq = open('AdminAdmin.txt', 'w', encoding = 'utf8')
	for i in range(len(arq_ADM)):
		arq.write(arq_ADM[i]+'\n')
	arq.close()
	return

def Trocar_senha_secreta(arquivo):
	senha2 = input('Digite a sua senha secreta\n')
	if Checa_senha_secreta(arquivo, senha2) == True:
		Varq, n, n2 = Carrega_arq(arquivo)
		senha3 = input('Digite sua nova senha\n')
		Varq[n2+1] = 'Senha: ' + senha3
		arq = open(arquivo, 'w', encoding = 'utf8')
		for i in range(len(Varq)):
			arq.write(Varq[i]+'\n')
		arq.close()
	return

def Exibir_2(k):
	if k == 1:
		arq, n, n2 = Carrega_arq('AdminAdmin.txt')
		print('Existem ' + str(n2-n-1) + ' contas cadastradas')
	elif k == 2:
		arq = open('Logs.txt', 'r', encoding = 'utf8')
		for i in arq:
			print(i.replace('\n', ''))
	return

def Avisar_todos():
	arq_ADM, n, n2 = Carrega_arq('AdminAdmin.txt')
	mensagem = input('Digite a mensagem\n')
	for i in range(n+1, n2):
		n3 = arq_ADM[i].find('.txt')
		Escrever(arq_ADM[i][0:n3+4], mensagem, 1)
	return

def Excluir(nome): ################################
	certeza = input('Você tem certeza de que deseja excluir sua conta? Este ato é completamente irreversível(sim/não)\n')
	if certeza.strip().lower() == 'sim':
		arq_ADM, n, n2 = Carrega_arq('AdminAdmin.txt')
		for i in range(n+1, n2):
			n3 = arq_ADM[i].find(',')
			if arq_ADM[i][0:n3] == nome:
				n4 = arq_ADM[i].find('.txt')
				os.remove(arq_ADM[i][0:n4]+'.txt')
				for j in range(i, len(arq_ADM)-1):
					arq_ADM[j] = arq_ADM[j+1]
				arq_ADM.pop()
				aciona_Log('O usuário ' + nome + ' excluiu sua conta.')
				return

#------------------Sessão de processamento suporte------------------
def Carrega_arq(arquivo):
	arq = open(arquivo, 'r', encoding ='utf8')
	Varquivo = []
	for i in arq:
		Varquivo.append(i.replace('\n',''))
	for i in range(len(Varquivo)):
		if arquivo == 'AdminAdmin.txt':
			if Varquivo[i] == '------------Contas------------':
				n = i
			if Varquivo[i] == '-------------Log--------------':
				n2 = i
		else:
			if Varquivo[i] == '------------Texto-------------':
				n = i
			if Varquivo[i] == '---------Área secreta---------':
				n2 = i
	arq.close()
	return Varquivo, n, n2

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

def Checa_senha_secreta(arquivo, senha):
	arq, n, n2 = Carrega_arq(arquivo)
	if arq[n2+1][7:] == senha:
		return True
	return False

def Checa_secreta(arquivo):
	arq, n, n2 = Carrega_arq(arquivo)
	if len(arq) - n2 > 1:
		return True
	return False

def Acha_contato(nome):
	arq_ADM, n, n2 = Carrega_arq('AdminAdmin.txt')
	for i in range(n+1,n2):
		n3 = arq_ADM[i].find(',')
		if arq_ADM[i][0:n3] == nome:
			n3 = arq_ADM[i].find(' || ')
			for j in range(len(arq_ADM[i])-1, 0, -1):
				if arq_ADM[i][j] == ' ':
					return arq_ADM[i][n3+4:j-3]

def Acha_tipo(nome):
	arq_ADM, n, n2 = Carrega_arq('AdminAdmin.txt')
	for i in range(n+1,n2):
		n3 = arq_ADM[i].find(',')
		if arq_ADM[i][0:n3] == nome:
			for j in range(len(arq_ADM[i])-1, 0, -1):
				if arq_ADM[i][j] == ' ':
					return arq_ADM[i][j+1:]

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
	arq.close()
	return

def aciona_Log(mensagem):
	log = open('Logs.txt', 'a', encoding ='utf8')
	log.write(mensagem + '\n')
	log.close()
	Checa_len_log()
	arq_ADM = open('AdminAdmin.txt', 'a', encoding ='utf8')
	arq_ADM.write(mensagem + '\n')
	return

def Checa_len_log():
	arq_ADM, n, n2 = Carrega_arq('AdminAdmin.txt')
	if len(arq_ADM) - n2 - 1 == 100:
		for i in range(n2+1, len(arq_ADM)-1):
			arq_ADM[i] = arq_ADM[i+1]
		arq_ADM.pop()
		arq = open('AdminAdmin.txt', 'w', encoding = 'utf-8')
		for i in range(len(arq_ADM)):
			arq.write(arq_ADM[i] + '\n')
		arq.close()
	return

main()
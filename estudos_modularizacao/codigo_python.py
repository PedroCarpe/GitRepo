#A ideia do algoritmo, é simular o cadastro de um cliente/usuario
num = 4
id1 = []
nome = []
cpf = []
email = []
telefone = []

def criarId():
    global id1
    global num
    id1.append(num)
    num += 1
    
def criarNome():
    global nome
    nome.append(input('Digite seu nome: '))
    
def criarCpf():
    global cpf
    cpf.append(input('Digite seu CPF: '))  
    
def criarEmail():
    global email
    email.append(input('Digite seu email: '))
    
def criarTelefone():
    global telefone
    telefone.append(input('Digite seu telefone: '))
 
def cadastrar():
    criarId()
    criarNome()
    criarCpf()
    criarEmail()
    criarTelefone()
    
def Atualizar():
    posicao = nome.index(input('Digite o nome que procura: '))
    nome[posicao] = input('Digite o novo nome: ')    
    
def Deletar():
    pos = nome.index(input('Digite o nome que deseja apagar: '))
    id1.pop(pos)
    cpf.pop(pos)
    email.pop(pos)
    telefone.pop(pos)
    nome.pop(pos)


#vetor = [id1[0],nome[0],cpf[0],email[0],telefone[0]]


'''resposta=input('\nQuer atualizar seus dados (sim/nao)? ')
if resposta=='sim':
    try:
        print('___Atualização__de__Cadastro___')
        Atualizar()
    except:
        print('Cliente não encontrado!')    

resposta=input('\nDeseja apagar um cadastro (sim/nao)? ')
if resposta=='sim':
    try:
        print('___Apagar__Cadastro___')
        Deletar()
    except:
        print('Cliente não encontrado!')'''
    
for t in range(len(id1)):
    print('\n___Dados__Cadastrados___\n'+'Nome: '+nome[t]+'\n'+'CPF: '+cpf[t][0:3]+'.'+cpf[t][3:6]+'.'+cpf[t][6:9]+'-'+cpf[t][9:]+'\n'+'Email: '+email[t]+'\n'+'Telefone: ('+telefone[t][0:2]+') '+telefone[t][2:])    
  
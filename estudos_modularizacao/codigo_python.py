#A ideia do algoritmo, é simular o cadastro de um cliente/usuario
#APF, validar entradas dos campos

num = 0
id1 = []
nome = []
cpf = []
email = []
telefone = []

def criar_id():
    global id1
    global num
    id1.append(num)
    num += 1
    
def criar_nome():
    global nome
    
    nome_ = input('Digite seu nome: ')
    copia_nome = nome_
    nome_ = nome_.split()
    
    for partes_nome in nome_:
        if partes_nome.isalpha() == True:
            boleana = True
        else:
            boleana = False
            break
    #cadastrar()

    #print(boleana)
    if boleana == True:
        nome.append(copia_nome)
        return True
    else:
        print('nome incorreto!')    
      
    
def criar_cpf():
    global cpf
    cpf.append(input('Digite seu CPF: '))  
    
def criar_email():
    global email
    email.append(input('Digite seu email: '))
    
def criar_telefone():
    global telefone
    telefone.append(input('Digite seu telefone: '))
 
def cadastrar():
    #criar_id()
    if criar_nome() == True:
        criar_cpf()
        criar_email()
        criar_telefone()
        
    
'''def atualizar():
    posicao = nome.index(input('Digite o nome que procura: '))
    nome[posicao] = input('Digite o novo nome: ')
'''    
    
def atualizar():
    antigo_email = input('Digite o antigo email: ')
    novo_email = input('Digite o novo email: ')
    
    return novo_email,antigo_email

def deletar():
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
  
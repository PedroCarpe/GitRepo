#A ideia do algoritmo, é simular o cadastro de um cliente/usuario
#APF, validar entradas dos campos

nome = []
cpf = []
email = []
telefone = []

    
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

    #print(boleana)
    if boleana == True:
        #print('\u2705')
        nome.append(copia_nome)
        return True
    else:
        print('\u001b[31m'+'Nome incorreto, digite novamente!'+'\u001b[37m')
        criar_nome()    
      
    
'''def criar_cpf():
    global cpf
    cpf.append(input('Digite seu CPF: '))'''

def criar_cpf():
    global cpf

    cpf_ = input('Digite seu CPF(somente números/sem espaços): ')

    if cpf_.isnumeric() == True:
        boleana = True
    else:
        boleana = False

    #print(boleana)
    if boleana == True:
        cpf.append(cpf_)
        return True
    else:
        print('\u001b[31m'+'CPF incorreto, digite novamente!'+'\u001b[37m')
        criar_cpf()      
    
'''def criar_email():
    global email
    email.append(input('Digite seu email: '))'''

def criar_email():
    global email

    email_ = input('Digite seu email: ')

    if email_.find('@') != -1:
        boleana = True
    else:
        boleana = False

    #print(boleana)
    if boleana == True:
        email.append(email_)
        return True
    else:
        print('\u001b[31m'+'Email incorreto, digite novamente!'+'\u001b[37m')
        criar_email()    
    
'''def criar_telefone():
    global telefone
    telefone.append(input('Digite seu telefone: '))'''

def criar_telefone():
    global telefone

    telefone_ = input('Digite seu Telefone(somente números/sem espaços): ')

    if telefone_.isnumeric() == True:
        boleana = True
    else:
        boleana = False

    #print(boleana)
    if boleana == True:
        telefone.append(telefone_)
        return True
    else:
        print('\u001b[31m'+'Telefone incorreto, digite novamente!'+'\u001b[37m')
        criar_telefone()    
 
'''def cadastrar():
    if criar_nome() == True:    
        if criar_cpf() == True:
            criar_email()
            criar_telefone()
        else:
            criar_cpf()   
    else:
        criar_nome()'''

def cadastrar():
    criar_nome()
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
    #id1.pop(pos)
    cpf.pop(pos)
    email.pop(pos)
    telefone.pop(pos)
    nome.pop(pos)


#vetor = [id1[0],nome[0],cpf[0],email[0],telefone[0]]

'''resposta=input('\nDeseja apagar um cadastro (sim/nao)? ')
if resposta=='sim':
    try:
        print('___Apagar__Cadastro___')
        Deletar()
    except:
        print('Cliente não encontrado!')'''
    
#for t in range(len(id1)):
#    print('\n___Dados__Cadastrados___\n'+'Nome: '+nome[t]+'\n'+'CPF: '+cpf[t][0:3]+'.'+cpf[t][3:6]+'.'+cpf[t][6:9]+'-'+cpf[t][9:]+'\n'+'Email: '+email[t]+'\n'+'Telefone: ('+telefone[t][0:2]+') '+telefone[t][2:])    
  
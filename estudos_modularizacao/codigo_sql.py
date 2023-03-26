#A ideia do algoritmo, é simular o cadastro de um cliente/usuario
import mysql.connector
from codigo_python import cadastrar,atualizar,cpf,email,telefone


#Conexao com o banco de dados
mybd = mysql.connector.connect(
host = 'localhost',
user = 'root',
password = 'senha',
database = 'usuarios'
)
mycursor = mybd.cursor()

print('___Cadastro__de__Cliente___')
while True:
    nome = cadastrar()

    sql = ('INSERT INTO pessoas (nome,cpf,email,telefone) VALUES(%s,%s,%s,%s)')

    for usuario in range(len(nome)):
        val = (nome[usuario],cpf[usuario],email[usuario],telefone[usuario])
        mycursor.execute(sql,val)
        mybd.commit()

    resposta = input('\nQuer cadastrar outro cliente (sim/nao)? ')
    if resposta == 'nao':
        break



'''resposta_atualizar = input('\nQuer atualizar seus dados (sim/nao)? ')
if resposta_atualizar == 'sim':
    mycursor.execute('SELECT * FROM pessoas')
    myresult = mycursor.fetchall()

    print('')
    print('___Dados__Cadastrados___\n')
    for result in myresult:
        print(result)
    try:
        print('\n___Atualização__de__Cadastro___')
        dados_ = atualizar()
        sql = f"UPDATE pessoas SET {dados_[2]} = '{dados_[0]}' WHERE {dados_[2]} = '{dados_[1]}'"
        mycursor.execute(sql)
        mybd.commit()
        print(mycursor.rowcount," registro(s) afetado(s)!")
        
        mycursor.execute(f"SELECT * FROM pessoas WHERE {dados_[2]} = '{dados_[0]}'")
        myresult = mycursor.fetchall()

        print('')
        print('___Registro(s)__Cadastrado(s)___\n')
        for result in myresult:
            print(result)
    except:
        print('Erro, operação não efetuada!')'''   

#--------------------------------------------------------------------------------
'''sql = ('INSERT INTO pessoas (nome,cpf,email,telefone) VALUES(%s,%s,%s,%s)')

#variavel 'nome' escolhida aleatoriamente, como referencia
for usuario in range(len(nome)):
    val = (nome[usuario],cpf[usuario],email[usuario],telefone[usuario])
    mycursor.execute(sql,val)
    mybd.commit()'''

#---------------------------------------------------------------------------------
'''mycursor.execute('SELECT * FROM pessoas')
myresult = mycursor.fetchall()

print('')
print('___Dados__Cadastrados___\n')
for result in myresult:
    print(result)'''

mycursor.close()
mybd.close()
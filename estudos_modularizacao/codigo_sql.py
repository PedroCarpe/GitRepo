#A ideia do algoritmo, é simular o cadastro de um cliente/usuario
import mysql.connector
from codigo_python import cadastrar,id1,nome,cpf,email,telefone

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
    cadastrar()
    resposta = input('\nQuer cadastrar outro cliente (sim/nao)? ')
    if resposta == 'nao':
        break

    

#--------------------------------------------------------------------------------
sql = ('INSERT INTO pessoas (nome,cpf,email,telefone) VALUES(%s,%s,%s,%s)')

#variavel 'nome' escolhida aleatoriamente, como referencia
for usuario in range(len(nome)):
    val = (nome[usuario],cpf[usuario],email[usuario],telefone[usuario])
    mycursor.execute(sql,val)
    mybd.commit()

#---------------------------------------------------------------------------------
mycursor.execute('SELECT * FROM pessoas')
myresult = mycursor.fetchall()

print('')
for result in myresult:
    print(result)


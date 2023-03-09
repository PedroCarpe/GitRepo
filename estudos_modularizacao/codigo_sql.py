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

print('___Cadastro__de__Cliente___')
while True:
    cadastrar()
    resposta = input('\nQuer cadastrar outro cliente (sim/nao)? ')
    if resposta == 'nao':
        break

print(id1,nome,cpf,email,telefone)
    

mycursor = mybd.cursor()
sql = ('INSERT INTO pessoas (id,nome,cpf,email,telefone) VALUES(%s,%s,%s,%s,%s)')

#variavel 'nome' escolhida aleatoriamente, como referencia
for usuario in range(len(nome)):
    val = (id1[usuario],nome[usuario],cpf[usuario],email[usuario],telefone[usuario])
    mycursor.execute(sql,val)
    mybd.commit()

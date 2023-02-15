#Automação de tarefa escrita txt.
import random
import datetime


#Utilização do ChatGPT para automatizar processo.
# Define the start and end dates
start_date = datetime.date(2023, 1, 1)
end_date = datetime.date(2023, 12, 31)

# Generate a random number of days between the start and end dates
days_between = (end_date - start_date).days
random_days = random.randint(0, days_between)

# Add the random number of days to the start date to get the random date
random_date = start_date + datetime.timedelta(days=random_days)



#Dados pre definido.
titulo = ['empresa', 'produto', 'valor', 'data',]
empresa = ['A','B','C','D']
produto = ['tijolo', 'ferro', 'aluminio', 'telha']
data = random_date



#escrevendo arquivo txt.
linha_titulo = ','.join(titulo)
caminho = '/home/brant/Documents/saga/vendas.txt'
with open(caminho, 'w') as f:
    #escrevendo o titulo.
    f.write(f"{linha_titulo}\n")
    #escrevendo linha.
    for i in range(0,100):
        valor = random.randint(1,1000)

        f.write(f"{random.choice(empresa)},{random.choice(produto)},{valor},{data}\n")


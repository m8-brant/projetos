import pandas as pd

#Atráves de um arquivo txt criar do 0 uma planilha no excel, formato xlsx.


#txt caminho
path_txt = '/home/brant/Documents/saga/vendas.txt'
#data frame
#lendo o arquivo txt em formato csv.
df = pd.read_csv(path_txt, delimiter=',')

#xlsx caminho
path_xlsx = '/home/brant/Documents/saga/vendas.xlsx'
#escrevendo os dados do txt para excel.
df.to_excel(path_xlsx, index=False)

import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACf8a71f915bc55114bcfd8a21b846f7e8"
# Your Auth Token from twilio.com/console
auth_token  = "129dbf610a4190963c61d3c766c1c659"
client = Client(account_sid, auth_token)
# Passo a passo

# Abrir os 6 arquivos do Excel
# Para cada arquivo:

# Verificar se algum valor na coluna vendas daquele arquivo e maior que 55.000

# Se for maior do que 55.000 -> Envia um SMS com o NOME, mes e as vendas dele
# Caso nao seja maior do que 55.000 nao quero faze nada
lista_meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho']

for mes in lista_meses: #pra cada mes da lista_meses me diz qual e o mes
    tabela_vendas = pd.read_excel(f'{mes}.xlsx') #(f) vai formatar e dps vai ser dinamico
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0] #loc e para localizar
        vendas =tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0] # n recebe a tabela, so recebe o valar q vc quer
        print(f' No mes {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5521983013194",
            from_="+16185773659",
            body=f' No mes {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)





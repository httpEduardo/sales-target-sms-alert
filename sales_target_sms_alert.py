import os

import pandas as pd
from twilio.rest import Client

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
sender_number = os.environ.get("TWILIO_FROM_NUMBER")
recipient_number = os.environ.get("TWILIO_TO_NUMBER")

if not all((account_sid, auth_token, sender_number, recipient_number)):
    raise SystemExit(
        "Set TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_NUMBER, "
        "and TWILIO_TO_NUMBER before running this script."
    )

client = Client(account_sid, auth_token)


# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to=recipient_number,
            from_=sender_number,
            body=f'No mês de {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)


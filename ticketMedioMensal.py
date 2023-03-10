from AnaliseDados import clientes_df

ticket_medio = clientes_df['Valor Contrato Mensal'].mean()

print('Ticket_medio mensal: R${:,.2f}'.format(ticket_medio))
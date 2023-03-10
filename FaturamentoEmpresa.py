from AnaliseDados import funcionarios_df, servicos_df, clientes_df

faturamento_df = servicos_df[['ID Cliente', 'Tempo Total de Contrato (Meses)']].merge(clientes_df[['ID Cliente', 'Valor Contrato Mensal']], on='ID Cliente')

#SOMA FATURAMENTO TOTAL

faturamento_df['Faturamento Total'] = faturamento_df['Tempo Total de Contrato (Meses)'] * faturamento_df['Valor Contrato Mensal']

print('O faturamento total da empresa foi de R${:,}'.format(sum(faturamento_df['Faturamento Total'])))
    
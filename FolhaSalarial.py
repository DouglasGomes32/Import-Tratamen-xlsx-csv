from AnaliseDados import funcionarios_df

#Folha salarial

funcionarios_df['Salario Total'] = funcionarios_df['Salario Base'] + funcionarios_df['Impostos'] + funcionarios_df['Beneficios'] + funcionarios_df['VT'] + funcionarios_df['VR']
print('Total da folha salarial mensal é de R${:,}'.format(funcionarios_df['Salario Total'].sum()))
from AnaliseDados import servicos_df, funcionarios_df

contratos_area_df = servicos_df[['ID Funcionário']].merge(funcionarios_df[['ID Funcionário', 'Area']], on=['ID Funcionário'])
#print(contratos_area_df)

contratos_area_qtde = contratos_area_df['Area'].value_counts()
print(contratos_area_qtde)
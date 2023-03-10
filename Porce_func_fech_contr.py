from AnaliseDados import funcionarios_df, servicos_df
import matplotlib.pyplot as plt

qtde_func_fecharamcontrato = len(servicos_df['ID Funcionário'].unique())
qtde_func_total = len(funcionarios_df['ID Funcionário'])
percentual = qtde_func_fecharamcontrato / qtde_func_total

print('A quantidade de funcionários que fecharam contrato, foi de : {:.2%}'.format(percentual))

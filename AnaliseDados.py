import pandas as pd

funcionarios_df = pd.read_csv('CadastroFuncionarios.csv', sep=';', decimal=',')
clientes_df = pd.read_csv('CadastroClientes.csv', sep=';', decimal=',')
servicos_df = pd.read_excel('BaseServiçosPrestados.xlsx', engine='openpyxl')

#retirar colunas de estado civil e cargo da tabela de funcionarios
funcionarios_df = funcionarios_df.drop(['Estado Civil', 'Cargo'], axis=1)


print(funcionarios_df)
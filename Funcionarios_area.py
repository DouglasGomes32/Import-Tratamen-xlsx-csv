from AnaliseDados import funcionarios_df
import matplotlib.pyplot as plt

funcionarios_qtde = funcionarios_df[['ID Funcionário', 'Area']]
funcionarios_qtde_area = funcionarios_qtde['Area'].value_counts()

print(funcionarios_qtde_area)
funcionarios_qtde_area.plot(kind='bar')
plt.show()

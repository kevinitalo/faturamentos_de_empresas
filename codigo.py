# passo a passo do projeto 
# passo 1: pegar cada base de dados ok
# passo 2: para cada base de dados ok
    # calcular o faturamento total(somar todos os valores da coluna de vendas)
# passo 3: crir um ranking com o faturamento total de todas as lojas 
# passo 4: enviar por e-mail esse ranking para a diretoria

import pandas as pd

lista_cidades = ["BH","DF","Manaus", "Rio", "Salvador", "SP"]

faturamentos = {}
for cidade in lista_cidades:
    vendas_df = pd.read_excel(f"Loja {cidade}.xlsx")
    faturamento_cidade = sum(vendas_df["Vendas"])
    faturamentos[cidade] = faturamento_cidade

ranking_df = pd.DataFrame.from_dict(faturamentos, orient="index", columns=["Vendas"])

ranking_df = ranking_df.sort_values(by="Vendas", ascending=False)

mensagem = f"""
Prezados,

Segue em anexo o ranking de vendas das lojas:

{ranking_df.to_string()}

Fico à disposição
At.te
Kevin Italo"""
print(mensagem)


import pandas as pd
import numpy as np

df_cancelamentos = pd.read_csv("cancelamentos_analisado.csv")
df_previsao = pd.read_csv("previsao_cancelamentos.csv")
df_modelo = pd.read_csv("modelo_previsao.csv")
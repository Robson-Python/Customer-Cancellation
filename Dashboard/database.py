import pandas as pd
import numpy as np

df_cancelamentos = pd.read_csv("https://github.com/Robson-Python/Customer-Cancellation/blob/main/Dashboard/cancelamentos_analisado.csv")
df_previsao = pd.read_csv("https://github.com/Robson-Python/Customer-Cancellation/blob/main/Dashboard/previsao_cancelamentos.csv")
df_modelo = pd.read_csv("https://github.com/Robson-Python/Customer-Cancellation/blob/main/Dashboard/modelo_cancelamento.pkl")

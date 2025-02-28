import pandas as pd
import numpy as np

df_cancelamentos = pd.read_csv("/workspaces/Customer-Cancellation/Dashboard/cancelamentos_analisado.csv")
df_previsao = pd.read_csv("/workspaces/Customer-Cancellation/Dashboard/previsao_cancelamentos.csv")
df_modelo = pd.read_csv("/workspaces/Customer-Cancellation/Dashboard/modelo_previsao.csv")
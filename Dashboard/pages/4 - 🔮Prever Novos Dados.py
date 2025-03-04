import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
import joblib
import requests

# Configuração da página
st.set_page_config(
    page_title="Dashboard de Cancelamentos de Clientes - Previsão",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
st.sidebar.title("Desenvolvido por:")
st.sidebar.page_link("https://www.datascienceportfol.io/robsonprogramadordel", label="Robson Silva - Programador Python", icon="🐍")

# Titulo do Dashboard
st.header("📊 Dashboard Cancelamentos de Clientes")
st.title("🔮Prever Novos Cancelamentos")
st.write("Use o Modelo de IA para prever novos Cancelamentos!")

# Carregar modelo de IA treinado
# Faz o download do arquivo
url = "https://raw.githubusercontent.com/Robson-Python/Customer-Cancellation/main/Dashboard/modelo_cancelamento.pkl"
response = requests.get(url)
with open("modelo_cancelamento.pkl", 'wb') as f:
    f.write(response.content)

# Carrega o modelo do arquivo baixado
modelo_previsao = joblib.load("modelo_cancelamento.pkl")

# Carregar base de dados para previsão
novos_dados = st.file_uploader("Escolha um arquivo", type=["CSV", "xlsx"])

if novos_dados is not None:
   if novos_dados.name.endswith('.csv'):
      df_previsao = pd.read_csv(novos_dados)
   else:
      df_previsao = pd.read_excel(novos_dados)
      
   st.write("Dados carregados:")
   # Codificar coluna sexo
   codificador_sexo = LabelEncoder()
   df_previsao["sexo"] = codificador_sexo.fit_transform(df_previsao["sexo"])

   # Codificar coluna assinatura
   codificado_assinatura = LabelEncoder()
   df_previsao["assinatura"] = codificado_assinatura.fit_transform(df_previsao["assinatura"])

   # Codificar coluna duracao_contrato
   codificar_duracao = LabelEncoder()
   df_previsao["duracao_contrato"] = codificar_duracao.fit_transform(df_previsao["duracao_contrato"])
   
   # Visualizar o dataframe
   st.dataframe(df_previsao)
    
# Executar a previsão
if st.button("Fazer Previsão"):
   # Fazer a previsão através do modelo de IA treinado
   nova_previsao = modelo_previsao.predict(df_previsao)

   # Adicionar o campo cacelou com a nova previsão
   df_previsao["cancelou"] = nova_previsao

   # Reverter a codificação de volta para os rótulos originais
   df_previsao["sexo"] = codificador_sexo.inverse_transform(df_previsao["sexo"])
   df_previsao["assinatura"] = codificado_assinatura.inverse_transform(df_previsao["assinatura"])
   df_previsao["duracao_contrato"] = codificar_duracao.inverse_transform(df_previsao["duracao_contrato"])

   # Substituir os valores da coluna sexo
   df_previsao["sexo"] = df_previsao["sexo"].replace({
   "Male": "Masculino",
   "Female": "Feminino"
    })

   # Substituir os valores da coluna assinatura
   df_previsao["assinatura"] = df_previsao["assinatura"].replace({
   "Basic": "Básico",
   "Premium": "Prêmio",
   "Standard": "Padrão"
   })

   # Substituir os valores da coluna duração do contrato
   df_previsao["duracao_contrato"] = df_previsao["duracao_contrato"].replace({
   "Annual": "Anual",
   "Monthly": "Mensal",
   "Quarterly": "Trimestral"
   })

   # Visualizar o dataframe com a coluna cancelou
   st.dataframe(df_previsao)
   
   # Dataframe para plotagem da nova previsão
   df_nova_previsao = df_previsao

   # Contagem de valores
   cancelou_counts = df_nova_previsao["cancelou"].value_counts()
   # Formatação com separador de milhares
   formatted_counts = cancelou_counts.apply(lambda x: "{:,}".format(x).replace(",", "."))

   # Normalização dos valores e formatação em porcentagem
   cancelou_normalized = df_nova_previsao["cancelou"].value_counts(normalize=True).map("{:.1%}".format)

   # Criação das colunas
   col1, col2, col3 = st.columns(3)
   col1.markdown("")
   col1.markdown("")
   col1.markdown("### **Cancelou**: ")

   # Exibindo a métrica
   col2.metric(label="SIM", value=formatted_counts[1], delta=cancelou_normalized[1], delta_color="off", border=True)
   col3.metric(label="NÃO", value=formatted_counts[0], delta=cancelou_normalized[0], border=True)

   # Plotando os gráficos

   st.write("")
   st.write("")
   st.write("### **Visualização dos resultados baseado no Modelo de Previsão:**")
   st.write("")

   # Criar colunas e plotar gráficos
   def plot_histograms(df_nova_previsao):
       colunas = [col for col in df_nova_previsao.columns if col != 'cancelou']
       col_pairs = [(colunas[i], colunas[i + 1]) if i + 1 < len(colunas) else (colunas[i], None) for i in range(0, len(colunas), 2)]

       for col1, col2 in col_pairs:
           cols = st.columns(2)
           for i, col in enumerate([col1, col2]):
               if col:
                    with cols[i]:
                       sns.set_theme(style='whitegrid')
                       fig, ax = plt.subplots(figsize=(6, 3))
                       sns.histplot(data=df_nova_previsao, x=col, hue="cancelou", kde=True, multiple="stack")
                       ax.set_title('Cancelamentos por ' + col)
                       st.pyplot(fig)
   # Plotar histogramas                 
   plot_histograms(df_nova_previsao)

   # Texto
   parabens_text = """
   Parabéns! Sua previsão foi concluída com sucesso.

   --- """
   # Exibir o texto
   st.markdown(parabens_text)

   # Exibir balões
   st.balloons()
   
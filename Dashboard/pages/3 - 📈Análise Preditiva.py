import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from database import df_modelo

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
st.title("📈Análise Preditiva")
st.write("Modelo de Previsão dos Cancelamentos!")

# Contagem de valores
cancelou_counts = df_modelo["cancelou"].value_counts()
# Formatação com separador de milhares
formatted_counts = cancelou_counts.apply(lambda x: "{:,}".format(x).replace(",", "."))

# Normalização dos valores e formatação em porcentagem
cancelou_normalized = df_modelo["cancelou"].value_counts(normalize=True).map("{:.1%}".format)

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
def plot_histograms(df_modelo):
    colunas = [col for col in df_modelo.columns if col != 'cancelou']
    col_pairs = [(colunas[i], colunas[i + 1]) if i + 1 < len(colunas) else (colunas[i], None) for i in range(0, len(colunas), 2)]

    for col1, col2 in col_pairs:
        cols = st.columns(2)
        for i, col in enumerate([col1, col2]):
            if col:
                with cols[i]:
                    sns.set_theme(style='whitegrid')
                    fig, ax = plt.subplots(figsize=(6, 3))
                    sns.histplot(data=df_modelo, x=col, hue="cancelou", kde=True, multiple="stack")
                    ax.set_title('Cancelamentos por ' + col)
                    st.pyplot(fig)
                    
plot_histograms(df_modelo)

# Texto do modelo
modelo_text = """
Como os gráficos demonstram, é possível observar que na previsão dos novos clientes, as chances de cancelamento são muito menores agora.

---
Concluída uma análise aprofundada nos dados e com insights valiosos extraídos, aproveitamos esses insights 
e aplicamos em um modelo de Inteligência Artificial IA, que é capaz ler essas novas informações e dizer 
automaticamente a previsão de cancelamentos para a empresa como mostrado nos gráficos acima.

--- """

# Exibindo texto do modelo
st.markdown(modelo_text)
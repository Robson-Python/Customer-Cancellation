import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from database import df_previsao

# Configuração da página
st.set_page_config(
    page_title="Dashboard de Cancelamentos de Clientes - Prescrição",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
st.sidebar.title("Desenvolvido por:")
st.sidebar.page_link("https://www.datascienceportfol.io/robsonprogramadordel", label="Robson Silva - Programador Python", icon="🐍")

# Titulo do Dashboard
st.header("📊 Dashboard Cancelamentos de Clientes")
st.title("📉Análise Prescritiva")
st.write("Visão das orientações para tomada de decisão!")

# Contagem de valores
cancelou_counts = df_previsao["cancelou"].value_counts()
# Formatação com separador de milhares
formatted_counts = cancelou_counts.apply(lambda x: "{:,}".format(x).replace(",", "."))

# Normalização dos valores e formatação em porcentagem
cancelou_normalized = df_previsao["cancelou"].value_counts(normalize=True).map("{:.1%}".format)

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
st.write("### **Visualização dos resultados baseado na Análise Prescritiva:**")
st.write("")

# Criar colunas e plotar gráficos
def plot_histograms(df_previsao):
    colunas = [col for col in df_previsao.columns if col != 'cancelou']
    col_pairs = [(colunas[i], colunas[i + 1]) if i + 1 < len(colunas) else (colunas[i], None) for i in range(0, len(colunas), 2)]

    for col1, col2 in col_pairs:
        cols = st.columns(2)
        for i, col in enumerate([col1, col2]):
            if col:
                with cols[i]:
                    sns.set_theme(style='whitegrid')
                    fig, ax = plt.subplots(figsize=(6, 3))
                    sns.histplot(data=df_previsao, x=col, hue="cancelou", kde=True, multiple="stack")
                    ax.set_title('Cancelamentos por ' + col)
                    st.pyplot(fig)
                    
plot_histograms(df_previsao)


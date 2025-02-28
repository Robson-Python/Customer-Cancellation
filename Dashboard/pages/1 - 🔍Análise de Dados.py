import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from database import df_cancelamentos

# Configuração da página
st.set_page_config(
    page_title="Dashboard de Cancelamentos de Clientes - Análises",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
st.sidebar.title("Desenvolvido por:")
st.sidebar.page_link("https://www.datascienceportfol.io/robsonprogramadordel", label="Robson Silva - Programador Python", icon="🐍")

# Título do Dashboard
st.header("📊 Dashboard Cancelamentos de Clientes")
st.title("🔍Resultado da Análise de Dados")
st.write("Insights extraídos!")

# Contagem de valores
cancelou_counts = df_cancelamentos["cancelou"].value_counts()
# Formatação com separador de milhares
formatted_counts = cancelou_counts.apply(lambda x: "{:,}".format(x).replace(",", "."))

# Normalização dos valores e formatação em porcentagem
cancelou_normalized = df_cancelamentos["cancelou"].value_counts(normalize=True).map("{:.1%}".format)

# Criação das colunas
col1, col2, col3 = st.columns(3)
col1.markdown("")
col1.markdown("")
col1.markdown("### **Cancelou:** ")

# Exibindo a métrica
col2.metric(label="SIM", value=formatted_counts[0], delta=cancelou_normalized[0], delta_color="inverse", border=True)
col3.metric(label="NÃO", value=formatted_counts[1], delta=cancelou_normalized[1], delta_color="off", border=True)

# Plotando os gráficos

st.write("")
st.write("")
st.write("### **Visualização das principais causas de Cancelamentos:**")
st.write("")

# Primeira linha com duas colunas
col1, col2 = st.columns(2)
# Segunda linha com duas colunas
col3, col4 = st.columns(2)
# Terceira linha com duas colunas
col5, col6 = st.columns(2)

# Primeiro gráfico
fig1, ax1 = plt.subplots(figsize=(6, 3))
sns.histplot(data=df_cancelamentos, x="idade", hue="cancelou", kde=True, multiple="stack", ax=ax1)
ax1.set_title("Cancelamentos por Idade")
col1.pyplot(fig1)

# Segundo gráfico
fig2, ax2 = plt.subplots(figsize=(6, 3))
sns.histplot(data=df_cancelamentos, x="sexo", hue="cancelou", kde=True, multiple="stack", ax=ax2)
ax2.set_title("Cancelamentos por Sexo")
col2.pyplot(fig2)

# Terceiro gráfico
fig3, ax3 = plt.subplots(figsize=(6, 3))
sns.histplot(data=df_cancelamentos, x="frequencia_uso", hue="cancelou", kde=True, multiple="stack", ax=ax3)
ax3.set_title("Cancelamentos por Frequência de Uso")
col3.pyplot(fig3)

# Quarto gráfico
fig4, ax4 = plt.subplots(figsize=(6, 3))
sns.histplot(data=df_cancelamentos, x="duracao_contrato", hue="cancelou", kde=True, multiple="stack", ax=ax4)
ax4.set_title("Cancelamentos por Duração do Contrato")
col4.pyplot(fig4)

# Quinto gráfico
fig5, ax5 = plt.subplots(figsize=(6, 3))
sns.histplot(data=df_cancelamentos, x="ligacoes_callcenter", hue="cancelou", kde=True, multiple="stack", ax=ax5)
ax5.set_title("Cancelamentos por Ligações Call Center")
col5.pyplot(fig5)

# Sexto gráfico
fig6, ax6 = plt.subplots(figsize=(6, 3))
sns.histplot(data=df_cancelamentos, x="dias_atraso", hue="cancelou", kde=True, multiple="stack", ax=ax6)
ax6.set_title("Cancelamentos por Dias de Atraso")
col6.pyplot(fig6)

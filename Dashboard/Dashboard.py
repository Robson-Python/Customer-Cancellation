import streamlit as st
from database import df_cancelamentos

# Configuração da página
st.set_page_config(
    page_title="Dashboard de Cancelamentos de Clientes",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
    )

# Sidebar
st.sidebar.title("Desenvolvido por:")
st.sidebar.page_link("https://www.datascienceportfol.io/robsonprogramadordel", label="Robson Silva - Programador Python", icon="🐍")

# Título do Dashboard
st.header("📊 Dashboard Cancelamentos de Clientes")
st.write("Bem-vindo ao Dashboard de Cancelamentos!")
st.title("Projeto - Cancelamentos de Clientes")
st.markdown("### **Desafio**: ")
st.markdown("Uma empresa com mais de 800 mil clientes, recentemente percebeu que na sua base total de clientes, a maioria são clientes inativos, ou seja, que já cancelaram o serviço.")
st.markdown("Precisando melhorar seus resultados ela quer conseguir entender os principais motivos desses cancelamentos e quais as ações mais eficientes para reduzir esse número.")

# Mostrar o DataFrame
st.subheader('Dados Originais (Primeiras 20 linhas)')
st.dataframe(df_cancelamentos.head(20))

# Usando shape para conferir as dimensões do dataframe
df_tamanho = df_cancelamentos.shape
st.write(f"Quantidade total de registros na base de dados: {df_tamanho}")
st.write("---")
st.write("A base de dados possuia 881666 e 12 colunas, com o tratamento dos dados conseguimos reduzir para 440832 linhas e 12")
st.write("Na base original havia muitos registros ausentes e duplicdos")
st.write("---")

# EDA Básica
st.subheader("Estatísticas Descritivas")
st.dataframe(df_cancelamentos.describe())


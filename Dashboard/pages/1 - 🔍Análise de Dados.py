import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from database import df_cancelamentos

# Função para codificar o valor da coluna Cancelou (0 para Não e 1 para Sim) quando necessário para cálculos matemáticos
def codificar_cancelamento():
    if df_cancelamentos["cancelou"].dtypes == object:
       df_cancelamentos["cancelou"] = df_cancelamentos["cancelou"].replace({
           "Não": 0,
           "Sim": 1
        })
    else: 
       df_cancelamentos["cancelou"] = df_cancelamentos["cancelou"].replace({
          0: "Não",
          1: "Sim"
        })

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

# Contagem das assinaturas do contrato
assinatura_count = df_cancelamentos["assinatura"].value_counts()

# Contagem da duração dos contratos
duracao_count = df_cancelamentos["duracao_contrato"].value_counts()

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
# Quarta linha com duas colunas
col7, col8 = st.columns(2)

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

# Sétimo gráfico
fig7, ax7 = plt.subplots(figsize=(6, 3))
ax7.pie(duracao_count, labels=duracao_count.index, autopct='%1.1f%%', startangle=140)
ax7.set_title("Duração dos Contratos")
ax7.axis("equal")
col7.pyplot(fig7)

# Oitavo gráfico
fig8, ax8 = plt.subplots(figsize=(6, 3))
ax8.pie(assinatura_count, labels=assinatura_count.index, autopct='%1.1f%%', startangle=140)
ax8.set_title("Assinaturas")
ax8.axis("equal")
col8.pyplot(fig8)

# Renomear os valores da coluna cancelou para valor numérico
codificar_cancelamento()

# Média das durações do Contrato por agrupamento
st.dataframe(df_cancelamentos.groupby("duracao_contrato").mean(numeric_only=True))

# Texto da média duraçao do contrato
duracao_text = """
Com as informações agrupadas, é possível notar que os clientes do plano Mensal, possuem uma 
média de cancelamento igual a 1, ou seja, como visto na análise anterior, que supostamente preveu que 
praticamente todos os clientes que utilizam esse plano, fizeram o cancelamento do serviço.

--- """

# Exibir texto duração do contrato
st.markdown(duracao_text)

# Média das Assinaturas do Contrato por agrupamento
st.dataframe(df_cancelamentos.groupby("assinatura").mean(numeric_only=True))

# Texto média assinaturas
assinatura_text = """
Na análise percentual, podemos verificar que temos praticamente a mesma quantidade em cada uma das 
assinaturas, ou seja, temos praticamente 1/3 em cada assinatura, e na análise da média os valores de 
cancelamento também são muito parecidos.

--- """

# Exibir texto média assinaturas
st.markdown(assinatura_text)

# Renomear os valores da coluna cancelou para valor texto
codificar_cancelamento()

# # Fazer a previsão dos cancelamentos sem o Contrato Mensal
previsao_contrato = df_cancelamentos[df_cancelamentos["duracao_contrato"] != "Mensal"]

# Contagem de valores
cancelou_counts_previsao = previsao_contrato["cancelou"].value_counts()

# Formatação com separador de milhares
formatted_counts_previsao = cancelou_counts_previsao.apply(lambda x: "{:,}".format(x).replace(",", "."))

# Normalização dos valores e formatação em porcentagem
cancelou_normalized_previsao = previsao_contrato["cancelou"].value_counts(normalize=True).map("{:.1%}".format)

# Criação das colunas
col4, col5, col6 = st.columns(3)
col4.markdown("")
col4.markdown("")
col4.markdown("### **Cancelou:** ")

# Exibindo a métrica
col5.metric(label="SIM", value=formatted_counts_previsao[1], delta=cancelou_normalized_previsao[1], delta_color="off", border=True)
col6.metric(label="NÃO", value=formatted_counts_previsao[0], delta=cancelou_normalized_previsao[0], border=True)

# Resumo do análise
previsao_text = """
A previsão sem o contrato mensal nos mostra que a proporção de cancelamentos caiu em 46.1%, mas esse número ainda é considerado alto. 

--- """

# Exibir resumo da análise
st.markdown(previsao_text)

# Criar texto da análise
analise_text = """
De acordo com a análise exploratória preliminar, a empresa começou com 56.7% de cancelamentos. 
Com mais algumas análises exploratórias conseguimos reduzir para 53.9%.

Baseado nas sugestões que os gráficos mostraram, o principais vilões dos cancelamentos são:

1 - Atendimento Call Center, onde se encontra o maior motivo para cancelamentos. Esse é um setor que envolve recursos humanos, que pode ser resolvido com reuniões, treinamentos e técnicas voltadas para este serviço. Provavelmente resolvendo esse problema, os cancelamentos envolvidos com o sexo feminino e com a idade acima de 50 anos, podem também ser resolvidos aqui, uma vez que mulheres e pessoas mais velhas também utilizam o call center.

2 - Duração do Contrato, onde todos cancelaram no plano mensal. Aqui o problema pode ser resolvido com melhores preços nos outros dois contratos, mesmo que pague um pouquinho mais caro, para o cliente é melhor se organizar e pagar um contrato de maior tempo e à vista.

3 - E por último o Atraso nos Pagamentos com mais de 20 dias. Aqui o problema pode estar relacionado com questões de juros e moras que acabam inviabilizando o pagamento por parte do cliente, forçando o mesmo a cancelar. Políticas para antecipação de pagamento, descontos para pagamentos antecipados, entre outras medidas, podem contribuir para menos cancelamentos do cliente.

 --- """

# Exibir o texto
st.markdown(analise_text)

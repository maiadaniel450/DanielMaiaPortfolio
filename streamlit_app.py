import streamlit as st
import pandas as pd

# Definir a paleta de cores (preto e vermelho)
st.set_page_config(page_title="Meu Portfólio", page_icon=":guardsman:", layout="wide")

# Definir o tema
st.markdown("""
    <style>
    .main {
        background-color: #000000;
    }
    .block-container {
        background-color: #000000;
        color: #ffffff;
    }
    .stButton>button {
        background-color: #e60000;  /* Vermelho */
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho
st.title("Bem-vindo ao Meu Portfólio!")

st.write("""
    Aqui você pode visualizar alguns dos meus trabalhos e projetos, incluindo relatórios em Power BI, 
    planilhas do Excel e códigos que desenvolvi. Fique à vontade para explorar!
""")

# Seção para relatórios em Power BI
st.header("Relatórios Power BI")
st.write("""
    Infelizmente, não posso incorporar os relatórios diretamente no Streamlit, mas você pode visualizar 
    os relatórios publicados no Power BI clicando no link abaixo:
""")
st.markdown("[Acesse meu relatório Power BI aqui](https://app.powerbi.com/)", unsafe_allow_html=True)

# Seção para arquivos Excel
st.header("Relatórios Excel")
st.write("""
    Abaixo estão alguns arquivos Excel que preparei e que estão disponíveis para visualização.
    Você pode fazer o download e explorar os dados.
""")

# Carregar e exibir um arquivo Excel como exemplo
excel_file = "exemplo_relatorio.xlsx"  # Caminho para o seu arquivo Excel
df = pd.read_excel(excel_file)
st.write(df)

# Seção para códigos
st.header("Meus Códigos")
st.write("""
    Aqui você pode visualizar alguns dos meus códigos em Python e outros projetos de programação.
""")

# Exemplo de exibição de código
st.code("""
# Exemplo de código Python
import numpy as np
import pandas as pd

# Gerar uma série de números aleatórios
data = np.random.randn(100, 2)
df = pd.DataFrame(data, columns=['A', 'B'])
df.head()
""", language="python")

# Botão de contato
st.markdown("""
    Para mais informações ou entrar em contato, me envie um e-mail para: 
    [meuemail@example.com](mailto:meuemail@example.com)
""")

# Rodapé
st.write("Feito com ❤️ usando Streamlit")


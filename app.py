import streamlit as st


#configuração de página
st.set_page_config(
    page_title= "Projeto de estilização do streamlit",
    page_icon='',
    layout="wide"
)

#Título e subtítulo
st.title(" Projeto de Estilização Streamlit")
st.subheader("Exemplo de como organizar e estilizar um app")

#Barra Lateral
st.sidebar.header("Filtros")
st.sidebar.checkbox("Ativar tema escuro", key="Tema")
st.sidebar.slider("Selecionar valor", 0, 100, 25)

#Métricas
st.metric("Vendas", "R$50.000", "+5%")
st.metric("Usuários", "1.200", "-2%")

#Colunas
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Coluna 1")
    st.warning("Tudo certo!")
    st.button("Clique aqui")
    
with col2:
    st.header("Coluna 2")
    st.warning("Atenção!")
    st.radio("Escolha uma opção", ["Opção1", "Opção2", "Opção3"])
    
with col3:
    st.header("Coluna 3")
    st.info("Informação útil")
    st.selectbox("Escolha um item", ["Item 1", "Item 2", "Item 3"])
    
#Expander
with st.expander("Clique para ver mais detalhes"):
    st.write("Aqui dentro você pode colocar informações adicionais, gráficos ou tabelas.")
    st.checkbox("Ativar detalhe extra")
    st.text_input("Digite algo interessante")
    
# Cores e Markdown
st.markdown(
    """
    <div style='background-color: #f9f9f9; padding: 10px; border-radius: 10px'>
    <h4 style= 'color: #FF5733; '>Texto colorido com estilo personalizado</h4>
    </div>
    """,
    unsafe_allow_html=True
)

#Rodapé
st.markdown("---")
st.markdown(" Exemplo simples de estilização no streamlit sem lógica complexa")

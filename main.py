import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=400)

with col2:
    st.title("Matheus Santos")
    texto = """

    Olá! Eu sou um programador Python, estudante de inglês e ciencia da computação. Estudo programação desde 
    2018 e possuo experiencia profissional solida com rotinas administrativas com Excel e VBA onde atuo a 3 anos.

    """
    st.write(texto)

    st.write("Confira meus projetos e me contate se achar qualquer um deles interessante.")
    st.write("GitHub: https://github.com/Fkmatheus")
    st.write("Linkedin: https://www.linkedin.com/in/matheus-santos-aa31a823a/")

   
import streamlit as st
from PIL import Image
from streamlit_modal import Modal

st.set_page_config(page_title="creIA", page_icon="favicon.png",  layout="wide")

# Centraliza o menu usando columns
cols = st.columns([1, 3, 1])
with cols[1]:
    selected_option = st.radio("", ["Overview", "Mapeamento de Obras", "Detecção de Falhas em Obras", "About"], horizontal=True)

# Main content based on selection
if selected_option == "Overview":
    st.title("🧠 CreIA: Inteligência que constrói, visão que previne")

    texto = """
    CreIA é um sistema de inteligência artificial que utiliza redes neurais convolucionais para identificar imagens de obras e diagnosticar problemas estruturais. Com visão computacional, auxilia na detecção precoce de falhas em construções.
    Uma ferramenta inovadora para inspeções mais seguras e eficientes na engenharia civil.
    """

    st.markdown(
        f"""
        <div style='text-align: justify; font-size: 16px;'>
            {texto}
        """,
        unsafe_allow_html=True
    )

elif selected_option == "Mapeamento de Obras":
    st.subheader("Sistema inteligente para monitoramento urbano por meio da análise de imagens aéreas e identificação de obras em andamento. 🛰️")

    uploaded_file = st.file_uploader("📤 Carregar um arquivo:")

    if uploaded_file is not None:
        st.write("✅ Arquivo enviado com sucesso!")
        name = uploaded_file.name
        image = Image.open(uploaded_file)
        st.image(image, use_container_width=True)

        modal = Modal(
                "Resposta do Modelo:",
                key="demo-modal",

                # Optional
                padding=20,    # default value
                max_width=744  # default value
        )

        if name == 'foto1.jpg':
            open_modal = st.button("🤖 Gerar análise com IA")
            if open_modal:
                modal.open()

            if modal.is_open():
                with modal.container():
                    st.write("🏗️ Canteiro de obras")
                    st.image("hammer GIF.gif")


        if name == 'foto2.jpg':
            open_modal = st.button("🤖 Gerar análise com IA")
            if open_modal:
                modal.open()

            if modal.is_open():
                with modal.container():
                    st.write("🏗️ Canteiro de obras")
                    st.image("hammer GIF.gif")

        if name == 'foto3.png':
            open_modal = st.button("🤖 Gerar análise com IA")
            if open_modal:
                modal.open()

            if modal.is_open():
                with modal.container():
                    st.write("🏡 Zona residencial")
                    st.image("house.gif")

elif selected_option == "Detecção de Falhas em Obras":
    st.subheader("Sistema inteligente para monitoramento urbano por meio da análise de imagens aéreas e identificação de obras em andamento. 🛰️")

    uploaded_file = st.file_uploader("📤 Carregar um arquivo:")

    if uploaded_file is not None:
        st.write("✅ Arquivo enviado com sucesso!")
        name = uploaded_file.name
        image = Image.open(uploaded_file)
        st.image(image, use_container_width=True)

elif selected_option == "About":
    st.title("About")
    st.write("This app was built with Streamlit.")

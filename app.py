import streamlit as st
from PIL import Image
from streamlit_modal import Modal

st.set_page_config(page_title="creIA", page_icon="logo.png",  layout="wide")

# Centraliza o menu usando columns
cols = st.columns([1, 3, 1])
with cols[1]:
    selected_option = st.radio("", ["Overview", "Mapeamento de Obras", "Relatório automático",  "Rotas de Fiscalização", "About"], horizontal=True)

st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://images.unsplash.com/photo-1614850523011-8f49ffc73908?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if selected_option == "Overview":

    #st.title("🧠 CreIA: Inteligência que constrói, visão que previne")
    st.markdown('<h1 style="color: white;">🧠 CreIA: Inteligência que constrói, visão que previne</h1>', unsafe_allow_html=True)

    # texto = """
    # CreIA é um sistema de inteligência artificial que utiliza redes neurais convolucionais para identificar imagens de obras e obter seus endereços. Com visão computacional, auxilia na geração de rotas de fiscalização e criação de relatórios.
    # Uma ferramenta inovadora para inspeções eficientes por parte do CREA-PB.
    # """

    # st.markdown(
    #     f"""
    #     <div style='text-align: justify; font-size: 16px;'>
    #         {texto}
    #     """,
    #     unsafe_allow_html=True
    # )

    texto = """
    CreIA é um sistema de inteligência artificial que utiliza redes neurais convolucionais para identificar imagens de obras e obter seus endereços. Com visão computacional, auxilia na geração de rotas de fiscalização e criação de relatórios.
    Uma ferramenta inovadora para inspeções eficientes por parte do CREA-PB.
    """

    st.markdown(
        f"""
        <div style='text-align: justify; font-size: 16px; color: white;'>
            {texto}

        """,
        unsafe_allow_html=True
    )

    logo = Image.open("logo.png")
    crea_logo = Image.open("crea-logo.png")
    hack_logo = Image.open("hack-logo.png")

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

    with col1:
        st.write("")

    with col2:
        st.write("")

    with col3:
        st.image(logo, width=150)

    with col4:
        st.image(hack_logo, width=150)

    with col5:
        st.image(crea_logo, width=150)

    with col6:
        st.write("")

    with col7:
        st.write("")

elif selected_option == "Mapeamento de Obras":
    st.subheader("Sistema inteligente para monitoramento urbano por meio da análise de imagens aéreas e identificação de obras em andamento 🛰️")
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
                    st.image("obra.png", width=100)
                    st.write("🌍 **Coordenadas geográficas do local:** -7.225226441265343, -35.89788344237098")
                    st.write("📍 **Endereço do local:** R. Prof. Capiba, 462 - Centenário, Campina Grande - PB, 58428-023")

        if name == 'foto2.jpg':
            open_modal = st.button("🤖 Gerar análise com IA")
            if open_modal:
                modal.open()

            if modal.is_open():
                with modal.container():
                    st.write("🏗️ Canteiro de obras")
                    st.image("obra.png", width=100)
                    st.write("🌍 **Coordenadas geográficas do local:** -7.118408784900688, -34.87516541708327")
                    st.write("📍 **Endereço do local:** Av. Dom Pedro I, 809 - Centro, João Pessoa - PB, 58013-021")

        if name == 'foto3.png':
            open_modal = st.button("🤖 Gerar análise com IA")
            if open_modal:
                modal.open()

            if modal.is_open():
                with modal.container():
                    st.write("🏡 Ambiente edificado")
                    st.image("casa.png", width=100)

elif selected_option == "Relatório automático":
    st.title("🏗️ Formulário de Fiscalização de Obra")

    with st.form("form_fiscalizacao_obra"):
        st.subheader("📍 Informações do Local")
        endereco = st.text_input("Endereço da obra:")

        st.subheader("📸 Fotos da Obra")
        fotos = st.file_uploader("Envie fotos do local", accept_multiple_files=True, type=["jpg", "jpeg", "png"])

        st.subheader("🆔 Identificação CREA")
        tem_adesivo = st.radio("Há adesivo do CREA visível?", ["Sim", "Não"])

        st.subheader("📞 Responsável pela Obra")
        nome_responsavel = st.text_input("Nome do responsável:")
        contato_responsavel = st.text_input("Contato (telefone ou e-mail):")

        st.subheader("📝 Observações adicionais")
        observacoes = st.text_area("Observações:")

        enviado = st.form_submit_button("Enviar")

    if enviado:
        st.success("✅ Formulário enviado com sucesso!")

        st.write("### 📋 Dados coletados:")
        st.write(f"**Endereço:** {endereco}")
        st.write(f"**Adesivo do CREA presente?** {tem_adesivo}")
        st.write(f"**Responsável:** {nome_responsavel}")
        st.write(f"**Contato:** {contato_responsavel}")
        st.write(f"**Observações:** {observacoes}")

elif selected_option == "Rotas de Fiscalização":
    st.subheader("🧭 IA para ajudar em mapeamento de rota a partir de palavras-chave")

    keywords = st.text_input("📝 Digite palavras-chave:", "")

    hospitais = [
    {
        "nome": "Hospital de Emergência e Trauma Dom Luiz Gonzaga Fernandes",
        "endereco": "Av. Floriano Peixoto, 4700 – Bairro das Malvinas",
        "telefone": "(83) 3310-5850"
    },
    {
        "nome": "Hospital da FAP (Fundação Assistencial da Paraíba)",
        "endereco": "Av. Dr. Francisco Pinto de Oliveira, s/n – Universitário",
        "telefone": "(83) 2102-0300"
    },
    {
        "nome": "Hospital HELP",
        "endereco": "Av. Prefeito Severino Bezerra Cabral, 162 – Catolé",
        "telefone": "(83) 3337-3232"
    },
    {
        "nome": "Hospital Universitário Alcides Carneiro (HUAC/UFCG)",
        "endereco": "Rua Carlos Chagas, s/n – Bairro São José",
        "telefone": "(83) 2101-9200"
    },
    {
        "nome": "Hospital Campina Grande",
        "endereco": "Rua Treze de Maio, 393 – Centro",
        "telefone": "(83) 3341-2773"
    },
    {
        "nome": "Hospital Unimed Campina Grande",
        "endereco": "Av. Vigário Calixto, 100 – Catolé",
        "telefone": "(83) 2101-8000"
    },
    {
        "nome": "Hospital de Clínicas de Campina Grande",
        "endereco": "Rua Siqueira Campos – Bairro São José",
        "telefone": "(83) 3322-7893"
    }]
    if st.button("🔍 Buscar informações"):
        if keywords:
            for hospital in hospitais:
                st.markdown(f"### 🏥 {hospital['nome']}")
                st.write(f"📍 Endereço: {hospital['endereco']}")
                st.write(f"📞 Telefone: {hospital['telefone']}")
                st.markdown("---")

        else:
            st.write('ok')

elif selected_option == "About":
    st.title("About")
    st.write("This app was built with Streamlit.")

import streamlit as st
from PIL import Image
from streamlit_modal import Modal

st.set_page_config(page_title="creIA", page_icon="logo.png",  layout="wide")

cols = st.columns([1, 3, 1])
with cols[1]:
    selected_option = st.radio("", ["Overview", "Mapeamento de Obras", "Relatório automático",  "Rotas de Fiscalização", "Sobre"], horizontal=True)

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

    st.markdown('<h1 style="color: white;">🧠 CreIA: Inteligência que constrói, visão que previne</h1>', unsafe_allow_html=True)

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

    st.markdown(
    """
    <h3 style='color: white;'>
        Sistema inteligente para monitoramento urbano por meio da análise de imagens aéreas e identificação de obras em andamento 🛰️
    </h3>
    """,
    unsafe_allow_html=True
    )

    st.markdown("<p style='color: white; font-weight: bold;'>📤 Carregar um arquivo:</p>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("")

    if uploaded_file is not None:
        st.markdown("<p style='color: white;'>✅ Arquivo enviado com sucesso!</p>", unsafe_allow_html=True)
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

        else:
            open_modal = st.button("🤖 Gerar análise com IA")
            if open_modal:
                modal.open()

            if modal.is_open():
                with modal.container():
                    st.write("🔍 Lamentamos, mas ainda não reconhecemos essa imagem.")

elif selected_option == "Relatório automático":
    st.markdown(
        "<h1 style='color: white;'>🏗️ Formulário de Fiscalização de Obra</h1>",
        unsafe_allow_html=True
    )


    with st.form("form_fiscalizacao_obra"):
        st.markdown(
            "<h3 style='color: white;'>📍 Endereço da obra</h3>",
            unsafe_allow_html=True
        )
        endereco = st.text_input("Endereço:")
        coord = st.text_input("Coordenadas geográficas:")

        st.markdown(
            "<h3 style='color: white;'>📸 Envie fotos da obra</h3>",
            unsafe_allow_html=True
        )
        fotos = st.file_uploader("", accept_multiple_files=True, type=["jpg", "jpeg", "png"])

        st.markdown(
            "<h3 style='color: white;'>🆔 Há adesivo do CREA visível?</h3>",
            unsafe_allow_html=True
        )
        tem_adesivo = st.radio("", ["Sim", "Não"])

        st.markdown(
            "<h3 style='color: white;'>📞 Responsável pela Obra</h3>",
            unsafe_allow_html=True
        )
        nome_responsavel = st.text_input("Nome do responsável:")
        contato_responsavel = st.text_input("Contato (telefone ou e-mail):")
        cpf_responsavel = st.text_input("CPF/CNPJ do responsável:")

        st.markdown(
            "<h3 style='color: white;'>📝 Observações adicionais</h3>",
            unsafe_allow_html=True
        )
        observacoes = st.text_area("Descrição da obra:")
        obs_2 = st.text_area("Atividades da obra:")

        enviado = st.form_submit_button("Enviar")

    if enviado:
        st.success("✅ Formulário enviado com sucesso!")

        st.markdown("<h3 style='color: white;'>📋 Dados coletados:</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: white;'><strong>Endereço:</strong> {endereco}, {coord}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: white;'><strong>Adesivo do CREA presente?</strong> {tem_adesivo}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: white;'><strong>Responsável:</strong> {nome_responsavel}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: white;'><strong>Contato:</strong> {contato_responsavel}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: white;'><strong>CPF/CNPJ:</strong> {cpf_responsavel}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: white;'><strong>Descrição da obra:</strong> {observacoes}</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: white;'><strong>Atividades da obra:</strong> {obs_2}</p>", unsafe_allow_html=True)

elif selected_option == "Rotas de Fiscalização":
    st.markdown(
        "<h3 style='color: white;'>🧭 IA para ajudar em mapeamento de rota a partir de palavras-chave</h3>",
        unsafe_allow_html=True
    )

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
                st.markdown(f"<h3 style='color: white;'>🏥 {hospital['nome']}</h3>", unsafe_allow_html=True)
                st.markdown(f"<p style='color: white;'>📍 <strong>Endereço:</strong> {hospital['endereco']}</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='color: white;'>📞 <strong>Telefone:</strong> {hospital['telefone']}</p>", unsafe_allow_html=True)
                st.markdown("<hr style='border: 1px solid white;'>", unsafe_allow_html=True)

elif selected_option == "Sobre":
    st.header("📘 MANUAL DE UTILIZAÇÃO – SISTEMA CRE-IA")

    # Objetivo
    st.header("📌 1. OBJETIVO DO SISTEMA")
    st.markdown("""
    O **CRE-IA** é uma plataforma de inteligência artificial aplicada à fiscalização de obras.
    Ela permite:
    - Identificar construções irregulares
    - Gerar relatórios automáticos
    - Traçar rotas de fiscalização com base em dados públicos e imagens georreferenciadas
    """)

    st.markdown("---")

    # Menu Principal
    st.header("🧭 2. MENU PRINCIPAL")
    st.subheader("2.1 🔍 Mapeamento de Obras")
    st.markdown("""
    **Objetivo:** identificar automaticamente a existência de obras em imagens.

    **Como usar:**
    1. Clique na aba “Mapeamento de Obras”.
    2. Faça upload de uma imagem aérea (.jpg).
    3. O sistema irá:
    - Detectar construções presentes
    - Informar coordenadas geográficas (latitude e longitude)
    - Fornecer endereço aproximado com base na geolocalização

    ✅ Ideal para confirmar a existência de obras em áreas suspeitas ou distantes.
    """)

    st.markdown("---")

    st.subheader("2.2 📄 Relatório Automático")
    st.markdown("""
    **Objetivo:** gerar um relatório técnico com base nas informações coletadas da obra.

    **Como usar:**
    1. Acesse a aba “Relatório Automático”.
    2. Preencha os campos solicitados:
    - Localização
    - Coordenadas
    - Tipo de obra
    - Situação encontrada
    - Responsável técnico (se houver)
    3. O sistema compilará automaticamente um relatório em texto formal e técnico.

    ✅ Útil para gerar relatórios padronizados prontos para anexar a processos ou enviar ao CREA.
    """)

    st.markdown("---")

    st.subheader("2.3 🗺️ Rotas de Fiscalização")
    st.markdown("""
    **Objetivo:** automatizar a identificação de locais a serem fiscalizados.

    **Como usar:**
    1. Acesse a aba “Rotas de Fiscalização”.
    2. Digite palavras-chave relacionadas aos empreendimentos (ex: “loteamento”, “construção civil”, “obra residencial”).
    3. O sistema realiza _data scraping_ no Google Maps e retorna:
    - Nome do empreendimento
    - Endereço
    - Coordenadas
    4. Os dados podem ser usados para montar a rota da fiscalização.

    ✅ Ferramenta ideal para planejar visitas técnicas com base em buscas inteligentes.
    """)

    st.markdown("---")

    # Considerações
    st.header("🛡️ 3. CONSIDERAÇÕES DE USO")
    st.markdown("""
    - O sistema é de uso técnico e restrito a profissionais vinculados ao CREA.
    - As imagens devem ser **nítidas e recentes** para maior precisão no mapeamento.
    - Os dados coletados devem ser **validados antes de qualquer autuação**.
    """)

    st.markdown("---")

    # Suporte
    st.header("🧾 4. SUPORTE E CONTATO")
    st.markdown("""
    Para dúvidas técnicas ou problemas de acesso, entre em contato com o suporte responsável pela plataforma via **e-mail institucional do CREA**.
    """)

# Importa o Streamlit para criar o site.
import streamlit as st

# Importa o Leafmap para criar o mapa.
import leafmap.foliumap as leafmap

# Importa a classe Localizador do arquivo localizador.py.
from localizador import Localizador

# Configura a página do Streamlit.
st.set_page_config(page_title="Mapa por nome do lugar", layout="wide")

# Cria o título principal do site.
st.title("Mapa por nome do lugar")

# Cria um texto explicativo para o usuário.
st.write("Digite o nome de uma cidade, país, estado ou região para visualizar no mapa.")

# Cria a barra de digitação do nome do lugar.
nome_lugar = st.text_input("Digite o nome do lugar", value="Rio de Janeiro")

# Cria o botão de busca.
botao_buscar = st.button("Buscar lugar")

# Verifica se o botão foi pressionado.
if botao_buscar:

    # Cria um objeto da classe Localizador.
    localizador = Localizador()

    # Mostra uma mensagem enquanto o programa faz a busca.
    with st.spinner("Buscando coordenadas do lugar..."):

        # Busca as coordenadas do lugar digitado.
        resultado = localizador.buscar_coordenadas(nome_lugar)

    # Verifica se nenhum lugar foi encontrado.
    if resultado is None:

        # Mostra uma mensagem de erro.
        st.error("Lugar não encontrado. Tente digitar outro nome.")

    # Caso o lugar tenha sido encontrado, executa este bloco.
    else:

        # Guarda a latitude encontrada.
        latitude = resultado["latitude"]

        # Guarda a longitude encontrada.
        longitude = resultado["longitude"]

        # Guarda o nome completo do lugar encontrado.
        nome_completo = resultado["nome"]

        # Mostra mensagem de sucesso.
        st.success(f"Lugar encontrado: {nome_completo}")

        # Mostra as coordenadas encontradas.
        st.write(f"Latitude: {latitude}")
        st.write(f"Longitude: {longitude}")

        # Cria um mapa centralizado na coordenada encontrada.
        mapa = leafmap.Map(center=[latitude, longitude], zoom=11)

        # Adiciona um marcador no mapa.
        mapa.add_marker(location=[latitude, longitude], popup=nome_completo)

        # Exibe o mapa no Streamlit.
        mapa.to_streamlit(height=600)

# Importa o Nominatim, que transforma o nome de um lugar em coordenadas.
from geopy.geocoders import Nominatim


# Cria a classe responsável por localizar lugares.
class Localizador:

    # Método construtor da classe.
    def __init__(self):

        # Cria o objeto geocodificador.
        self.geolocator = Nominatim(user_agent="meu_app_streamlit")

    # Método que recebe o nome do lugar e retorna suas coordenadas.
    def buscar_coordenadas(self, nome_lugar):

        # Faz a busca do lugar digitado pelo usuário.
        local = self.geolocator.geocode(nome_lugar)

        # Verifica se o local não foi encontrado.
        if local is None:

            # Retorna None caso nenhum resultado seja encontrado.
            return None

        # Retorna os dados do lugar encontrado.
        return {
            "nome": local.address,
            "latitude": local.latitude,
            "longitude": local.longitude,
        }

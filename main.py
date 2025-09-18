import requests
from bs4 import BeautifulSoup

# URL que vamos acessar
url = "https://surfguru.com.br/previsao/brasil/santa-catarina/florianopolis/praia-joaquina"

# Faz a requisição HTTP
response = requests.get(url)

# Verifica se deu certo
if response.status_code == 200:
    html = response.text
    print("Página acessada com sucesso!")
    
    # Salvar o HTML em um arquivo local
    with open("pagina.html", "w", encoding="utf-8") as f:
        f.write(html)
    
    # (Opcional) usar BeautifulSoup para analisar o HTML
    soup = BeautifulSoup(html, "html.parser")
    print("Título da página:", soup.title.string)
else:
    print("Erro ao acessar a página:", response.status_code)

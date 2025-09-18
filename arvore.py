import re
from bs4 import BeautifulSoup
import json
import pandas as pd

# Substitua pelo conteúdo do HTML baixado
import main
html = main.html

# Criar objeto BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Localizar todas as tags <script>
tags_script = soup.find_all("script")

# Procurar pela variável "var ondas =" em cada tag
for i, tag in enumerate(tags_script, start=1):
    conteudo_script = tag.get_text()  # Captura o conteúdo interno da tag
    if "var ondas =" in conteudo_script:  # Filtre apenas onde esta variável aparece
        print(f"\n[!] Variável 'var ondas =' encontrada na tag <script> {i}:")
        
        # Use regex para capturar o JSON ou estrutura completa
        match = re.search(r"var ondas\s*=\s*({.*?});", conteudo_script, re.DOTALL)
        if match:
            print("\nConteúdo da variável 'ondas':")
            print(match.group(1)) 
            dados_ondas = json.loads(match.group(1))
            
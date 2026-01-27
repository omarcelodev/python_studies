# O que é pip?
#   -pip = Python Package Installer

#   -Ele serve para baixar, instalar, atualizar e remover bibliotecas 

# Instalando uma biblioteca

# pip install nome_da_biblioteca

# Exemplo:
#   pip install requests

import requests


resposta = requests.get("https://api.github.com")
print(resposta.status_code)

# Desintalando/Atualizando uma biblioteca

# pip uninstall nome_da_biblioteca
# pip instal --upgrade nome

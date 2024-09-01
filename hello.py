"""Hello World multilínguas.

Dependendo da linguagem configurada no ambiente, 
o programa exibe a mensagem correspondente.

Como usar: Tenha a variável LANG configurada em seu ambiente.

  export LANG=pt_br

Execução: Executar o código do arquivo (python3 <nome-do-arquivo>).
"""
# Dunders
__version__ = "0.0.1"
__author__ = "Matheus"
__license__ = "unlicense"

# Script
import os 

current_language = os.getenv("LANG", "pt_BR")[:5]
msg = "Hello, World!"

if (current_language == "pt_BR"):
    msg = "Olá, mundo!"
elif (current_language == "it_IT"):
    msg = "Ciao, mondo!"
elif (current_language == "es_ES"):
    msg = "Hola, mundo!"
elif (current_language == "fr_FR"):
    msg = "Bonjour tout le monde!"

print(msg)
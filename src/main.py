import pyautogui
import time
import pandas as pd
from pathlib import Path

pyautogui.PAUSE = 1 # Entre cada comando demora 1s para executar

link_sistema = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

#------------------------------------------------------------------
    
### Passo 01: Entrar no sistema da empresa

# Pressiona Command + Space para abrir o Spotlight
pyautogui.keyDown("command")
pyautogui.press("space")
pyautogui.keyUp("command")
# Espera o Spotlight abrir
time.sleep(1)

# Abrir o safari
pyautogui.write("safari")
pyautogui.press("return")

# Digita o link do sistema e entra
pyautogui.write(link_sistema)
pyautogui.press("return")

# Fazer uma pausa maior pro site carregar
time.sleep(3)

#------------------------------------------------------------------

### Passo 02: Fazer login

# Posição onde está o campo E-mail no site
pyautogui.click(x=574, y=374)
pyautogui.write("pythonimpressionador@gmail.com")

# Passar para o próximo campo
pyautogui.press("tab")
pyautogui.write("sua senha muito muito muito dificilima")

# Passar para o botão Logar
pyautogui.click(x=853, y=540)
pyautogui.press("return")

# Fazer uma pausa maior pro formulario do site carregar
time.sleep(4)

#------------------------------------------------------------------

### Passo 03: Abrir a base de dados (importar o arquivo)

# Define o diretório raiz do projeto.
# __file__ pega o caminho do arquivo atual (codigo.py)
# resolve() transforma em caminho absoluto
# parent.parent sobe duas pastas (de src/ para a pasta principal do projeto)
BASE_DIR = Path(__file__).resolve().parent.parent

# Cria o caminho para a pasta onde estão os dados brutos (data/raw)
# Usar "/" com Path concatena caminhos de forma segura no sistema operacional
RAW = BASE_DIR / "data/raw"

tabela = pd.read_csv(RAW / "produtos.csv")
print(tabela)

#------------------------------------------------------------------

# Passo 05: Repetir o passo 04 até acabar a lista de produtos

# Para cada linha da minha tabela, vou 
for linha in tabela.index:
    # Passo 04: Cadastrar um produto

    # Clicar no campo do Codigo do Produto
    pyautogui.click(x=568, y=255)
    codigo = str(tabela.loc[linha, "codigo"]) # Transformar codigo em string para conseguir usar o write
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # Passar para o proximo campo - Marca do Produto
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    # Passar para o campo Tipo do Produto
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    # Passar para o campo Categoria do Produto
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    # Passar para o campo Preço Unitário do Produto
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    # Passar para o campo Custo do Produto
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    # Passar para o campo Obs
    obs = str(tabela.loc[linha, "obs"])
    # Se a observação estiver vazia, não escrever NaN
    if(obs != "nan"):
        pyautogui.write(obs)
    # Clicou no botão Enviar
    pyautogui.click(x=782, y=908)

    pyautogui.scroll(5000) # Scroll pro inicio da tela


#------------------------------------------------------------------
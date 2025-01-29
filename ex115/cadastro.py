import os

def criar(nome_arquivo, conteudo=""):
    """Cria um arquivo de texto e adiciona conteúdo opcional."""
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)
    print(f"Arquivo '{nome_arquivo}' criado com sucesso!")

def editar(nome_arquivo, novo_conteudo):
    """Edita um arquivo, substituindo todo o conteúdo existente."""
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(novo_conteudo)
        print(f"Arquivo '{nome_arquivo}' editado com sucesso!")
    else:
        print(f"Erro: O arquivo '{nome_arquivo}' não existe.")

def ler(nome_arquivo):
    """Lê e retorna o conteúdo de um arquivo."""
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            return arquivo.read()
    else:
        print(f"Erro: O arquivo '{nome_arquivo}' não existe.")
        return None

def apagar(nome_arquivo):
    """Apaga um arquivo do sistema."""
    if os.path.exists(nome_arquivo):
        os.remove(nome_arquivo)
        print(f"Arquivo '{nome_arquivo}' apagado com sucesso!")
    else:
        print(f"Erro: O arquivo '{nome_arquivo}' não existe.")
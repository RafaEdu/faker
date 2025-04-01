import random
import psycopg2

# Estabelecendo a conexão com o banco de dados (substitua com suas credenciais)
conect = psycopg2.connect(
    dbname="ticket1m",  # Substitua pelo nome do seu banco de dados
    user="postgres",  # Substitua pelo seu usuário do PostgreSQL
    password="postgres",  # Substitua pela sua senha do PostgreSQL
    host="localhost",
    port="5432"
)

def ler_arquivo_em_lista(caminho_arquivo):
    lista_linhas = []
    
    try:
        # Tente abrir o arquivo com a codificação 'utf-8'
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                lista_linhas.append(linha.strip())  # Remover quebras de linha extras
    except UnicodeDecodeError:
        print("Erro de codificação ao ler o arquivo. Tentando com 'latin1'.")
        try:
            # Tentando 'latin1' caso o 'utf-8' falhe
            with open(caminho_arquivo, 'r', encoding='latin1') as arquivo:
                for linha in arquivo:
                    lista_linhas.append(linha.strip())
        except FileNotFoundError:
            print(f"O arquivo {caminho_arquivo} não foi encontrado.")
    
    return lista_linhas

caminho = 'lista_municipios.txt'  # Caminho para o arquivo de cidades
cidades = ler_arquivo_em_lista(caminho)  # Lê o arquivo e armazena as cidades

def inserir_dados_cidade(cidades):
    cursor = conect.cursor()
    sql = "INSERT INTO cidade (idcidade, nome, estado_idestado) VALUES (%s, %s, %s)"
    id_cidade = 1  # Começa o id das cidades de 1
    for cidade in cidades:
        # Inserir cada cidade com um ID único e um estado aleatório entre 1 e 27
        cursor.execute(sql, (id_cidade, cidade, random.randint(1, 27)))
        id_cidade += 1  # Incrementa o id para a próxima cidade
    
    conect.commit()  # Confirma as alterações no banco de dados
    cursor.close()  # Fecha o cursor

# Chama a função para inserir as cidades no banco de dados
inserir_dados_cidade(cidades)

# Fecha a conexão com o banco de dados
conect.close()

print("Cidades inseridas com sucesso!")

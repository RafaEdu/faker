import psycopg2
import random
import string

# Conectar ao banco de dados
conect = psycopg2.connect(
    dbname="ticket1m",  
    user="postgres",  
    password="postgres",  
    host="localhost",
    port="5432"
)

cursor = conect.cursor()

def generate_plate():
    """Gera uma placa no formato LLLNLNN (L = letra, N = número)."""
    return (
        "".join(random.choices(string.ascii_uppercase, k=3)) +
        str(random.randint(0, 9)) +
        random.choice(string.ascii_uppercase) +
        str(random.randint(0, 9)) +
        str(random.randint(0, 9))
    )

# Garantir placas únicas
plates = set()
while len(plates) < 500:
    plates.add(generate_plate())

# Query SQL atualizada para incluir a coluna tipo_veiculo_idtipo_veiculo
insert_query = """
INSERT INTO veiculos (idveiculos, placa, modelo_idmodelo, cidade_idcidade, tipo_veiculo_idtipo_veiculo) 
VALUES (%s, %s, %s, %s, %s)
"""

for i, plate in enumerate(plates, start=1):
    idmodelo = random.randint(1, 50)
    cidade_idcidade = random.randint(1, 5570)
    tipo_veiculo = random.randint(1, 7)  # Novo campo, valores entre 1 e 7

    cursor.execute(insert_query, (i, plate, idmodelo, cidade_idcidade, tipo_veiculo))

# Confirmar e fechar conexão
conect.commit()
cursor.close()
conect.close()

print("500 registros inseridos com sucesso!")

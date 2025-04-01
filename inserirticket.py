import psycopg2
import random
from datetime import datetime, timedelta

conect = psycopg2.connect(
    dbname="ticket1m",  
    user="postgres",  
    password="postgres",  
    host="localhost",
    port="5432"
)

cursor = conect.cursor()

def random_datetime_2024():
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31, 23, 59, 59)
    delta = end_date - start_date
    random_seconds = random.randint(0, int(delta.total_seconds())) 
    return start_date + timedelta(seconds=random_seconds)


# Inserção otimizada com batch inserts
insert_query = """
INSERT INTO ticket (idticket, data_hora, praca_idpraca, veiculos_idveiculos) 
VALUES (%s, %s, %s, %s)
"""

batch_size = 10000  
data_batch = []

for i in range(1, 1_000_001):  # Gera 1 milhão de registros
    data_hora = random_datetime_2024()
    praca_idpraca = random.randint(1, 10)
    veiculos_idveiculos = random.randint(1, 500)
    
    data_batch.append((i, data_hora, praca_idpraca, veiculos_idveiculos))

    if len(data_batch) == batch_size:
        cursor.executemany(insert_query, data_batch)
        conect.commit()  
        data_batch = []  

if data_batch:
    cursor.executemany(insert_query, data_batch)
    conect.commit()

cursor.close()
conect.close()

print("1 milhão de registros inseridos com sucesso!")
headers = {'charset': 'utf-8'}
import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask , request, jsonify


INSERT_ATOR = (
    "INSERT INTO sistema.ator(primeiro_nome, sobrenome, data_nasc) VALUES (%s,%s,%s)"
)

SELECT_ATOR = (
    "SELECT primeiro_nome, sobrenome, data_nasc, id_premios FROM sistema.ator WHERE sobrenome LIKE %s" 
)

DELETE_ATOR = (
    "DELETE FROM sistema.ator WHERE sobrenome ILIKE %s "
)

load_dotenv()

app = Flask(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)

@app.post("/api/insert")
def insert_ator():
    data = request.get_json() # -- dicionário de dados
    primeiro_nome = data["primeiro_nome"]
    sobrenome = data["sobrenome"]
    data_nasc = data["data_nasc"]
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_ATOR, (primeiro_nome,sobrenome,data_nasc, ))
            ator_id = cursor.fetchone()[0]
    return {"id": ator_id, "message": f"Ator(a) {primeiro_nome} inserido!"}

@app.get('/api/atores')
def consultar_atores():
    try:
        data = request.get_json()
        sobrenome = data ["sobrenome"]
        with connection:
            with connection.cursor() as cursor:
        # Executa a consulta SQL predefinida com o valor do parâmetro sobrenome
                cursor.execute(SELECT_ATOR, (f'%{sobrenome}%',))

                resultados = cursor.fetchall()

            cursor.close()
            resultado_json = []
            for resultado in resultados:
                resultado_json.append({
                    'primeiro_nome': resultado[0],
                    'sobrenome': resultado[1],
                    'data_nasc': resultado[2],
                    'id_premios': resultado[3]
                })

            return jsonify(resultado_json)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.get('/api/delete')
def deletar_atores():
    data = request.get_json()
    sobrenome = data ["sobrenome"]
    with connection:
        with connection.cursor() as cursor:
        # Executa a consulta SQL predefinida com o valor do parâmetro sobrenome
            cursor.execute(DELETE_ATOR, (f'%{sobrenome}%',))
        return {"message": f"Ator(a) {sobrenome} Deletado!"}    
    
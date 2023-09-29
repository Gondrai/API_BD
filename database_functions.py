import os
import psycopg2
from dotenv import load_dotenv

INSERT_ATOR = (
    "INSERT INTO sistema.ator(primeiro_nome, sobrenome, data_nasc, id_premios) VALUES (%s,%s,%s,%s)"
) # Inserir ator 

SELECT_ATOR = (
    "SELECT primeiro_nome, sobrenome, data_nasc, id_premios FROM sistema.ator WHERE sobrenome LIKE %s" 
) # Selecionar ator 

DELETE_ATOR = (
    "DELETE FROM sistema.ator WHERE sobrenome ILIKE %s and primeiro_nome = %s "
) # Deletar ator 

UPDATE_ATOR = (
    "UPDATE sistema.ator SET primeiro_nome = %s , sobrenome = %s , data_nasc = %s , id_premios =  %s WHERE primeiro_nome = %s and sobrenome = %s"
) # Atualizar ator 

INSERT_FILME = (
    "INSERT INTO sistema.filme (idioma_original, titulo, subtitulo, sinopse, ano, duracao, id_premios, id_roteirista, id_diretor) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
) # Inserir filme 

SELECT_FILME = (
    "SELECT idioma_original, titulo, subtitulo, sinopse, ano, duracao, id_premios FROM sistema.filme WHERE titulo LIKE %s" 
) # Selecionar filme 

DELETE_FILME = (
    "DELETE FROM sistema.filme WHERE titulo ILIKE %s and subtitulo ILIKE %s "
) # Deletar filme 


UPDATE_FILME = (
    "UPDATE sistema.filme SET titulo='%s', subtitulo='%s', idioma_original='%s', sinopse='%s, ano='%s', duracao='%s' WHERE titulo ILIKE '%s'"
) # Atualizar filme 

load_dotenv()
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)

def insert_atores(primeiro_nome, sobrenome, data_nasc, id_premios):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_ATOR, (primeiro_nome, sobrenome, data_nasc,id_premios))
            ator_id = cursor.fetchone()[0]
    return ator_id

def select_atores(sobrenome):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_ATOR, (f'%{sobrenome}%',))
            resultados = cursor.fetchall()
        
        resultado_json = []
        for resultado in resultados:
            resultado_json.append({
                'primeiro_nome': resultado[0],
                'sobrenome': resultado[1],
                'data_nasc': resultado[2],
                'id_premios': resultado[3]
            })

        return resultado_json

def delete_atores(sobrenome, primeiro_nome):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(DELETE_ATOR, (sobrenome, primeiro_nome))
    return f"Ator(a) {sobrenome} Deletado!"


def update_atores(primeiro_nome, sobrenome, data_nasc, id_premios):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_ATOR, (primeiro_nome, sobrenome, data_nasc, id_premios))
            ator_id = cursor.fetchone()[0]
    return ator_id


def insert_filme(idioma_original, titulo, subtitulo, sinopse, ano, duracao, id_premios, id_roteirista, id_diretor):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_FILME, (idioma_original, titulo, subtitulo, sinopse, ano, duracao, id_premios, id_roteirista, id_diretor))
            filme_id = cursor.fetchone()[0]
    return filme_id





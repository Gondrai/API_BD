import os
import psycopg2
from dotenv import load_dotenv

INSERT_ATOR = (
    "INSERT INTO sistema.ator(primeiro_nome, sobrenome, data_nasc) VALUES (%s, %s,%s) RETURNING id_ator"
    )
 # Inserir ator 


SELECT_ATOR = (
    "SELECT primeiro_nome, sobrenome, data_nasc, id_premios FROM sistema.ator WHERE sobrenome ILIKE %s and primeiro_nome ILIKE %s" 
) # Selecionar ator 

DELETE_ATOR = (
   "DELETE FROM sistema.ator WHERE sobrenome ILIKE %s and primeiro_nome = %s"
) # Deletar ator 

UPDATE_ATOR = (
    "UPDATE sistema.ator SET primeiro_nome = %s, sobrenome = %s, data_nasc = %s, id_premios = %s WHERE primeiro_nome = %s and sobrenome = %s"
) # Atualizar ator 

INSERT_FILME = (
    "INSERT INTO sistema.filme (idioma_original, titulo, subtitulo, sinopse, ano, duracao, id_premios, id_roteirista, id_diretor) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id_filme"
) # Inserir filme 

SELECT_FILME = (
    "SELECT idioma_original, titulo, subtitulo, sinopse, ano, duracao, id_premios, id_roteirista, id_diretor FROM sistema.filme WHERE titulo ILIKE %s" 
) # Selecionar filme 

DELETE_FILME = (
    "DELETE FROM sistema.filme WHERE titulo ILIKE %s and subtitulo ILIKE %s"
) # Deletar filme 


UPDATE_FILME = (
    "UPDATE sistema.filme SET titulo=%s, subtitulo=%s, idioma_original=%s, sinopse=%s, ano=%s, duracao=%s WHERE titulo ILIKE %s"
) # Atualizar filme 

load_dotenv()
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)

def insert_atores(primeiro_nome, sobrenome, data_nasc):
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(INSERT_ATOR, (primeiro_nome, sobrenome, data_nasc))
                ator_id = cursor.fetchone()[0]
        connection.commit()  
        return ator_id
    except psycopg2.Error as e:
        
        return None


def select_atores(sobrenome, primeiro_nome):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_ATOR, (sobrenome, primeiro_nome))
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
            cursor.execute(UPDATE_ATOR, (primeiro_nome, sobrenome, data_nasc, id_premios, primeiro_nome, sobrenome))
            ator_id = cursor.fetchone()[0]
    return ator_id


def insert_filme(idioma_original, titulo, subtitulo, sinopse, ano, duracao, id_premios, id_roteirista, id_diretor):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_FILME, (idioma_original, titulo, subtitulo, sinopse, ano, duracao, id_premios, id_roteirista, id_diretor))
            filme_id = cursor.fetchone()[0]
    return filme_id

def select_filmes(titulo):
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(SELECT_FILME, (f'%{titulo}%',))
                resultados = cursor.fetchall()

        resultado_json = []
        for resultado in resultados:
            resultado_json.append({
                'idioma_original': resultado[0],
                'titulo': resultado[1],
                'subtitulo': resultado[2],
                'sinopse': resultado[3],
                'ano': resultado[4],
                'duracao': resultado[5],
                'id_premios': resultado[6],
                'id_roteirista': resultado[7],
                'id_diretor': resultado[8]
            })

        return resultado_json
    except psycopg2.Error as e:
        # Trate a exceção aqui, por exemplo, registrando-a ou retornando uma mensagem de erro
        return []

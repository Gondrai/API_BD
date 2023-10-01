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
    "UPDATE sistema.ator SET primeiro_nome = %s, sobrenome = %s, data_nasc = %s WHERE id_ator = %s RETURNING id_ator"
) # Atualizar ator 

INSERT_FILME = (
    "INSERT INTO sistema.filme (idioma_original, titulo, subtitulo, sinopse, ano, duracao, id_roteirista, id_diretor) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id_filme"
) # Inserir filme 

SELECT_FILME = (
    "SELECT idioma_original, titulo, subtitulo, sinopse, ano, duracao, id_roteirista, id_diretor FROM sistema.filme WHERE titulo ILIKE %s" 
) # Selecionar filme 

DELETE_FILME = (
    "DELETE FROM sistema.filme WHERE titulo ILIKE %s and subtitulo ILIKE %s"
) # Deletar filme 


UPDATE_FILME = (
    "UPDATE sistema.filme SET titulo=%s, subtitulo=%s, idioma_original=%s, sinopse=%s, ano=%s, duracao=%s, id_roteirista= %s, id_diretor= %s WHERE id_filme=%s RETURNING id_filme"
) # Atualizar filme 

INSERT_RELACIONAMENTO = (
    "INSERT INTO sistema.rel_papel_ator_filme(id_papel, id_ator, id_filme) VALUES (%s, %s,%s) RETURNING id_relacionamento"
    )
SELECT_RELACIONAMENTO = (
    "SELECT id_papel, id_ator, id_filme, id_relacionamento FROM sistema.rel_papel_ator_filme WHERE id_relacionamento = %s" 
)

DELETE_RELACIONAMENTO = (
   "DELETE FROM sistema.rel_papel_ator_filme WHERE id_relacionamento = %s"
) # Deletar RELACIONAMENTO 

UPDATE_RELACIONAMENTO = (
    "UPDATE sistema.rel_papel_ator_filme SET id_papel = %s, id_ator = %s, id_filme = %s WHERE id_relacionamento = %s RETURNING id_relacionamento"
)

load_dotenv()
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)

def insert_atores(primeiro_nome, sobrenome, data_nasc):
    if not primeiro_nome or not sobrenome or not data_nasc:
        return {"error": "Todos os campos (primeiro_nome, sobrenome, data_nasc) são obrigatórios."}

    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(INSERT_ATOR, (primeiro_nome, sobrenome, data_nasc))
                id_ator = cursor.fetchone()[0]
        connection.commit()
        return {"id": id_ator, "message": f"Ator(a) {primeiro_nome} inserido!"}
    except psycopg2.Error as e:
        return {"error": str(e)}


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
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(DELETE_ATOR, (sobrenome, primeiro_nome))
        if cursor.rowcount == 0:
            # Se nenhum registro foi excluído (rowcount = 0), significa que o ator não foi encontrado
            return f"Ator(a) {sobrenome} não encontrado na tabela."
        else:
            return f"Ator(a) {sobrenome} Deletado!"
    except psycopg2.Error as e:
        return f"Erro ao excluir o ator: {str(e)}"


def update_atores(id_ator, primeiro_nome, sobrenome, data_nasc):
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(UPDATE_ATOR, (primeiro_nome, sobrenome, data_nasc, id_ator))
                result = cursor.fetchone()
                if result:
                    id_ator = result[0]
                    connection.commit()
                    return {"id": id_ator, "message": f"Ator(a) com ID {id_ator} atualizado!"}
                else:
                    return {"error": "Ator não encontrado para atualização."}
    except psycopg2.Error as e:
        return {"error": str(e)}

def insert_filme(idioma_original, titulo, subtitulo, sinopse, ano, duracao, id_roteirista, id_diretor):
    if not titulo or not ano or not duracao:
        return {"error": "Os campos obrigatórios (titulo, ano, duracao) não podem estar vazios."}

    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    INSERT_FILME,
                    (idioma_original, titulo, subtitulo, sinopse, ano, duracao, id_roteirista, id_diretor),
                )
                filme_id = cursor.fetchone()[0]
        return {"id": filme_id, "message": f"Filme {titulo} inserido com sucesso!"}
    except psycopg2.Error as e:
        return {"error": str(e)}

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
                'id_roteirista': resultado[6],
                'id_diretor': resultado[7]
            })

        if not resultado_json:
            return {"message": "Nenhum filme encontrado com base no título fornecido."}

        return resultado_json
    except psycopg2.Error as e:
        return {"error": str(e)}
    
def delete_filmes(titulo, subtitulo):
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(DELETE_FILME, (f'%{titulo}%', f'%{subtitulo}%'))
        if cursor.rowcount == 0:
            # Se nenhum registro foi excluído (rowcount = 0), significa que o filme não foi encontrado
            return f"Filme(a) {titulo}, {subtitulo} não encontrado na tabela."
        else:
            
            return f"Filme(a) {titulo}, {subtitulo} Deletado!"
    except psycopg2.Error as e:
        return f"Erro ao excluir o filme: {str(e)}"

def update_filmes(id_filme, idioma_original, titulo, subtitulo, sinopse, ano, duracao, id_roteirista, id_diretor):
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(UPDATE_FILME, (titulo, subtitulo, idioma_original, sinopse, ano, duracao,id_roteirista,id_diretor, id_filme))
                result = cursor.fetchone()
                if result:
                    id_filme = result[0]
                    connection.commit()
                    return {"id": id_filme, "message": f"Filme(a) com ID {id_filme} atualizado!"}
                else:
                    return {"error": "Filme não encontrado para atualização."}
    except psycopg2.Error as e:
        return {"error": str(e)}
    
    
def insert_relacionamento(id_papel, id_ator, id_filme):
    if not id_papel or not id_ator or not id_filme:
        return {"error": "Todos os campos (id_papel, id_ator, id_filme) são obrigatórios."}

    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(INSERT_RELACIONAMENTO, (id_papel, id_ator, id_filme))
                id_relacionamento = cursor.fetchone()[0]
        connection.commit()
        return {"id": id_relacionamento, "message": f"Relacionamento(a) {id_relacionamento} inserido!"}
    except psycopg2.Error as e:
        return {"error": str(e)}
    
def select_relacionamentos(id_relacionamento):
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(SELECT_RELACIONAMENTO, (id_relacionamento,))
                resultados = cursor.fetchall()
        
        if not resultados:
            return {"error": "ID de relacionamento não encontrado na tabela."}
        
        resultado_json = []
        for resultado in resultados:
            resultado_json.append({
                'id_papel': resultado[0],
                'id_ator': resultado[1],
                'id_filme': resultado[2],
                'id_relacionamento': resultado[3]
            })

        return resultado_json
    except psycopg2.Error as e:
        # Trate a exceção aqui, por exemplo, registrando-a ou retornando uma mensagem de erro
        return {"error": str(e)}
    
def delete_relacionamentos(id_relacionamento):
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(DELETE_RELACIONAMENTO, (id_relacionamento,))
        if cursor.rowcount == 0:
            # Se nenhum registro foi excluído (rowcount = 0), significa que o ator não foi encontrado
            return f"Relacionamento(a) {id_relacionamento} não encontrado na tabela."
        else:
            return f"Relacionamento(a) {id_relacionamento} Deletado!"
    except psycopg2.Error as e:
        return f"Erro ao excluir o Relacionamento: {str(e)}"
    
    
def update_relacionamentos(id_relacionamento, id_papel, id_ator, id_filme):
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(UPDATE_RELACIONAMENTO, (id_papel, id_ator, id_filme, id_relacionamento))
                result = cursor.fetchone()
                if result:
                    id_relacionamento = result[0]
                    connection.commit()
                    return {"id": id_relacionamento, "message": f"Relacionamento(a) com ID {id_relacionamento} atualizado!"}
                else:
                    return {"error": "Relacionamento não encontrado para atualização."}
    except psycopg2.Error as e:
        return {"error": str(e)}
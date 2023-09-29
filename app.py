headers = {'charset': 'utf-8'}
from flask import Flask, request, jsonify
from database_functions import insert_atores, select_atores, delete_atores, update_atores, insert_filme, select_filmes

app = Flask(__name__)

@app.post("/api/inserir_atores")
def insert_ator_route():
    data = request.get_json()
    primeiro_nome = data["primeiro_nome"]
    sobrenome = data["sobrenome"]
    data_nasc = data["data_nasc"]
    id_premios = data["id_premios"]
    id_ator = insert_atores(primeiro_nome, sobrenome, data_nasc, id_premios)
    return {"id": id_ator, "message": f"Ator(a) {primeiro_nome} inserido!"}

@app.get('/api/consultar_atores')
def consultar_atores_route():
    try:
        data = request.get_json()
        sobrenome = data["sobrenome"]
        primeiro_nome = data["primeiro_nome"]
        resultados = select_atores(sobrenome, primeiro_nome)
        return jsonify(resultados)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.get('/api/deletar_atores')
def deletar_atores_route():
    data = request.get_json()
    sobrenome = data["sobrenome"]
    message = delete_atores(sobrenome)
    return {"message": message}

@app.post('/api/atualizar_atores')
def atualizar_atores_route():
    data = request.get_json()
    sobrenome = data["sobrenome"]
    primeiro_nome = data["primeiro_nome"]
    message = update_atores(sobrenome, primeiro_nome)
    return {"message": message}

@app.post('/api/inserir_Filmes')
def inserir_filmes_route():
    data = request.get_json()
    idioma_original = data["idioma_original"]
    titulo = data["titulo"]
    subtitulo = data["subtitulo"]
    sinopse = data["sinopse"]
    ano = data["ano"]
    duracao = data["duracao"]
    id_premios = data["id_premios"]
    id_roteirista = data["id_roteirista"]
    id_diretor = data["id_roteirista"]
    id_filme = insert_filme(idioma_original, titulo, subtitulo, sinopse, ano, duracao, id_premios, id_roteirista, id_diretor)
    return {"id": id_filme, "message": f"Ator(a) {titulo} inserido!"}

@app.get('/api/selecionar_filmes')
def consultar_filmes_route():
    try:
        data = request.get_json()
        idioma_original = data["idioma_original"]
        titulo = data["titulo"]
        subtitulo = data["subtitulo"]
        sinopse = data["sinopse"]
        ano = data["ano"]
        duracao = data["duracao"]
        id_premios = data["id_premios"]
        id_roteirista = data["id_roteirista"]
        id_diretor = data["id_diretor"]
        resultados = select_filmes(idioma_original, titulo, subtitulo, sinopse, ano, duracao, id_premios, id_roteirista, id_diretor)
        return jsonify(resultados)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    app.run()

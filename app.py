headers = {'charset': 'utf-8'}
from flask import Flask, request, jsonify

from database_functions import update_relacionamentos, delete_relacionamentos, select_relacionamentos, insert_atores, select_atores, delete_atores, update_atores, insert_filme, select_filmes, delete_filmes, update_filmes,insert_relacionamento

app = Flask(__name__)

@app.post("/api/inserir_ator")
def insert_ator_route():
    data = request.get_json()
    primeiro_nome = data.get("primeiro_nome")
    sobrenome = data.get("sobrenome")
    data_nasc = data.get("data_nasc")
    
    result = insert_atores(primeiro_nome, sobrenome, data_nasc)
    
    if "error" in result:
        return {"error": result["error"]}
    
    return result


@app.get('/api/consultar_ator')
def consultar_atores_route():
    try:
        data = request.get_json()
        sobrenome = data["sobrenome"]
        primeiro_nome = data["primeiro_nome"]
        resultados = select_atores(sobrenome, primeiro_nome)
        return jsonify(resultados)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.get('/api/deletar_ator')
def deletar_atores_route():
    try:
        data = request.get_json()
        sobrenome = data["sobrenome"]
        primeiro_nome = data["primeiro_nome"]
        message = delete_atores(sobrenome, primeiro_nome)
        return {"message": message}
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.put("/api/atualizar_ator/<int:id_ator>")
def update_ator_route(id_ator):
    data = request.get_json()
    primeiro_nome = data.get("primeiro_nome")
    sobrenome = data.get("sobrenome")
    data_nasc = data.get("data_nasc")
    result = update_atores(id_ator, primeiro_nome, sobrenome, data_nasc)
    
    if "error" in result:
        return {"error": result["error"]}
    
    return result

@app.post('/api/inserir_Filme')
def inserir_filmes_route():
    try:
        data = request.get_json()
        idioma_original = data.get("idioma_original")
        titulo = data.get("titulo")
        subtitulo = data.get("subtitulo")
        sinopse = data.get("sinopse")
        ano = data.get("ano")
        duracao = data.get("duracao")
        id_roteirista = data.get("id_roteirista")
        id_diretor = data.get("id_diretor")
        
        if not titulo or not ano or not duracao:
            return {"error": "Os campos obrigatórios (titulo, ano, duracao) não podem estar vazios."}
        
        id_filme = insert_filme(idioma_original, titulo, subtitulo, sinopse, ano, duracao, id_roteirista, id_diretor)
        return {"id": id_filme, "message": f"Filme {titulo} inserido com sucesso!"}
    except Exception as e:
        return {"error": str(e)}

@app.get('/api/consultar_filme')
def consultar_filmes_route():
    try:
        data = request.get_json()
        titulo = data.get("titulo")
        resultados = select_filmes(titulo)

        if "error" in resultados:
            return jsonify(resultados), 500

        return jsonify(resultados)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.get('/api/deletar_filme')
def deletar_filmes_route():
    try:
        data = request.get_json()
        titulo = data.get("titulo")
        subtitulo = data.get("subtitulo")
        message = delete_filmes(titulo, subtitulo)
        return {"message": message}
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
@app.put("/api/atualizar_filme/<int:id_filme>")
def update_filme_route(id_filme):
    data = request.get_json()
    idioma_original = data.get("idioma_original")
    titulo = data.get("titulo")
    subtitulo = data.get("subtitulo")
    sinopse = data.get("sinopse")
    ano = data.get("ano")
    duracao = data.get("duracao")
    id_roteirista = data.get("id_roteirista")
    id_diretor = data.get("id_diretor")
    result = update_filmes(id_filme, idioma_original, titulo, subtitulo, sinopse, ano, duracao, id_roteirista, id_diretor)
    
    if "error" in result:
        return {"error": result["error"]}
    
    return result


@app.post("/api/inserir_relacionamento")
def insert_relacionamento_route():
    data = request.get_json()
    id_papel = data.get("id_papel")
    id_ator = data.get("id_ator")
    id_filme = data.get("id_filme")
    
    result = insert_relacionamento(id_papel, id_ator, id_filme)
    
    if "error" in result:
        return {"error": result["error"]}
    
    return result

@app.get('/api/consultar_relacionamento')
def consultar_relacionamento_route():
    try:
        data = request.get_json()
        id_relacionamento = int(data["id_relacionamento"])
        resultados = select_relacionamentos(id_relacionamento)
        
        if "error" in resultados:
            return jsonify(resultados), 404  # Retorne um código de status 404 (Not Found) quando o ID não existir
        
        return jsonify(resultados)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.get('/api/deletar_relacionamento')
def deletar_relacionamento_route():
    try:
        data = request.get_json()
        id_relacionamento = int(data["id_relacionamento"])
        message = delete_relacionamentos(id_relacionamento)
        return {"message": message}
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
@app.put("/api/atualizar_relacionamento/<int:id_relacionamento>")
def update_relacionamento_route(id_relacionamento):
    data = request.get_json()
    id_papel = data.get("id_papel")
    id_ator = data.get("id_ator")
    id_filme = data.get("id_filme")
    result = update_relacionamentos(id_relacionamento, id_papel, id_ator, id_filme)
    
    if "error" in result:
        return {"error": result["error"]}
    
    return result


if __name__ == "__main__":
    app.run()
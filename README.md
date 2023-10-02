# API | BANCO DE DADOS

Repositório para armazenar API, CRUD e QUERYS solicitadas na última etapa da matéria de banco de dados.

Tecnologias utilizadas:
- [Python](https://web.dio.me) 🐍

## 💻 Arquivos

| Título | Função |
|-------|---------|
|app.py| [Rotas](app.py)|
|.env| [Configurações de conexão](.env)|
|.flaskenv| [Configurações Flask](.flaskenv)|
|database_functions| [Funções CRUD](database_functions.py)|
|requirements| [Libs necessárias](requirements.txt)|
|consultas| [Consultas(Querys)](consultas.txt)|


```
---------JSON inserir_ator--------
{
    "primeiro_nome":"felisberto"
    "sobrenome":"juas"
    "data_nasc":"yyyy-mm-dd" 
    "id_premio": 3 #caso possua
}
----------------------------------
--------JSON inserir_filmes-------
{
    "idioma_original"  : "hindi",
    "titulo"  :"viagem a tasmania",
    "subtitulo" :"muito doida",
    "sinopse" :"geral faz uma viagem mt doida a tasmania",
    "ano" :"1805-12-23",
    "duracao" : "2:50",
    "id_roteirista": "20",
    "id_diretor" : "35"
}

----------------------------------
----JSON inserir_relacionamento---

{
    "id_papel"  : 92,
    "id_ator"  : 73,
    "id_filme" : 80
}
```
## 🔍 Referências

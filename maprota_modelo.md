## /api/inserir_ator -- Rota para inserção de ator - POST 
```
{
    "primeiro_nome":"felisberto",
    "sobrenome":"juas",
    "data_nasc":"yyyy-mm-dd" ,
    "id_premio": 3 #caso possua
}
```
## /api/consultar_ator -- Rota para consulta de ator - GET
```
{
    "primeiro_nome":"teste",
    "sobrenome":"tste"
}
```
## /api/deletar_ator -- Rota para deletar ator - GET
```
{
    "primeiro_nome":"teste",
    "sobrenome":"tste"
}
```
## /api/atualizar_ator/<int:id_ator> -- Rota para atualizar ator - PUT
```
{# obrigatório informar ao menos 1
    "primeiro_nome":"felisberto",
    "sobrenome":"juas",
    "data_nasc":"yyyy-mm-dd" ,
    "id_premio": 3 #caso possua
}
```
## /api/inserir_Filme -- Rota para inserir filme - POST
```
{
        "titulo": "Int",
        "idioma_original": "Inglês",
        "subtitulo": "-",
        "sinopse": "As reservas naturais da Terra estão chegando ao fim e um grupo de astronautas recebe a missão de verificar possíveis planetas para receberem a população mundial, possibilitando a continuação da espécie.",
        "ano": "2014-11-06",
        "duracao": "2:49",
        "diretor": null,
        "roteirista": null
}
```
## /api/consultar_filme -- Rota para consultar filme - GET
```
{
        "titulo": "Interestelar"
}
```
## /api/deletar_filme -- Rota para deletar filme - GET
```
{
        "titulo": "Int",
        "subtitulo":"-"
}
```
## /api/atualizar_filme/<int:id_filme> -- Rota para atualizar filme - PUT
```
{# obrigatório informar ao menos 1
        "titulo": "Interestelar",
        "idioma_original": "Inglês",
        "subtitulo": "-",
        "sinopse": "As reservas naturais da Terra estão chegando ao fim e um grupo de astronautas recebe a missão de verificar possíveis planetas para receberem a população mundial, possibilitando a continuação da espécie.",
        "ano": "2014-11-06",
}
```

## /api/inserir_relacionamento -- Rota para inserir relacionamento - POST
```
{
    "id_papel":109,
    "id_ator":96,
    "id_filme": 103
}
```
## /api/consultar_relacionamento -- Rota para consultar relacionamento - GET
```
{
    "id_relacionamento":91
}
```
## /api/deletar_relacionamento -- Rota para deletar relacionamento - GET
```
{
    "id_relacionamento":91
}
```
## /api/atualizar_relacionamento/<int:id_relacionamento> -- Rota para atualizar relacionamento - PUT
```
{ # obrigatório informar ao menos 1
    "id_papel":109, 
    "id_ator":96, 
    "id_filme": 103
}
```
## /api/realizar_transacao -- Rota para realizar transacao - POST
```
{
    "filme": {
        "titulo": "teste",
        "idioma_original": "Inglês",
        "subtitulo": "Legendado",
        "sinopse": "Uma breve descrição do filme.",
        "ano": "2023-12-10",
        "duracao": "1:20",
        "diretor": 30,
        "roteirista": 25
    },
    "atores": [
        {
            "primeiro_nome": "Ator6",
            "sobrenome": "Sobrenome6",
            "data_nasc": "1990-01-01"
        },
        {
            "primeiro_nome": "Ator7",
            "sobrenome": "Sobrenome7",
            "data_nasc": "1995-02-15"
        }
    ],
    "papéis": {
        "Papel1": {
            "personagem": "Personagem6"
        },
        "Papel2": {
            "personagem": "Personagem7"
        }
    }
}
```

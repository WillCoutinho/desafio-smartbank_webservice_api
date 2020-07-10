# – FILE: features/posts.feature # language: pt

Funcionalidade: Manipular Posts
Como usuário
Quero fazer requisições à API do JSON PlaceHolder
Então assim posso manipular os posts existentes


  Cenário: Criar post
    Dado o endereço da API do JSON PlaceHolder para criar um post
     E os dados deste post
     Quando eu faço uma requisição POST com os dados do novo post
     Então a API do JSON PlaceHolder deve retornar os dados do post criados com o código "201"

  Cenário: Validar post criado
    Dado o endereço da API do JSON PlaceHolder para consultar um post
     E o id do post criado
     Quando eu faço uma requisição GET com o id do post
     Então a API do JSON PlaceHolder deve retornar os dados do post com o código "200"
     E os dados devem ser os mesmos do post criado anteriormente

  Cenário: Excluir post criado
    Dado o endereço da API do JSON PlaceHolder para excluir um post
     E o id do post criado
     Quando eu faço uma requisição DELETE com o id do post
     Então a API do JSON PlaceHolder deve retornar o código "200"


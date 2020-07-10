# – FILE: features/funcionario.feature # language: pt

Funcionalidade: Manipular cadastro de funcionário
Como usuário
Quero fazer requisições à API de funcionarios
Então assim posso manipular o cadastro dos mesmos


  Cenário: Criar cadastro do funcionário
    Dado o endereço da API para criar funcionário
     E os dados do funcionário
     Quando eu faço uma requisição POST com os dados do novo funcionário
     Então a API deve retornar os dados cadastrados com o código "201"

  Cenário: Validar cadastro do funcionário criado
    Dado o endereço da API para pegar um cadastro
     E os dados do funcionário criado anteriormente
     Quando eu faço uma requisição GET com o id do funcionário
     Então a API deve retornar os dados cadastrados com o código "200"
     E os dados devem ser os mesmos do funcionário criado

  Cenário: Excluir cadastro do funcionário criado
    Dado o endereço da API para excluir um cadastro
     E o id do funcionário criado
     Quando eu faço uma requisição DELETE com o id do funcionário
     Então a API deve retornar o código "200"


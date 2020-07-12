from behave import given, when, then
import features.src.funcionario_handler as handler


@given(u'o endereço da API para criar funcionário')
def url_api_post(context):
    assert handler.url_criar_funcionario() is not None, "Url para requisição POST inválida."


@given(u'os dados do funcionário')
def dados_funcionario(context):
    context.novo_funcionario = handler.dados_funcionario()
    assert context.novo_funcionario is not None, "Dados do funcionário inválidos."


@when(u'eu faço uma requisição POST com os dados do novo funcionário')
def requisicao_post(context):
    context.funcionario_criado = handler.criar_funcionario(context.novo_funcionario)
    assert context.funcionario_criado is not None, "Sem resposta para requisição POST"


@then(u'a API deve retornar o código "200" com os dados cadastrados')
def status_code_post(context):
    assert handler.validar_status_POST(context.funcionario_criado.status_code), "Status Code para requisição POST incorreto."
    assert handler.status_funcionario_criado(context.funcionario_criado), "Dados retornados não batem com os dados enviados."


@given(u'o endereço da API para pegar um cadastro')
def url_api_get(context):
    assert handler.url_get_funcionario() is not None, "Url para requisição GET inválida."


@given(u'os dados do funcionário criado anteriormente')
def dados_funcionario_anterior(context):
    context.funcionario_criado = handler.get_ultimo_funcionario_add()
    context.id = handler.funcionario_id(context.funcionario_criado)
    assert context.funcionario_criado is not None, "Dados do último funcionário criado inválido."


@when(u'eu faço uma requisição GET com o id do funcionário')
def requisicao_get(context):
    context.resposta = handler.get_funcionario(context.id)
    assert context.resposta is not None, "Sem resposta para requisição GET."


@then(u'a API deve retornar os dados cadastrados com o código "200"')
def status_code_get(context):
    assert handler.validar_status_GET(context.resposta.status_code), "Status Code para requisição GET incorreto."


@then(u'os dados devem ser os mesmos do funcionário criado')
def checar_dados_funcionario_retornado(context):
    assert handler.checar_dados(context.funcionario_criado,
                                context.resposta), "Dados do funcionário criado não batem com os dados retornados."


@given(u'o endereço da API para excluir um cadastro')
def url_api_delete(context):
    assert handler.url_deletar_funcionario() is not None, "Url para requisição DELETE inválida."


@given(u'o id do funcionário criado')
def id_funcionario_anterior(context):
    context.funcionario_criado = handler.get_ultimo_funcionario_add()
    context.id = handler.funcionario_id(context.funcionario_criado)
    assert context.funcionario_criado is not None, "Dados do último funcionário criado inválido."


@when(u'eu faço uma requisição DELETE com o id do funcionário')
def requisicao_delete(context):
    context.resposta = handler.deletar_funcionario(context.id)
    assert context.resposta is not None, "Sem resposta para requisição DELETE."


@then(u'a API deve retornar o código "200"')
def status_code_delete(context):
    assert handler.validar_status_DELETE(context.resposta), "Status Code para requisição DELETE incorreto."

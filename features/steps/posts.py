from behave import given, when, then
import features.src.posts_handler as handler


@given(u'o endereço da API do JSON PlaceHolder para criar um post')
def url_api_post(context):
    assert handler.url_get_post() is not None, "Url para requisição POST inválida."


@given(u'os dados deste post')
def dados_post(context):
    context.dados = handler.dados_post()
    assert context.dados is not None, "Dados do post inválidos."


@when(u'eu faço uma requisição POST com os dados do novo post')
def requisicao_post(context):
    context.resposta = handler.criar_post(context.dados)
    assert context.resposta is not None, "Sem resposta para requisição POST."


@then(u'a API do JSON PlaceHolder deve retornar os dados do post criados com o código "201"')
def status_code_post(context):
    assert handler.validar_status_POST(context.resposta), "Status Code para requisição POST incorreto."


@given(u'o endereço da API do JSON PlaceHolder para consultar um post')
def url_api_get(context):
    assert handler.url_get_post() is not None, "Url para requisição GET inválida."


@given(u'o id do post criado')
def dados_post_anterior(context):
    context.post_criado = handler.get_ultimo_post_add()
    context.id = context.post_criado['id']
    assert context.post_criado is not None, "Dados do último post criado inválido."


@when(u'eu faço uma requisição GET com o id do post')
def requisicao_get(context):
    context.resposta = handler.retornar_post_por_id(context.id)
    assert context.resposta is not None, "Sem resposta para requisição GET."


@then(u'a API do JSON PlaceHolder deve retornar os dados do post com o código "200"')
def status_code_get(context):
    assert handler.validar_status_GET(context.resposta.status_code), "Status Code para requisição GET incorreto."


@then(u'os dados devem ser os mesmos do post criado anteriormente')
def checar_dados_post_retornado(context):
    assert context.id == context.resposta.json()['id'], "ID do post criado não bate com o ID retornado."
    assert context.post_criado['title'] == context.resposta.json()['title'], "Title do post criado não bate com o Title retornado."


@given(u'o endereço da API do JSON PlaceHolder para excluir um post')
def url_api_delete(context):
    assert handler.url_deletar_post() is not None, "Url para requisição DELETE inválida."


@when(u'eu faço uma requisição DELETE com o id do post')
def requisicao_delete(context):
    context.post_criado = handler.get_ultimo_post_add()
    context.id = context.post_criado['id']
    context.resposta = handler.deletar_post(context.id)
    assert context.resposta is not None, "Sem resposta para requisição DELETE."


@then(u'a API do JSON PlaceHolder deve retornar o código "200"')
def status_code_delete(context):
    assert handler.validar_status_DELETE(context.resposta), "Status Code para requisição DELETE incorreto."

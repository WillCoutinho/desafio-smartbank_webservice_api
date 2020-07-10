from behave import given, when, then
import features.src.posts_handler as handler


@given(u'o endereço da API do JSON PlaceHolder para criar um post')
def step_impl(context):
    pass


@given(u'os dados deste post')
def step_impl(context):
    context.dados = handler.dados_post()
    assert context.dados is not None


@when(u'eu faço uma requisição POST com os dados do novo post')
def step_impl(context):
    context.resposta = handler.criar_post(context.dados)
    assert context.resposta is not None


@then(u'a API do JSON PlaceHolder deve retornar os dados do post criados com o código "201"')
def step_impl(context):
    assert handler.validar_status_POST(context.resposta)


@given(u'o endereço da API do JSON PlaceHolder para consultar um post')
def step_impl(context):
    pass


@given(u'o id do post criado')
def step_impl(context):
    context.post_criado = handler.get_ultimo_post_add()
    context.id = context.post_criado['id']
    assert context.post_criado is not None


@when(u'eu faço uma requisição GET com o id do post')
def step_impl(context):
    context.resposta = handler.retornar_post_por_id(context.id)
    assert context.resposta is not None


@then(u'a API do JSON PlaceHolder deve retornar os dados do post com o código "200"')
def step_impl(context):
    assert handler.validar_status_GET(context.resposta.status_code)


@then(u'os dados devem ser os mesmos do post criado anteriormente')
def step_impl(context):
    assert context.id == context.resposta.json()['id']
    assert context.post_criado['title'] == context.resposta.json()['title']


@given(u'o endereço da API do JSON PlaceHolder para excluir um post')
def step_impl(context):
    pass


@when(u'eu faço uma requisição DELETE com o id do post')
def step_impl(context):
    context.post_criado = handler.get_ultimo_post_add()
    context.id = context.post_criado['id']
    context.resposta = handler.deletar_post(context.id)
    assert context.resposta is not None


@then(u'a API do JSON PlaceHolder deve retornar o código "200"')
def step_impl(context):
    assert handler.validar_status_DELETE(context.resposta)

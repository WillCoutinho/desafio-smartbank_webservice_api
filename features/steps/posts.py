from behave import given, when, then
import features.src.posts_handler as handler

url = 'https://jsonplaceholder.typicode.com/posts/'


@given(u'o endereço da API do JSON PlaceHolder para criar um post')
def step_impl(context):
    context.url = url


@given(u'os dados deste post')
def step_impl(context):
    context.dados = handler.dados_post()
    assert context.dados is not None


@when(u'eu faço uma requisição POST com os dados do novo post')
def step_impl(context):
    context.resposta = handler.criar_post(url, context.dados)
    assert context.resposta is not None


@then(u'a API do JSON PlaceHolder deve retornar os dados do post criados com o código "201"')
def step_impl(context):
    assert handler.validar_status_POST(context.resposta)


@given(u'o endereço da API do JSON PlaceHolder para consultar um post')
def step_impl(context):
    context.url = url


@given(u'o id do post criado')
def step_impl(context):
    context.id = 99
    #  ID viria do Post criado anteriormente, mas a plataforma utilizada não realiza ações de POST/PUT/DELETE


@when(u'eu faço uma requisição GET com o id do post')
def step_impl(context):
    context.resposta = handler.retornar_post_por_id(url, context.id)
    assert context.resposta is not None


@then(u'a API do JSON PlaceHolder deve retornar os dados do post com o código "200"')
def step_impl(context):
    assert handler.validar_status_GET(context.resposta.status_code)


@then(u'os dados devem ser os mesmos do post criado anteriormente')
def step_impl(context):
    assert context.id == context.resposta.json()['id']


@given(u'o endereço da API do JSON PlaceHolder para excluir um post')
def step_impl(context):
    context.url = url


@when(u'eu faço uma requisição DELETE com o id do post')
def step_impl(context):
    context.resposta = handler.deletar_post(url, context.id)
    assert context.resposta is not None


@then(u'a API do JSON PlaceHolder deve retornar o código "200"')
def step_impl(context):
    assert handler.validar_status_DELETE(context.resposta)

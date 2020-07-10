from behave import given, when, then
import features.src.funcionario_handler as handler

url = 'http://dummy.restapiexample.com/api/v1/'


@given(u'o endereço da API para criar funcionário')
def step_impl(context):
    context.url = handler.url_criar_funcionario(url)


@given(u'os dados do funcionário')
def step_impl(context):
    context.novo_funcionario = handler.dados_funcionario()


@when(u'eu faço uma requisição POST com os dados do novo funcionário')
def step_impl(context):
    context.funcionario_criado = handler.criar_funcionario(context.url, context.novo_funcionario)


@then(u'a API deve retornar os dados cadastrados com o código "201"')
def step_impl(context):
    assert handler.validar_status_POST(context.funcionario_criado.status_code)
    assert handler.status_funcionario_criado(context.funcionario_criado)


@given(u'o endereço da API para pegar um cadastro')
def step_impl(context):
    context.url = url


@given(u'os dados do funcionário criado anteriormente')
def step_impl(context):
    context.id = handler.funcionario_id(context.funcionario_criado)


@when(u'eu faço uma requisição GET com o id do funcionário')
def step_impl(context):
    context.resposta = handler.get_funcionario(url, context.id)


@then(u'a API deve retornar os dados cadastrados com o código "200"')
def step_impl(context):
    assert handler.validar_status_GET(context.resposta.status_code)


@then(u'os dados devem ser os mesmos do funcionário criado')
def step_impl(context):
    assert handler.checar_dados(context.funcionario_criado, context.resposta)


@given(u'o endereço da API para excluir um cadastro')
def step_impl(context):
    context.url = url


@given(u'o id do funcionário criado')
def step_impl(context):
    context.id = handler.funcionario_id(context.funcionario_criado)


@when(u'eu faço uma requisição DELETE com o id do funcionário')
def step_impl(context):
    context.resposta = handler.deletar_funcionario(context.url, context.id)


@then(u'a API deve retornar o código "200"')
def step_impl(context):
    assert handler.validar_status_DELETE(context.resposta.status_code)

from behave import given, when, then
import features.src.funcionario_handler as handler


@given(u'o endereço da API para criar funcionário')
def step_impl(context):
    pass


@given(u'os dados do funcionário')
def step_impl(context):
    context.novo_funcionario = handler.dados_funcionario()
    assert context.novo_funcionario is not None


@when(u'eu faço uma requisição POST com os dados do novo funcionário')
def step_impl(context):
    context.funcionario_criado = handler.criar_funcionario(context.novo_funcionario)
    assert context.funcionario_criado is not None


@then(u'a API deve retornar o código "200" com os dados cadastrados')
def step_impl(context):
    assert handler.validar_status_POST(context.funcionario_criado.status_code)
    assert handler.status_funcionario_criado(context.funcionario_criado)


@given(u'o endereço da API para pegar um cadastro')
def step_impl(context):
    pass


@given(u'os dados do funcionário criado anteriormente')
def step_impl(context):
    context.funcionario_criado = handler.get_ultimo_funcionario_add()
    context.id = handler.funcionario_id(context.funcionario_criado)
    assert context.funcionario_criado is not None


@when(u'eu faço uma requisição GET com o id do funcionário')
def step_impl(context):
    context.resposta = handler.get_funcionario(context.id)
    assert context.resposta is not None


@then(u'a API deve retornar os dados cadastrados com o código "200"')
def step_impl(context):
    assert handler.validar_status_GET(context.resposta.status_code)


@then(u'os dados devem ser os mesmos do funcionário criado')
def step_impl(context):
    assert handler.checar_dados(context.funcionario_criado, context.resposta)


@given(u'o endereço da API para excluir um cadastro')
def step_impl(context):
    pass


@given(u'o id do funcionário criado')
def step_impl(context):
    context.funcionario_criado = handler.get_ultimo_funcionario_add()
    context.id = handler.funcionario_id(context.funcionario_criado)
    assert context.funcionario_criado is not None


@when(u'eu faço uma requisição DELETE com o id do funcionário')
def step_impl(context):
    context.resposta = handler.deletar_funcionario(context.id)
    assert context.resposta is not None


@then(u'a API deve retornar o código "200"')
def step_impl(context):
    assert handler.validar_status_DELETE(context.resposta)

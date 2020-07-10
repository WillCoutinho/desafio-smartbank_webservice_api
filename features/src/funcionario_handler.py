from faker import Faker
import requests

fake = Faker()
headers = {
    'Accept': '*/*',
    'User-Agent': 'request'
}


def criar_funcionario(url, dados):
    resposta = requests.post(url_criar_funcionario(url), data=dados, headers=headers)
    return resposta


def deletar_funcionario(url, id):
    resposta = requests.delete(url_deletar_funcionario(url, id), headers=headers)
    return resposta.status_code


def get_funcionario(url, id):
    resposta = requests.get(url_get_funcionario(url, id), headers=headers)
    return resposta


def checar_dados(funcionario_criado, resposta):
    if funcionario_criado.json()['data'] == resposta.json()['data']:
        return True
    else:
        return False


def status_funcionario_criado(funcionario_criado):
    funcionario = funcionario_criado.json()['data']
    
    if funcionario['id'] is not None:
        return True
    else:
        return False


def funcionario_id(funcionario_criado):
    funcionario = funcionario_criado.json()['data']  # ['data']['id']
    return funcionario['id']


def url_criar_funcionario(url):
    return url + 'create'


def url_get_funcionario(url, id):
    return url + str(id)


def url_deletar_funcionario(url, id):
    return url + str(id)


def validar_status_POST(status_retornado):
    if status_retornado == 201:
        return True
    else:
        return False


def validar_status_DELETE(status_retornado):
    if status_retornado == 200:
        return True
    else:
        return False


def validar_status_GET(status_retornado):
    if status_retornado == 200:
        return True
    else:
        return False


def retornar_funcionario_por_id(url, id):
    resposta = requests.get(url + str(id))
    return resposta.json()


def dados_funcionario():
    funcionario = {
        'name': fake.name(),
        'salary': fake.random_int(1000, 250000),
        'age': fake.random_int(18, 65)
    }
    return funcionario

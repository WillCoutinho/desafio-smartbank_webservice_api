from faker import Faker
import requests

fake = Faker()
headers = {
    'Accept': '*/*',
    'User-Agent': 'request'
}

url_get_by_id = 'http://dummy.restapiexample.com/api/v1/employee/'
url_get_list = 'http://dummy.restapiexample.com/api/v1/employees'
url_delete = 'http://dummy.restapiexample.com/api/v1/delete/'
url_post = 'http://dummy.restapiexample.com/api/v1/create'


def criar_funcionario(dados):
    try:
        resposta = requests.post(url_criar_funcionario(), data=dados, headers=headers)
        return resposta
    except Exception as e:
        print(e)
        return False


def deletar_funcionario(id):
    try:
        resposta = requests.delete(url_deletar_funcionario(id), headers=headers)
        return resposta.status_code
    except Exception as e:
        print(e)
        return False


def get_funcionario(id):
    try:
        resposta = requests.get(url_get_funcionario(id), headers=headers)
        return resposta
    except Exception as e:
        print(e)
        return False


def get_ultimo_funcionario_add():
    try:
        resposta = requests.get(url_get_list, headers=headers)
        ultimo_funcionario_add = resposta.json()['data']
        return ultimo_funcionario_add[-1]
    except Exception as e:
        print(e)
        return False


def checar_dados(funcionario_criado, resposta):
    try:
        if isinstance(funcionario_criado, dict):
            if funcionario_criado == resposta.json()['data']:
                return True
        
        else:
            if funcionario_criado.json()['data'] == resposta.json()['data']:
                return True
            else:
                return False
    except Exception as e:
        print(e)
        return False


def status_funcionario_criado(funcionario_criado):
    try:
        funcionario = funcionario_criado.json()['data']
        if funcionario['id'] is not None:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def funcionario_id(funcionario_criado):
    try:
        if isinstance(funcionario_criado, dict):
            return funcionario_criado['id']
        
        else:
            if funcionario_criado.json() is not None:
                funcionario = funcionario_criado.json()['data']
                return funcionario['id']
            else:
                return None
    except Exception as e:
        print(e)
        return False


def url_criar_funcionario():
    return url_post


def url_get_funcionario(id='1'):
    return url_get_by_id + str(id)


def url_deletar_funcionario(id='1'):
    return url_delete + str(id)


def validar_status_POST(status_retornado):
    try:
        if status_retornado == 200:
            return True
        else:
            return False
    
    except Exception as e:
        print(e)
        return False


def validar_status_DELETE(status_retornado):
    try:
        if status_retornado == 200:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def validar_status_GET(status_retornado):
    try:
        if status_retornado == 200:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def dados_funcionario():
    # funcionario = {
    #     'name': fake.name(),
    #     'salary': fake.random_int(1000, 250000),
    #     'age': fake.random_int(18, 65)
    # }
    funcionario = {
        "name": "Tester ABC",
        "salary": "0000",
        "age": "20",
    }
    return funcionario

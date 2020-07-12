from faker import Faker
import requests

fake = Faker()
headers = {
    'Accept': '*/*',
    'User-Agent': 'request'
}

url = 'https://jsonplaceholder.typicode.com/posts/'


def criar_post(dados):
    try:
        resposta = requests.post(url_criar_post(), data=dados, headers=headers)
        return resposta.status_code
    except Exception as e:
        print(e)


def deletar_post(id):
    try:
        resposta = requests.delete(url_deletar_post(id), headers=headers)
        return resposta.status_code
    except Exception as e:
        print(e)
        return False


def validar_status_POST(status):
    try:
        if status == 201:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def validar_status_DELETE(status):
    try:
        if status == 200:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def validar_status_GET(status):
    try:
        if status == 200:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def retornar_post_por_id(id):
    try:
        resposta = requests.get(url_get_post(id), headers=headers)
        return resposta
    except Exception as e:
        print(e)
        return False


def get_ultimo_post_add():
    try:
        resposta = requests.get(url, headers=headers)
        ultimo_funcionario_add = resposta.json()
        return ultimo_funcionario_add[-1]
    except Exception as e:
        print(e)
        return False


def post_id(post_criado):
    try:
        if isinstance(post_criado, dict):
            return post_criado['id']
        
        else:
            if post_criado.json() is not None:
                post = post_criado.json()['id']
                return post['id']
            else:
                return None
    except Exception as e:
        print(e)
        return False


def url_criar_post():
    return url


def url_get_post(id='1'):
    return url + str(id)


def url_deletar_post(id='1'):
    return url + str(id)


def dados_post():
    post = {
        "title": fake.ascii_email(),
        "body": fake.text(),
        "userId": fake.random_int(0, 100)
    }
    return post

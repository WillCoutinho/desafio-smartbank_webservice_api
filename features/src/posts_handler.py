from faker import Faker
import requests

fake = Faker()
headers = {
    'Accept': '*/*',
    'User-Agent': 'request'
}


def criar_post(url, dados):
    resposta = requests.post(url, data=dados, headers=headers)
    return resposta.status_code


def deletar_post(url, id):
    resposta = requests.delete(url + str(id), headers=headers)
    return resposta.status_code


def validar_status_POST(atual):
    if atual == 201:
        return True
    else:
        return False


def validar_status_DELETE(atual):
    if atual == 200:
        return True
    else:
        return False


def validar_status_GET(atual):
    if atual == 200:
        return True
    else:
        return False


def retornar_post_por_id(url, id):
    resposta = requests.get(url + str(id))
    return resposta


def dados_post():
    post = {
        "title": fake.ascii_email(),
        "body": fake.text(),
        "userId": fake.random_int(0, 100)
    }
    return post

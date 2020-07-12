## Desafio 1 - API
Passo a passo para instalar, configurar e rodar os testes de API.\
Cenários feitos para as APIs [Dummy RestAPI Examples](http://dummy.restapiexample.com/) e [JSON Place Holder](https://jsonplaceholder.typicode.com/posts/)

>**_Nota_**: API [Dummy RestAPI Examples](http://dummy.restapiexample.com/) se mostrou instável durante os testes (fora do ar ou não \
retornando as requisições) e, por esse motivo, criei cenários também para API [JSON Place Holder](https://jsonplaceholder.typicode.com/posts/)

##
### Pré Requisitos - Windows 10

Instale a versão 3.8.3 (executable) do [*Python*](https://www.python.org/downloads/release/python-383/)
>**_Nota_**: Antes de instalar, selecione a opção 'Add Python 3.8 to PATH'

Instale o [*GIT*](https://git-scm.com/download/win) para clonar o repositório

Baixe o framework de report [*Allure (2.13.5)*](https://github.com/allure-framework/allure2/releases) e descompacte na pasta que desejar.
 - Abra o terminal _Powershell_: ``Menu Iniciar > digite _'Powershell'``
 - Configure o ``PATH`` do _Allure Framework_ com o comando: 
````bash
$env:PATH += ';\Caminho_Pasta_Allure\allure-2.13.5\bin'
````

Instale o [*Java JDK*](https://www.java.com/pt_BR/download/) e abra as opções: ``Menu Iniciar > Digite 'Ambiente' > 
'Editar Variáveis de Ambiente' > Variáveis de Ambiente``

- Crie uma nova variável de usuário ``JAVA_HOME`` e como valor o caminho onde o Java foi instalado
- Crie uma nova variável de sistema em _Path_, adicionando a expressão ``%JAVA_HOME%\bin``
- Reinicie a máquina para que as mudanças tenham efeito.

##
### Pré Requisitos - Linux (Ubuntu)
Instale a versão 3.8.3 (executable) do *Python*: ``sudo apt-get install python3.8``

Instale o *Python pip*: ``sudo apt install python3-pip``

Instale o *GIT*: ``sudo apt install git``

Baixe o framework de report [*Allure (2.13.5)*](https://github.com/allure-framework/allure2/releases) e descompacte na pasta que desejar.\
Abra o terminal e insira o caminho da pasta ``bin`` do _Allure Framework_ no ``PATH`` environment: 
````bash 
export PATH=$PATH:~/Caminho_Allure/bin
source ~/.bashrc
````

Instale o [*Java JDK*](https://www.java.com/pt_BR/download/) e crie as variáveis de ambiente ``JAVA_HOME`` e como valor o caminho onde JAVA está instalado.\
Insira também a pasta ``\bin`` no Path environment.
> _*Nota*_: Em caso de dúvidas utilize o [guia da Oracle](https://www.java.com/pt_BR/download/help/path.xml)  


Pronto, já será possível checar a versão do _Allure_ (``allure --version``) para confirmar se o ``PATH`` foi 
configurado corretamente.

##
### Git Clone e Instalação das Libs

Crie uma pasta com o nome e no diretório que quiser (para clonar o repositório).\
Clone o repositório do [Desafio 1 - API](https://gitlab.com/Coutinho_W/desafio-smartbank_webservice_api) e entre na pasta clonada.

Instale a lib ``pipenv`` com o comando: ``pip install pipenv``\
E instale as dependências pelo ``Pipfile`` (que está no diretório raiz clonado) com o comando: ``pipenv install``\
Aguarde as dependências serem instaladas. Após o processo use o comando ``pipenv shell`` para rodar uma VirtualEnv.

Para rodar os testes vamos usar o comando abaixo. 
Os parâmetros deste comando são:\
``--lang=pt``: língua utilizada nos arquivos ``.feature``\
``-f allure_behave.formatter:AllureFormatter``: formato que vamos utilizar na saída (_Allure Framework_)\
``-o allure_result_folder``: pasta onde será salva a saída do teste\
``./features``: features que serão executadas
       
````bash
behave --lang=pt -f allure_behave.formatter:AllureFormatter -o allure_result_folder ./features
````
 
Após os testes rodarem, usamos o comando abaixo para gerar o relatório.
O comando criará um servidor local que vai ler os arquivos em ``allure_result_folder`` e lançará os resultados no browser:
````bash
allure serve allure_result_folder
````

Pronto, relatório dos testes de API disponíveis no browser.
##
#### Repositório Git

GitLab: [*Desafio 1 - API (Smartbank)*](https://gitlab.com/Coutinho_W/desafio-smartbank_webservice_api) 

##
#### Libs utilizadas

* [Behave](https://pypi.org/project/behave/#description) - BDD com suporte ao Python
* [Allure-Behave](https://pypi.org/project/allure-behave/#description) - Framework para gerar reports
* [Faker](https://pypi.org/project/Faker/#description) - Gerador de dados
* [Pipenv](https://pypi.org/project/pipenv/#description) - Package/VirtualEnv manager 
* [Requests](https://pypi.org/project/requests/#description) - HTTP library


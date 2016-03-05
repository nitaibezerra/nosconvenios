NosConvenios - Aplicativo que baixa todos os convênios em json e salva na pasta data. Os dados são baixados da API do Siconv disponível em http://api.convenios.gov.br/

Projeto iniciado no Open Data Day BSB 2016.

# Instalação

1. Clonar o repositório

`git clone https://github.com/nitaibezerra/nosconvenios.git`

2. Criar e ativar o ambiente virtual

```
cd nosconvenios
virtualenv --no-site-packages pyenv
source pyenv/bin/activate
```

3. Instalar dependências

`pip install -r requirements.txt`

4. Para executar o script e baixar os dados dos convênios

`python download-dados.py`

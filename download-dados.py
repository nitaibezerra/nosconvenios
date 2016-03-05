# -*- coding: utf-8 -*-
import requests
import json
import os
import urlparse

url_pagina = 'http://api.convenios.gov.br/siconv/v1/consulta/convenios.json'

while True:
    pagina = requests.get(url_pagina)
    json_pagina = json.loads(pagina.content)
    urls = [convenio["href"] for convenio in json_pagina["convenios"]]

    if not os.path.exists('dados'):
        print u'Criando diretório de dados'
        os.mkdir('dados')

    for url in urls:
        convenio = requests.get(url, headers={'accept': 'application/json'})
        if convenio.ok:
            filename = os.path.basename(urlparse.urlparse(url).path)
            with open('dados/convenio-id-%s.json' % filename, 'w') as f:
                print u'Gravando arquivo do convênio de id: %s' % filename
                f.write(convenio.content)
        else:
            print 'ERRO ao gravar arquivo do convênio de id: %s' % filename

    #Baixando próxima página de convênios. Cada página contém 500 convênios
    url_pagina = json_pagina["metadados"]["proximos"]

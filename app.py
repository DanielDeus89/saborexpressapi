import json
import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

try:
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        dados_restaurante = {}
        for item in dados_json:
            nome_do_restaurante = item['Company']
            if nome_do_restaurante not in dados_restaurante:
                dados_restaurante[nome_do_restaurante] = []

            dados_restaurante[nome_do_restaurante].append({
                "item": item['Item'],
                "price": item['price'],
                "description": item['description']
            })

    for nome_do_restaurante,dados  in dados_restaurante.items():
        nome_do_arquivo = f'{nome_do_restaurante}.json'
        with open(nome_do_arquivo, 'w', encoding='utf-8') as arquivo_restaurante:
            json.dump(dados, arquivo_restaurante, indent=4, ensure_ascii=False)
        print(f"Arquivo {nome_do_arquivo} salvo com sucesso!")

    else:
        print(f"Erro na requisição. Código de status: {response.status_code}")


except requests.RequestException as e:
    print(f"Erro ao acessar a API: {e}")

except Exception as e:
    print(f"Erro inesperado: {e}")



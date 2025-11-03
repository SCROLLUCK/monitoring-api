# Sistema de Monitoramento Ambiental com FastAPI

Este sistema foi desenvolvido para monitorar a qualidade do ar em diferentes locais. Ele utiliza o framework FastAPI para criar uma API RESTful que permite a publicação de dados sobre a qualidade do ar e a consulta desses dados.

O sistema é composto por dois principais componentes:

1. Uma API RESTful desenvolvida com FastAPI que permite a publicação de dados sobre a qualidade do ar e a consulta desses dados.
2. Um banco de dados relacional que armazena os dados sobre a qualidade do ar.

A API RESTful é composta por dois endpoints:

1. `POST /monitoring`: Este endpoint permite a publicação de dados sobre a qualidade do ar. Ele recebe os dados sobre a temperatura, umidade de humidade e o local onde foi realizada a medição.
2. `GET /monitoring`: Este endpoint permite a consulta dos dados sobre a qualidade do ar. Ele retorna uma lista com todos os dados sobre a qualidade do ar armazenados no banco de dados.

O banco de dados relacional é responsável por armazenar os dados sobre a qualidade do ar. Ele é composto por uma tabela que contém as seguintes colunas:

- `id`: Identificador único da medição.
- `timestamp`: Data e hora em que a medição foi realizada.
- `temperature`: Temperatura medida em graus Celsius.
- `humidity`: Umidade de humidade medida em porcento.

Este sistema foi desenvolvido para ser escalável e flexível, permitindo a adição de novos endpoints e a integração com outros sistemas.

## Tecnologias Utilizadas

- FastAPI: Framework para criar APIs RESTful em Python.
- Tortoise: ORM para criar e manipular o banco de dados relacional.
- PostgreSQL: Banco de dados relacional utilizado para armazenar os dados sobre a qualidade do ar.

## Como Executar o Sistema

1. Clone o repositório para uma pasta local.
2. Instale as dependências necessárias com o comando `pip install -r requirements.txt`.
3. Execute o comando `docker-compose up` para criar e iniciar o banco de dados.
4. Execute o comando `uvicorn main:app --host 0.0.0.0 --port 8000` para executar a API.
5. Acesse a API com o comando `curl -X POST http://localhost:8000/monitoring -H "Content-Type: application/json" -d '{"timestamp": "2022-01-01T12:00:00", "temperature": 20.0, "humidity": 60.0, "location": "Sala"}'`.
6. Acesse a API com o comando `curl -X GET http://localhost:8000/monitoring` para consultar os dados sobre a qualidade do ar.

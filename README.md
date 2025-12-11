# Web Store

Projeto de loja virtual utilizando Django (backend) e React (frontend).

## Estrutura

- **backend/**: API REST com Django, JWT, CORS, e suporte a imagens.
- **frontend/**: Interface web com React.

## Requisitos

- Instalar dependências do backend:
  ```bash
    cd backend
  pip install -r requirements.txt
  ```
- Instalar dependências do frontend:
  ```bash
  cd frontend
  npm install
  ```

## Como rodar

### Backend (Django)

    ```bash
    cd backend
    python manage.py runserver
    ```

### Frontend (React)

    ```bash
    cd frontend
    npm start
    ```

## Funcionalidades

- Cadastro e autenticação de usuários (JWT)
- Listagem de produtos
- Carrinho de compras
- Integração entre frontend e backend via API REST

## Licença

MIT

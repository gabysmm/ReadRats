## Dominio - ReadRats

### Visão Geral
Modelagem do dominio do projeto para definição de arquitetura 

### Entidades existentes

- User
- Comunidade
- Desafio
- Post
- Comentário 
- Score
- Membro da comunidade

### Especificando as entidades

#### User
- id
- username
- email
- foto
- bio

Relacionamentos:

- segue outros usuários
- participa de comunidades
- cria posts 
- comenta posts

#### Comunidade
- id 
- nome
- descricao
- tipo (temporaria/continua)
- criador_id
- data_criacao

relacionamentos:
- tem muitos membros
- tem desafios
- tem no minimo 1 desafio ativo 

#### Desafio
- id
- comunidade_id
- tipo_pontuacao
- ativo (boolean)
- data_inicio
- data_fim

relaciomanetos:
- pertence a uma comunidade
- recebe posts
- gera ranking

#### Post
- id
- user_id
- desafio_id
- paginas_lidas
- capitulos_lidos
- descricao
- foto
- pontos_Gerados
- data_criacao

relacionamentos:
- recebe comentários
- realizado por um usuário/membro da comunidade
- gera pontos

#### Comentários
- id 
- user_id
- post_id
- texto
- data_Criacao

relacionamentos:
- realizado em um post
- realizado por um user

### Score
- id
- desafio_id
- user_id
- pontuacao_total

relacionamentos:
- pertence a Desafio
- pertence a USer

#### Membro da comunidade (Entidade associativa)
- id 
- user_id
- papel (admin/membro normal)
- data_entrada

relacionamentos:
- pertence a user
- pertence a comunidade

### Diagrama de dominio

```mermaid
erDiagram

    USER {
        int id PK
        string username
        string email
        string foto
        string bio
    }

    COMUNIDADE {
        int id PK
        string nome
        string descricao
        string tipo
        int criador_id FK
        datetime data_criacao
    }

    MEMBERSHIP {
        int id PK
        int user_id FK
        int comunidade_id FK
        string papel
        datetime data_entrada
    }

    DESAFIO {
        int id PK
        int comunidade_id FK
        string tipo_pontuacao
        boolean ativo
        datetime data_inicio
        datetime data_fim
    }

    POST {
        int id PK
        int user_id FK
        int desafio_id FK
        int paginas_lidas
        int capitulos_lidos
        string descricao
        string foto
        int pontos_gerados
        datetime data_criacao
    }

    COMENTARIO {
        int id PK
        int user_id FK
        int post_id FK
        string texto
        datetime data_criacao
    }

    SCORE {
        int id PK
        int user_id FK
        int desafio_id FK
        int pontuacao_total
    }

    USER ||--o{ MEMBERSHIP : participa
    COMUNIDADE ||--o{ MEMBERSHIP : possui

    COMUNIDADE ||--o{ DESAFIO : possui

    USER ||--o{ POST : cria
    DESAFIO ||--o{ POST : recebe

    POST ||--o{ COMENTARIO : possui
    USER ||--o{ COMENTARIO : escreve

    USER ||--o{ SCORE : acumula
    DESAFIO ||--o{ SCORE : gera
```



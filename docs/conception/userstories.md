## Histórias de Usuário - ReadRats

## Visão Geral
Documento responsavél por amazenar requisitos em formas de história de usuário com usuários, organizados e numerados de acordo com sua prioridade no projeto. 

---
## Epico 1 - Comunidades e Desafios

### 01 - Criar Comunidade <br>
**Como** leitora <br>
**Quero** criar uma comunidade de leitura  <br>
**Para** participar de desafios ou metas em grupo

Critérios de aceitação:
- Usuário consegue criar uma comunidade informando nome e descrição
- Comunidade criada fica visível para a criadora
- Criadora é automaticamente adicionada como admin
- Comunidade inicia sem desafios ativos, com ranking padrão

Exemplo de uso: <br>
Maria cria a comunidade "Leitura 2026", adiciona uma descrição e passa a visualizar a comunidade no seu painel, podendo criar desafios dentro dela, visualizar ranking da comunidade, progresso individual e publicar progresso de leituras.

### 02 - Definir tipo de comunidade <br>
**Como** leitora <br>
**Quero** definir se a comunidade será temporária ou contínua <br>
**Para** escolher se ela servirá para um único desafio ou vários

Critérios de aceitação:
- No momento da criação, é possível escolher entre comunidade temporária ou contínua
- Comunidades temporárias permitem apenas um desafio ativo
- Comunidades contínuas permitem múltiplos desafios ao longo do tempo, ou apenas visualização padrão de dias lidos e ranking padrão
- O tipo da comunidade fica visível para todos os membros

Exemplo de uso<br>
Ao criar a comunidade “Maratona Principe Cruel, a usuária seleciona o tipo temporário e cria um único desafio para ler o livros em 30 dias.

#### 03 - Definir metas e desafios <br>
**Como** leitora <br>
**Quero** definir uma meta ou desafio dentro da comunidade <br>
**Para** motivar os participantes a lerem mais juntos. 

Critérios:
- Toda comunidade possui um desafio padrão inicial
- Ao criar um novo desafio, o desafio anterior é encerrado
- O ranking e a pontuação são reiniciados ao criar um novo desafio
- O desafio ativo fica visível para todos os membros

Exemplo de uso: <br>
Em uma comunidade contínua, a administradora encerra o desafio de "Páginas em janeiro" e cria um novo desafio chamado "Livros em feveiro", reiniciando o ranking.

#### 04 - Definir regras e pontuação do desafio<br>
**Como** leitora <br>
**Quero** definir como a pontuação do desafio funciona <br>
**Para** que todos saibam como serão ranqueados e o rank haja de acordo. 

Critérios de aceitação:
- Criadora do desafio escolhe o tipo de pontuação
- Tipos disponíveis:
    - páginas lidas
    - capítulos lidos
    - dias consecutivos lendo
    - livros finalizados
- O tipo de pontuação não pode ser alterado após o início do desafio
- A regra escolhida fica visível para todos os membros

Exemplo de uso: <br>
A admin cria um desafio baseado em páginas lidas, deixando a escolha dos livros livre e todos os participantes passam a pontuar conforme registram páginas no sistema. 


#### 05 - Visualizar ranking do desafio <br>
**Como** leitora <br>
**Quero** visualizar o ranking do desafio<br>
**Para** acompanhar meu desempenho em relação ao grupo

Critérios de aceitação:
- Rankking exibe os participantes ordenados pela pontuação
- A pontuação de usuária logada é destacada
- Ranking atualiza automaticamente conforme registros de leitura
- Ranking é acessível apenas para membros da comunidade
- Ranking é ordenada de acordo com o sistema de pontuação escolhido

Exemplo de uso: <br>
Após registrar sua leitura diária, a usuária vê sua posição subir no ranking da comunidade

#### 06 - Visualizar progresso individual e da comunidade <br>
**Como** leitora <br>
**Quero** visualizar o meu progresso e o da comunidade<br>
**Para** acompanhar evolução coletiva e individual

Critérios de aceitação:
- Usuária visualiza seu progresso pessoal no desafio 
- Usuária visualiza progresso total da comunidade
- PRogresso é apresentado de forma visual (ex: barra, porcentagem)

Exemplo de uso:
A usuária vê que já leu 60% da meta enquanto a comunidade alcançou 45%

### Epico 2 - Registro e Compartilhamento de leitura

#### 04 - Publicar progresso de leitura <br>
**Como** leitora <br>
**Quero** publicar minha leitura com foto, páginas ou capítulos e descrição <br>
**Para** compartilhar minha rotina de leitura e pontuar nos desafios

Critérios de aceitação:
- Publicação permite foto de comprovação, texto e progresso
- Progresso registrado impacta a pontuação do desafio ativo (em caso de leitura livre, com pontuação determinada pelo check in, progresso de leitura rápido também impacta mesmo que mínimo)
- Publicação aparece no feed da comunidade
- Publicação não pode existir sem progresso registrado

Exemplo de uso: <br>
A usuária posta uma foto do livro, informa 25 páginas lidas e automaticamente soma pontos no ranking

#### 05 - Comentar publicação <br>
**Como** leitora <br>
**Quero** comentar publicações de outras pessoas <br>
**Para** interagir e trocar experiências sobre os livros com o grupo

Critérios de aceitação:
- Usuário consegue escrever e enviar comentários
- Comentários ficam visiveis em baixo da publicação para membros da comunidade
- Comentários ficam associados à publicação.
- Comentário vísivel com nome, foto e horário de quem comentou

Exemplo de uso
Uma usuária comenta "Também estou amando esse livro" na publicação de outra leitora.

--- 

## Acesso a plataforma e Perfis
#### 06 - Cadastrar <br>
**Como** leitora <br>
**Quero** criar uma conta no ReadRats  <br>
**Para** registrar minhas leituras e acompanhar meu progresso em uma equipe

Critérios de aceitação:
- Usuário cria conta com dados básicos
- Conta criada permite acesso imediato
- Senhas devem seguir padrão de segurança de até 8 caracteres, pelo menos uma letra maiuscula, uma minuscula, um caractere especial e um número.

#### 07 - Login <br>
**Como** leitora <br>
**Quero** acessar minha conta  <br>
**Para** visualizar minha equipe, leituras e metas

Critério de aceitação:
- Login Válido permite acesso
- Login inválido exibe erro

#### 08 - Seguir amigos <br>
**Como** leitora <br>
**Quero** seguir ou adicionar amigos  <br>
**Para** acomapnhar o que eles estão lendo, encontrar comunidades e desafios em comum.

Critérios de aceitação:
- Um usuário quando segue ou adiciona como amigo outro usuário, passa a ver comunidades em comum 
- Usuário vê postagens e check in do perfil que segue

### 09 - Personalizar perfil <br>
**Como** leitora <br>
**Quero** mudar meu nome, email, senha, foto de perfil e descrição  <br>
**Para** modificar o perfil de acordo com seus gostos pessoais





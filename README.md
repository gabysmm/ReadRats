# ReadRats
Projeto Pessoal: Uma espécie de gymrats só que para leitores e clubes do livro, para da feedbacks e marcar progresso dos livros do mês.

## Executando com HTTPS

O projeto possui suporte a HTTPS utilizando um certificado SSL para ambiente de desenvolvimento.

### Iniciar o servidor HTTPS

```bash
python manage.py runserver_plus --cert-file certs/cert.pem
```

Após iniciar, a aplicação estará disponível em:

```text
https://127.0.0.1:8000
```

### Testando no GitHub Codespaces

Como o certificado utilizado é autoassinado, o proxy do Codespaces pode não encaminhar corretamente a conexão HTTPS para o navegador.

Para validar que o HTTPS está funcionando dentro do ambiente, execute:

```bash
curl -k https://127.0.0.1:8000
```

O parâmetro `-k` permite aceitar certificados autoassinados.

A resposta da aplicação confirma que o servidor está respondendo através de HTTPS.
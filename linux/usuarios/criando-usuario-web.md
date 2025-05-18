# Configurando páginas web pessoais automáticas com Nginx e skel no Linux

Este guia descreve como configurar um diretório `skel` no Linux para criar automaticamente uma página web pessoal para novos usuários, servida pelo Nginx.

## Passos

1. **Criar o diretório skel e a estrutura da página web:**

    ```bash
    sudo mkdir -p /etc/skel/public_html
    ```


2. **Criar um arquivo index.html básico:**

    ```bash
    sudo nano /etc/skel/public_html/index.html
    ```

    Cole o seguinte conteúdo HTML:

    ```html
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Página Pessoal de ~usuário</title>
    </head>
    <body>
        <h1>Bem-vindo à página de ~usuário!</h1>
        <p>Esta é a página web padrão.</p>
    </body>
    </html>
    ```


3. **Configurar as permissões:**

    ```bash
    sudo chown root:root /etc/skel/public_html
    sudo chmod 0755 /etc/skel/public_html
    sudo chmod 0644 /etc/skel/public_html/index.html
    ```


4. **Criar um template de configuração do Nginx:**
    ```bash
    sudo nano /etc/nginx/templates/user.conf.template
    ```

5. **Cole o seguinte conteúdo, substituindo `www-data` pelo usuário e grupo do seu Nginx, se necessário:**

  ```bash
  server {
      listen 80;
      listen [::]:80;

      server_name ~^(\w+)\.example\.com$; # Substitua example.com pelo seu domínio

      root /home/$1/public_html;
      index index.html;

      location / {
          try_files $uri $uri/ =404;
      }
  }
  ```

    **Nota:** O `server_name` usa uma expressão regular para capturar o subdomínio. O `$1` representa o nome do usuário.



6. **Criar um script para configurar o novo usuário no Nginx (recomendado):**

Crie um script que será executado após a criação de um novo usuário. Este script copiará o template de configuração e o adaptará para o novo usuário.
  ```bash
  sudo nano /usr/local/bin/setup-user-web
  ```

Cole o seguinte conteúdo, adaptando conforme necessário:

```bash
#!/bin/bash

USERNAME=$1

if [ -z "$USERNAME" ]; then
    echo "Uso: $0 <nome_de_usuario>"
    exit 1
fi

mkdir -p /home/$USERNAME/public_html
chown $USERNAME:$USERNAME /home/$USERNAME/public_html
chmod 0755 /home/$USERNAME/public_html

sed "s/~usuário/$USERNAME/g" /etc/skel/public_html/index.html > /home/$USERNAME/public_html/index.html
chown $USERNAME:$USERNAME /home/$USERNAME/public_html/index.html

cp /etc/nginx/templates/user.conf.template /etc/nginx/sites-available/$USERNAME.conf
sed -i "s/$1/$USERNAME/g" /etc/nginx/sites-available/$USERNAME.conf

ln -s /etc/nginx/sites-available/$USERNAME.conf /etc/nginx/sites-enabled/

systemctl reload nginx
```

7. **Exemplo de script aprimorado com tratamento de erros:**

```bash
#!/bin/bash

USERNAME=$1

if [ -z "$USERNAME" ]; then
    echo "Erro: Nome de usuário não fornecido." >&2
    exit 1
fi

mkdir -p /home/$USERNAME/public_html || { echo "Erro ao criar o diretório public_html." >&2; exit 1; }
chown $USERNAME:$USERNAME /home/$USERNAME/public_html || { echo "Erro ao definir o proprietário do diretório public_html." >&2; exit 1; }
chmod 0755 /home/$USERNAME/public_html || { echo "Erro ao definir as permissões do diretório public_html." >&2; exit 1; }

sed "s/~usuário/$USERNAME/g" /etc/skel/public_html/index.html > /home/$USERNAME/public_html/index.html || { echo "Erro ao criar o index.html." >&2; exit 1; }
chown $USERNAME:$USERNAME /home/$USERNAME/public_html/index.html || { echo "Erro ao definir o proprietário do index.html." >&2; exit 1; }


if ! cp /etc/nginx/templates/user.conf.template /etc/nginx/sites-available/$USERNAME.conf; then
  echo "Erro ao copiar o template de configuração." >&2
  exit 1
fi

sed -i "s/\$1/$USERNAME/g" /etc/nginx/sites-available/$USERNAME.conf || { echo "Erro ao substituir o placeholder no arquivo de configuração." >&2; exit 1; }

ln -s /etc/nginx/sites-available/$USERNAME.conf /etc/nginx/sites-enabled/ || { echo "Erro ao criar o link simbólico." >&2; exit 1; }

systemctl reload nginx || { echo "Erro ao recarregar o Nginx." >&2; exit 1; }
echo "Configuração concluída para o usuário $USERNAME."
```
**Nota:** O script acima verifica se o nome de usuário foi fornecido e se as operações foram bem-sucedidas. Se algo falhar, ele exibirá uma mensagem de erro apropriada.
**Permissões do script:**
```bash
sudo chown root:root /usr/local/bin/setup-user-web
```


Torne o script executável:
```bash
sudo chmod +x /usr/local/bin/setup-user-web
```

7. **Integrar o script com a criação de usuários:**

Adicione a seguinte linha ao final do arquivo `/etc/adduser.local`:
```bash	
/usr/local/bin/setup-user-web "$USERNAME"
```

8. **Testar:**
Crie um novo usuário teste: 
```bash
sudo adduser teste
```
Isso criará o diretório `/home/teste/public_html` e copiará o arquivo `index.html` para lá.
O Nginx também criará um arquivo de configuração em `/etc/nginx/sites-available/teste.conf` e criará um link simbólico em `/etc/nginx/sites-enabled/teste.conf`.
9. **Recarregar o Nginx:**
```bash
sudo systemctl reload nginx
``` 
10. **Testar a configuração:**
Acesse `http://teste.example.com` no seu navegador (substitua `teste` e `example.com` pelos valores corretos).
```bash
sudo nginx -t
```
Isso verificará a configuração do Nginx. Se tudo estiver correto, você verá uma mensagem de sucesso.


11. **Remover o usuário:**
Para remover o usuário e sua página web, use o seguinte comando:
```bash
sudo deluser --remove-home teste
``` 
Isso removerá o diretório do usuário e a configuração do Nginx.
```bash
sudo rm /etc/nginx/sites-available/teste.conf
sudo rm /etc/nginx/sites-enabled/teste.conf
``` 
```bash
sudo systemctl reload nginx
```
Isso removerá o link simbólico e recarregará o Nginx.
12. **Verificar o status do Nginx:**
```bash
sudo systemctl status nginx
```
Isso mostrará o status do Nginx e se há algum erro na configuração.
13. **Verificar os logs do Nginx:**
```bash 
sudo tail -f /var/log/nginx/error.log
```
Isso mostrará os logs de erro do Nginx em tempo real. Você pode verificar se há erros ao acessar a página web.



# Considerações importantes

Segurança: Verifique as permissões de arquivo.

Domínio: Substitua example.com pelo seu domínio. Configure o DNS corretamente.

Usuário e Grupo do Nginx: Utilize os valores corretos.

Firewall: Abra a porta 80 (ou 443 para HTTPS).

Complexidade: Para cenários complexos, use ferramentas como Puppet, Chef ou Ansible.

# Conclusão
Com esses passos, você terá configurado um diretório `skel` no Linux para criar automaticamente uma página web pessoal para novos usuários, servida pelo Nginx. Isso facilita a criação de páginas web pessoais para cada novo usuário criado no sistema.
# Referências
- [Nginx Documentation](https://nginx.org/en/docs/)
- [Linux adduser Command](https://linux)
- [Linux skel Directory](https://linux)
- [Nginx Configuration](https://nginx.org/en/docs/beginners_guide.html)
- [Nginx Server Blocks](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-ubuntu-20-04)
- [Nginx Templates](https://www.nginx.com/resources/wiki/start/topics/examples/server_blocks/)
- [Nginx Error Logs](https://www.nginx.com/resources/wiki/start/topics/tutorials/logging/)
- [Nginx Security](https://www.nginx.com/resources/wiki/start/topics/tutorials/security/)
- [Linux Permissions](https://linux)
- [Linux File Permissions](https://linux)

### Quando a execução do `/usr/local/bin/setup-user-web "$USERNAME"` falhar.
12. **Criar um script wrapper:**
Você pode criar um script que chama o adduser e, em seguida, executa o setup-user-web. Por exemplo:
```bash
#!/bin/bash
# Cria um novo usuário e configura a página web

adduser "$1"

if [[ $? -eq 0 ]]; then
    if /usr/local/bin/setup-user-web "$1"; then
        echo "Usuário '$1' criado e setup-user-web executado com sucesso."
    else
        echo "Usuário '$1' criado, mas houve um erro ao executar setup-user-web." >&2  # Envia a mensagem de erro para stderr
        exit 1 # Retorna um código de erro
    fi
else
    echo "Erro ao criar o usuário '$1'." >&2
    exit 1
fi
```

Salve este script como `adduser-web.sh`, torne-o executável e use-o para criar novos usuários.
```bash
chmod +x /usr/local/sbin/adduser-web.sh
```
Agora, você pode usar `adduser-web.sh` para criar novos usuários e configurar automaticamente suas páginas web.
```bash
sudo /usr/local/sbin/adduser-web.sh nome_do_usuario
```
### Observações
- **Segurança:** Certifique-se de que o diretório `public_html` e os arquivos dentro dele tenham as permissões corretas para evitar acesso não autorizado.
- **Firewall:** Se você estiver usando um firewall, certifique-se de que as portas 80 e 443 estejam abertas para permitir o tráfego HTTP e HTTPS.
- **HTTPS:** Considere configurar HTTPS para proteger as páginas web pessoais. Você pode usar o Let's Encrypt para obter certificados SSL gratuitos.
- **Backup:** Considere fazer backup das configurações do Nginx e dos diretórios `public_html` regularmente.
- **Documentação:** Consulte a documentação do Nginx e do Linux para obter mais informações sobre configuração e segurança.
- **Testes:** Sempre teste suas configurações em um ambiente de desenvolvimento antes de aplicá-las em produção.
- **Logs:** Monitore os logs do Nginx para identificar problemas de configuração ou segurança.
- **Atualizações:** Mantenha o Nginx e o sistema operacional atualizados para garantir a segurança e a estabilidade.
- **Limpeza:** Periodicamente, revise e limpe as configurações de usuários e páginas web que não são mais necessárias.
- **Automação:** Considere usar ferramentas de automação para gerenciar usuários e configurações de servidores, especialmente em ambientes de produção.


# Configurando o Nginx no Debian para Hosts Virtuais por Usuário

Este guia detalha como configurar o Nginx no seu servidor Debian (IP 191.222.252.87) para criar automaticamente diretórios `public_html`, ambientes virtuais Python para Streamlit (ou páginas HTML básicas) e hosts virtuais Nginx para cada novo usuário adicionado ao sistema.

**Pré-requisitos:**

*   Acesso root ao servidor Debian (via SSH ou console).
*   Conhecimento básico de linha de comando Linux.
*   Nginx instalado no servidor.  Se não estiver, instale com: `sudo apt update && sudo apt install nginx`
*   Python e pip instalados: `sudo apt update && sudo apt install python3 python3-pip`
*   Streamlit instalado (se você for usar Streamlit): `pip3 install streamlit`

**Passo 1: Criar o Diretório `/etc/skel/public_html` com Conteúdo Inicial**

Este diretório será copiado para a pasta `/home` de cada novo usuário. Você pode escolher entre um app Streamlit simples ou uma página HTML básica.

**Opção A: Streamlit App**

1.  **Crie o diretório:**

    ```bash
    sudo mkdir -p /etc/skel/public_html
    cd /etc/skel/public_html
    ```

2.  **Crie o arquivo `streamlit_app.py`:**

    ```bash
    sudo nano streamlit_app.py
    ```

    Cole o seguinte código Streamlit:

    ```python
    import streamlit as st

    st.title("Bem-vindo(a)!")
    st.write("Este é um aplicativo Streamlit básico.")

    nome = st.text_input("Digite seu nome:")
    if nome:
        st.write(f"Olá, {nome}!")
    ```

3.  **Crie o arquivo `requirements.txt`:**

    ```bash
    sudo nano requirements.txt
    ```

    Adicione:

    ```
    streamlit
    ```

4.  **Crie um script para inicializar o ambiente virtual e instalar dependências (opcional, mas recomendado):**

    ```bash
    sudo nano init_streamlit.sh
    ```

    Cole o seguinte script:

    ```bash
    #!/bin/bash

    # Cria o ambiente virtual
    python3 -m venv .venv

    # Ativa o ambiente virtual
    source .venv/bin/activate

    # Instala as dependências
    pip install -r requirements.txt

    # Desativa o ambiente virtual
    deactivate
    ```

    Torne o script executável:

    ```bash
    sudo chmod +x init_streamlit.sh
    ```

**Opção B: Página HTML Básica**

1.  **Crie o diretório:**

    ```bash
    sudo mkdir -p /etc/skel/public_html
    cd /etc/skel/public_html
    ```

2.  **Crie o arquivo `index.html`:**

    ```bash
    sudo nano index.html
    ```

    Cole o seguinte código HTML:

    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>Bem-vindo(a)!</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <h1>Bem-vindo(a) ao seu site!</h1>
        <p>Esta é uma página HTML básica.</p>
    </body>
    </html>
    ```

3.  **Crie o arquivo `style.css`:**

    ```bash
    sudo nano style.css
    ```

    Cole o seguinte código CSS (opcional, mas bom para estilo):

    ```css
    body {
        font-family: sans-serif;
        background-color: #f0f0f0;
        text-align: center;
    }

    h1 {
        color: #333;
    }

    p {
        color: #666;
    }
    ```

**Passo 2: Criar um Script para Configurar Novos Usuários**

Este script será executado automaticamente quando um novo usuário for adicionado.

1.  **Crie o script:**

    ```bash
    sudo nano /usr/local/sbin/create_user_website.sh
    ```

2.  **Cole o seguinte código:**

    ```bash
    #!/bin/bash

    # Script para criar diretório public_html, ambiente virtual (se necessário) e host virtual Nginx para novos usuários

    USERNAME="$1"

    if [ -z "$USERNAME" ]; then
        echo "Erro: Nome de usuário não fornecido."
        exit 1
    fi

    HOMEDIR="/home/$USERNAME"
    PUBLIC_HTML="$HOMEDIR/public_html"

    # Cria o diretório public_html se não existir
    if [ ! -d "$PUBLIC_HTML" ]; then
        echo "Criando diretório public_html para $USERNAME"
        cp -r /etc/skel/public_html "$PUBLIC_HTML"
        chown -R "$USERNAME":"$USERNAME" "$PUBLIC_HTML"

        # Se você estiver usando streamlit, inicializa o ambiente virtual
        if [ -f "$PUBLIC_HTML/init_streamlit.sh" ]; then
          echo "Inicializando ambiente virtual Streamlit para $USERNAME"
          su - "$USERNAME" -c "cd $PUBLIC_HTML && ./init_streamlit.sh"
        fi
    fi

    # Cria o host virtual Nginx
    VHOST_FILE="/etc/nginx/sites-available/$USERNAME.conf"
    SERVER_NAME="$USERNAME.191.222.252.87.xip.io" # Usando xip.io para testes.  Substitua por seu domínio real!

    echo "Criando host virtual Nginx para $USERNAME"

    cat <<EOF > "$VHOST_FILE"
    server {
        listen 80;
        listen [::]:80;
        server_name $SERVER_NAME;
        root $PUBLIC_HTML;
        index index.html index.htm;

        # Configuração para Streamlit (se estiver usando Streamlit)
        location / {
            proxy_pass http://localhost:8501; # Streamlit roda por padrão na porta 8501
            proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
            proxy_set_header Host \$http_host;
            proxy_redirect off;
        }

        # Configuração para arquivos estáticos (HTML básico)
        location / {
            try_files \$uri \$uri/ =404;
        }
    }
    EOF

    # Ativa o host virtual
    ln -s "$VHOST_FILE" /etc/nginx/sites-enabled/

    # Reinicia o Nginx
    systemctl restart nginx

    echo "Configuração do website para $USERNAME concluída."

    exit 0
    ```

    **Observações importantes sobre o script:**

    *   **`SERVER_NAME`:**  Este script usa `xip.io` para testes.  **Isso é APENAS para testes!**  Você **precisa** substituir `$USERNAME.191.222.252.87.xip.io` por um nome de domínio real que você possua e que aponte para o seu servidor (IP 191.222.252.87).  Se você não tem um domínio, você pode comprar um ou usar um serviço de DNS dinâmico.
    *   **Streamlit:** Se você estiver usando Streamlit, o script configura o Nginx para redirecionar as requisições para o aplicativo Streamlit rodando na porta 8501 (o padrão).
    *   **Permissões:** O script garante que o novo diretório `public_html` e seus arquivos pertençam ao novo usuário.
    *   **Ambiente Virtual Streamlit:** O script executa o `init_streamlit.sh` como o novo usuário, para criar e configurar o ambiente virtual.
    *   **`su - "$USERNAME" -c "..."`**:  Isso é fundamental.  Executa comandos como o usuário recém-criado, garantindo que o ambiente virtual seja configurado corretamente com as permissões corretas.
    *   **xip.io**: xip.io é útil para testar configurações locais sem precisar de um domínio real, mas *nunca* deve ser usado em produção.  Ele resolve qualquer nome `*.191.222.252.87.xip.io` para o IP 191.222.252.87.

3.  **Torne o script executável:**

    ```bash
    sudo chmod +x /usr/local/sbin/create_user_website.sh
    ```

**Passo 3: Configurar o `useradd` para Executar o Script**

Precisamos configurar o comando `useradd` para executar nosso script após a criação de cada novo usuário.

1.  **Edite o arquivo `/etc/adduser.conf`:**

    ```bash
    sudo nano /etc/adduser.conf
    ```

2.  **Localize a linha `FIRST_SYSTEM_UID=100` (ou similar) e adicione a seguinte linha abaixo dela:**

    ```
    ADDUSER_CONFIG=/etc/adduser.local.conf
    ```

3.  **Crie o arquivo `/etc/adduser.local.conf`:**

    ```bash
    sudo nano /etc/adduser.local.conf
    ```

4.  **Adicione a seguinte linha:**

    ```
    USERADD_POST_CMD /usr/local/sbin/create_user_website.sh
    ```

    **Importante:** Garanta que não haja espaços em branco extras no final da linha.

**Passo 4: Testar a Configuração**

1.  **Adicione um novo usuário:**

    ```bash
    sudo adduser testuser
    ```

    Você será solicitado a definir uma senha para o novo usuário e outras informações.

2.  **Verifique se o diretório `public_html` foi criado:**

    ```bash
    ls /home/testuser
    ```

    Você deve ver o diretório `public_html`.

3.  **Verifique se o host virtual Nginx foi criado:**

    ```bash
    ls /etc/nginx/sites-available/testuser.conf
    ls /etc/nginx/sites-enabled/testuser.conf
    ```

4.  **Se estiver usando Streamlit, verifique se o ambiente virtual foi criado:**

    ```bash
    ls /home/testuser/public_html/.venv
    ```

5.  **Acesse o site no seu navegador:**

    Abra seu navegador e digite `testuser.191.222.252.87.xip.io`. Se tudo estiver configurado corretamente, você deverá ver sua página HTML básica ou o aplicativo Streamlit.  Lembre-se, você precisa substituir `testuser.191.222.252.87.xip.io` pelo seu domínio real no arquivo `/etc/nginx/sites-available/testuser.conf` e recarregar o Nginx.

**Passo 5: Iniciando o Streamlit App (Se Estiver Usando Streamlit)**

Se você estiver usando Streamlit, o script `create_user_website.sh` cria o ambiente virtual, mas não inicia o aplicativo.  Você precisa iniciar o aplicativo Streamlit manualmente (ou configurar um serviço para iniciá-lo automaticamente).

1.  **Como iniciar o Streamlit app manualmente:**

    ```bash
    su - testuser -c "cd /home/testuser/public_html && source .venv/bin/activate && streamlit run streamlit_app.py"
    ```

    Isso iniciará o Streamlit app no terminal. Deixe o terminal aberto (ou use um gerenciador de processos como `nohup` ou `screen`).

2.  **Configurando um serviço systemd para iniciar o Streamlit app automaticamente:**

    Isso é a maneira recomendada para garantir que o Streamlit app sempre esteja rodando.

    *   **Crie um arquivo de serviço systemd:**

        ```bash
        sudo nano /etc/systemd/system/streamlit-testuser.service
        ```

    *   **Cole o seguinte conteúdo (ajuste os caminhos e o nome de usuário):**

        ```
        [Unit]
        Description=Streamlit App for testuser
        After=network.target

        [Service]
        User=testuser
        WorkingDirectory=/home/testuser/public_html
        ExecStart=/bin/bash -c "source .venv/bin/activate && streamlit run streamlit_app.py"
        Restart=on-failure

        [Install]
        WantedBy=multi-user.target
        ```

    *   **Habilite e inicie o serviço:**

        ```bash
        sudo systemctl enable streamlit-testuser.service
        sudo systemctl start streamlit-testuser.service
        ```

    *   **Verifique o status do serviço:**

        ```bash
        sudo systemctl status streamlit-testuser.service
        ```

        Isso mostrará se o serviço está rodando sem erros.

**Considerações Finais e Solução de Problemas:**

*   **Domínio:** A configuração mais crítica é garantir que o `server_name` nos arquivos de host virtual Nginx corresponda a um domínio que aponta para o seu servidor.  Sem isso, você não conseguirá acessar o site.
*   **Permissões:**  Verifique as permissões dos arquivos e diretórios.  O usuário deve ter permissão para ler e executar os arquivos em seu diretório `public_html`.
*   **Nginx:**  Certifique-se de que a configuração do Nginx esteja correta.  Erros na configuração podem impedir que o site seja exibido. Verifique os logs do Nginx em `/var/log/nginx/error.log` e `/var/log/nginx/access.log`.
*   **Firewall:**  Verifique se o firewall (se estiver ativo) está permitindo o tráfego HTTP (porta 80) e HTTPS (porta 443, se você estiver usando SSL) para o seu servidor.  `sudo ufw status` para verificar o status do firewall.
*   **Erros do Streamlit:** Se você estiver usando Streamlit e tiver problemas, verifique os logs do Streamlit para ver se há erros.  Se você configurou o systemd, os logs estarão em `journalctl -u streamlit-testuser.service`.
*   **SSL/HTTPS:**  Para uma configuração de produção, você definitivamente deve configurar SSL/HTTPS para criptografar o tráfego para o seu site. Você pode usar o Let's Encrypt para obter certificados SSL gratuitos: `sudo apt install certbot python3-certbot-nginx && sudo certbot --nginx -d seu_dominio.com`
*   **Segurança:** Revise as configurações de segurança do seu servidor, incluindo o firewall, as permissões de arquivos e diretórios, e as configurações do Nginx.

Este guia detalhado deve te ajudar a configurar o Nginx para gerenciar hosts virtuais por usuário, criar um ambiente de desenvolvimento básico e facilitar a criação de novos websites no seu servidor Debian. Lembre-se de adaptar o script e as configurações às suas necessidades específicas e de manter a segurança do seu servidor.

*   **Backup:** Sempre faça backup de suas configurações e dados antes de fazer alterações significativas no servidor.
*   **Documentação:** Consulte a documentação oficial do Nginx e do Streamlit para obter mais informações e opções de configuração avançadas.
*   **Comunidade:** Se você encontrar problemas, considere procurar ajuda em fóruns ou comunidades online, como Stack Overflow ou fóruns específicos do Debian e Nginx.
*   **Manutenção:** Revise periodicamente suas configurações e atualize o software para garantir que você esteja usando as versões mais seguras e estáveis.
*   **Monitoramento:** Considere implementar soluções de monitoramento para acompanhar o desempenho e a disponibilidade do seu servidor e aplicativos.
*   **Escalabilidade:** Se você planeja hospedar muitos usuários ou sites, considere soluções de escalabilidade, como balanceamento de carga ou contêineres (Docker).

## Links Úteis
*   [Documentação do Nginx](https://nginx.org/en/docs/)
*   [Documentação do Streamlit](https://docs.streamlit.io/)
*   [Documentação do Debian](https://www.debian.org/doc/)
*   [Documentação do Python](https://docs.python.org/3/)
*   [Documentação do pip](https://pip.pypa.io/en/stable/)
*   [Documentação do xip.io](http://xip.io/)
*   [Documentação do Let's Encrypt](https://letsencrypt.org/docs/)
*   [Documentação do Certbot](https://certbot.eff.org/)
*   [Documentação do systemd](https://www.freedesktop.org/wiki/Software/systemd/)
*   [Documentação do UFW](https://help.ubuntu.com/community/UFW)
*   [Documentação do SSH](https://www.ssh.com/academy/ssh)
*   [Documentação do adduser](https://manpages.debian.org/bullseye/adduser/adduser.8.en.html)
*   [Documentação do useradd](https://manpages.debian.org/bullseye/useradd/useradd.8.en.html)
*   [Documentação do bash](https://www.gnu.org/software/bash/manual/bash.html)
*   [Documentação do nano](https://www.nano-editor.org/docs.php)
*   [Documentação do chmod](https://manpages.debian.org/bullseye/coreutils/chmod.1.en.html)
*   [Documentação do chown](https://manpages.debian.org/bullseye/coreutils/chown.1.en.html)
# Configuração do Apache2 para Servir Sites a Partir dos Diretórios Home dos Usuários

Para configurar o Apache2 para servir sites a partir dos diretórios home dos usuários (como `http://siteteste.serveminecraft.net/~teste`), você precisará usar o módulo `mod_userdir`.

A forma `http://siteteste.serveminecraft.net/teste` (sem o `~`) é um pouco mais complexa de generalizar para todos os usuários e geralmente envolveria `Alias` ou `mod_rewrite` mais intrincados, podendo conflitar com outros diretórios na raiz do seu site. A abordagem padrão e mais simples é com o `~`.

Vamos focar na configuração `http://siteteste.serveminecraft.net/~usuario/`.

## Passos para configurar `mod_userdir`:

### 1. Verificar se o domínio principal está funcionando:
Primeiro, certifique-se de que `http://siteteste.serveminecraft.net/` já está configurado e funcionando corretamente no seu Apache. Esta configuração de `mod_userdir` será aplicada **dentro** desse VirtualHost (ou na configuração global se não houver VirtualHosts específicos).

### 2. Habilitar o módulo `mod_userdir`:
Na maioria das distribuições baseadas em Debian/Ubuntu:
```bash
sudo a2enmod userdir
sudo systemctl restart apache2
```

Em sistemas baseados em RHEL/CentOS, o módulo geralmente já está disponível, mas pode precisar ser carregado no arquivo de configuração principal se não estiver.

3. Configurar mod_userdir:

A configuração do mod_userdir geralmente fica em /etc/apache2/mods-available/userdir.conf (Debian/Ubuntu) ou diretamente no httpd.conf / apache2.conf ou em um arquivo de conf incluído (RHEL/CentOS).

Abra o arquivo de configuração do mod_userdir. Exemplo para Debian/Ubuntu:

```bash
sudo nano /etc/apache2/mods-available/userdir.conf
sudo nano /etc/httpd/conf.d/userdir.conf  # RHEL/CentOS
```

Você verá algo similar a isto (ou pode precisar adicionar/ajustar):
```apache
<IfModule mod_userdir.c>
    # UserDir: O diretório (relativo ao home do usuário) onde o conteúdo web será buscado.
    # 'public_html' é o padrão comum.
    UserDir public_html

    # Desabilita UserDir para o usuário root e outros usuários do sistema por segurança.
    UserDir disabled root

    # Habilita para todos os outros usuários.
    # Se quiser habilitar apenas para usuários específicos, comente a linha abaixo
    # e descomente a linha "UserDir enabled usuario1 usuario2".
    UserDir enabled

    # Exemplo para habilitar apenas para usuários específicos:
    # UserDir enabled teste joao maria

    <Directory /home/*/public_html>
        # AllowOverride: Permite que arquivos .htaccess sobrescrevam configurações.
        # FileInfo: Permite diretivas como AddType, ErrorDocument, etc.
        # AuthConfig: Permite diretivas de autenticação.
        # Limit: Permite diretivas como Deny, Allow.
        # Indexes: Permite listagem de diretórios se não houver index.html/php.
        AllowOverride FileInfo AuthConfig Limit Indexes

        # Options: Configurações para o diretório.
        # MultiViews: Permite content negotiation (ex: requisitar /file e servir /file.html).
        # Indexes: Habilita listagem de diretórios.
        # FollowSymLinks: Permite seguir links simbólicos (cuidado com a segurança).
        # SymLinksIfOwnerMatch: Mais seguro, só segue links se o dono do link for o mesmo do alvo.
        # IncludesNoExec: Permite Server-Side Includes (SSI) mas não a execução de CGI via SSI.
        Options MultiViews Indexes SymLinksIfOwnerMatch IncludesNoExec

        # Controle de Acesso para Apache 2.4+
        Require method GET POST OPTIONS
        # Para Apache 2.2 (mais antigo), seria:
        # Order allow,deny
        # Allow from all
    </Directory>

    # Se os diretórios home dos seus usuários não estiverem em /home/,
    # ajuste o caminho no <Directory> acima.
    # Por exemplo, se estiverem em /var/www/users/, seria:
    # <Directory /var/www/users/*/public_html>
</IfModule>
```

Explicação das diretivas chave:

UserDir public_html: Define que o Apache procurará por um diretório chamado public_html dentro do diretório home de cada usuário. Ex: /home/teste/public_html/. Você pode mudar public_html para outro nome se preferir (ex: www, htdocs).

UserDir disabled root: Desabilita o acesso via ~root por segurança.

UserDir enabled: Habilita para todos os outros usuários. Você pode listar usuários específicos se preferir maior controle (ex: UserDir enabled teste pedro).

<Directory /home/*/public_html>: Aplica configurações específicas para todos os diretórios public_html dos usuários.

AllowOverride: Controla quais diretivas podem ser colocadas em arquivos .htaccess dentro dos diretórios dos usuários. FileInfo AuthConfig Limit Indexes é uma boa base. Se você confia nos seus usuários, pode usar All.

Options: Define quais recursos do servidor estão disponíveis. Indexes permite que o Apache liste os arquivos de um diretório se não houver um index.html (ou similar). FollowSymLinks ou SymLinksIfOwnerMatch são importantes se os usuários precisarem usar links simbólicos.

Require method GET POST OPTIONS: (Apache 2.4+) Permite acesso a esses diretórios usando os métodos HTTP especificados. Se estiver usando Apache 2.2, seria Order allow,deny e Allow from all.

# 4. Criar o diretório public_html para os usuários:

Para cada usuário que você quer que tenha um site (ex: teste), você precisa criar o diretório public_html em seu diretório home e definir as permissões corretas.

Logado como root ou usando sudo:

## Criar o diretório para o usuário 'teste' (se ele já existir, pule)
```bash
# sudo useradd -m teste # (se o usuário ainda não existir)
# sudo passwd teste     # (defina uma senha para o usuário)

# Criar o diretório public_html
sudo mkdir /home/teste/public_html

# Dar posse do diretório ao usuário 'teste'
sudo chown teste:teste /home/teste/public_html

# Ajustar permissões:
# O diretório home do usuário precisa ter permissão de execução para 'outros' (o Apache)
# para que o Apache possa entrar nele.
sudo chmod 711 /home/teste

# O diretório public_html precisa ser legível e executável pelo Apache.
sudo chmod 755 /home/teste/public_html

# Crie um arquivo de teste
sudo su - teste -c "echo '<h1>Página do Usuário Teste</h1>' > /home/teste/public_html/index.html"
# Ou, como root:
# echo '<h1>Página do Usuário Teste</h1>' | sudo tee /home/teste/public_html/index.html
# sudo chown teste:teste /home/teste/public_html/index.html
sudo chmod 644 /home/teste/public_html/index.html
```

# Permissões importantes:

Diretório home do usuário (ex: /home/teste): Precisa ter permissão de execução (x) para o grupo "outros" ou para o usuário/grupo do Apache (www-data em Debian/Ubuntu). 711 (drwx--x--x) é uma boa opção, pois permite que o dono tenha controle total, e outros possam apenas "entrar" no diretório, mas não listar seu conteúdo.

Diretório public_html (ex: /home/teste/public_html): Precisa ser legível e executável pelo Apache. 755 (drwxr-xr-x) é comum.

Arquivos dentro de public_html (ex: index.html): Precisam ser legíveis pelo Apache. 644 (-rw-r--r--) é comum.

# 5. Reiniciar o Apache:

Após fazer as alterações de configuração e criar os diretórios:

```bash
# Para Debian/Ubuntu:
sudo systemctl restart apache2
```

Ou, se estiver em um sistema mais antigo:

```bash
sudo service apache2 restart
```

# 6. Testar:

Abra seu navegador e acesse: http://siteteste.serveminecraft.net/~teste/
Você deverá ver a "Página do Usuário Teste".

## VirtualHost Específico:

Se você tem um VirtualHost configurado para siteteste.serveminecraft.net em, por exemplo, /etc/apache2/sites-available/siteteste.conf, a configuração do mod_userdir (o arquivo userdir.conf) geralmente se aplica globalmente. No entanto, as diretivas UserDir e as configurações do <Directory /home/*/public_html> também podem ser colocadas dentro do seu bloco <VirtualHost> se você quiser que elas se apliquem apenas a esse host virtual específico.

Exemplo de um VirtualHost com mod_userdir embutido (menos comum, mas possível):

```apache	
<VirtualHost *:80>
    ServerName siteteste.serveminecraft.net
    DocumentRoot /var/www/siteteste.serveminecraft.net/html

    # ... outras configurações do seu VirtualHost ...

    # Configurações UserDir específicas para este VirtualHost
    UserDir public_html
    UserDir disabled root
    UserDir enabled teste

    <Directory /home/teste/public_html>
        AllowOverride All  # Ou mais restritivo
        Options Indexes FollowSymLinks MultiViews
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/siteteste_error.log
    CustomLog ${APACHE_LOG_DIR}/siteteste_access.log combined
</VirtualHost>
```

Na maioria dos casos, manter a configuração do userdir.conf separada e global é mais limpo, e ela será herdada pelos VirtualHosts.

# Solução de Problemas:

403 Forbidden: Geralmente problema de permissões nos diretórios (/home/usuario ou /home/usuario/public_html) ou nas configurações do Apache (Require ou Order/Allow). Verifique os logs de erro do Apache (/var/log/apache2/error.log).

404 Not Found: O diretório public_html não existe, o arquivo index.html (ou similar) não existe dentro dele, ou a diretiva UserDir está apontando para o nome errado (ex: UserDir www mas o diretório é public_html).

Verifique se o SELinux (em sistemas como CentOS/RHEL) está interferindo. Pode ser necessário ajustar as políticas do SELinux para permitir que o Apache leia os diretórios home dos usuários. (Ex: setsebool -P httpd_enable_homedirs 1).

Lembre-se de substituir teste pelo nome de usuário real e ajustar os caminhos se os diretórios home dos seus usuários não estiverem em /home/.


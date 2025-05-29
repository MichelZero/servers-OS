```config
# Configuração do Nginx para o site siteteste.serveminecraft.net
server {
    listen 80;
    listen [::]:80;
    server_name siteteste.serveminecraft.net;
    root /var/www/html;
    index index.html index.htm index.php;

    location / {
        try_files $uri $uri/ =404;
    }

    location /teste {
        alias /var/www/teste;
        index index.html index.htm index.php;
        try_files $uri $uri/ =404;
    }

    # Adicione outros blocos location conforme necessário
    # para recursos específicos, como CSS, JavaScript, imagens, etc.
    # dentro de cada diretório.  Exemplo para /teste:
    #
    # location ~ ^/teste/images/ {
    #     alias /var/www/teste/images/;
    # }

    # Configurações adicionais, como logs de acesso, etc.
    access_log /var/log/nginx/siteteste.access.log;
    error_log /var/log/nginx/siteteste.error.log;
}
```

# Comandos:

- Habilitar, iniciar ou reiniciar um serviço:
sudo systemctl restart nomeservico
sudo systemctl start nomeservico
sudo systemctl status nomeservico

- Verificar se o nginx está rodando:
sudo systemctl status nginx
- Verificar se o nginx está rodando na porta 80:
sudo netstat -tuln | grep 80
- Verificar se o nginx está rodando na porta 443:
sudo netstat -tuln | grep 443
- Verificar se o nginx está rodando na porta 8080:
sudo netstat -tuln | grep 8080


## Criação do link simbólico par habilitar o site no nginx:
 digite o seguinte comando no terminal:
```
sudo ln -s /etc/nginx/sites-available/seuarquivo /etc/nginx/sites-enabled/
```	

substitua "seuarquivo" pelo nome do arquivo de configuração do seu site.
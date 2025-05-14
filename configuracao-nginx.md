


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
# Instalação do Screenfetch no MOTD do Debian

Este guia explica como exibir a saída do `screenfetch` na mensagem do dia (MOTD) do Debian após o login SSH.

## Instalação

1. **Instale o screenfetch:**

   ```bash
   sudo apt update
   sudo apt install screenfetch


Crie o script de atualização do MOTD:

sudo nano /etc/update-motd.d/99-screenfetch
2. **Crie o script de atualização do MOTD:**

   Crie um novo arquivo chamado `99-screenfetch` em `/etc/update-motd.d/`:

   ```bash
   sudo nano /etc/update-motd.d/99-screenfetch
   ```
3. **Adicione o seguinte conteúdo ao script:**
   Cole o seguinte conteúdo no arquivo:

```bash
#!/bin/bash

if [ -f /var/run/motd.screenfetch_done ]; then
  exit 0
fi
touch /var/run/motd.screenfetch_done

> /var/run/motd.screenfetch

screenfetch >> /var/run/motd.screenfetch

chmod 644 /var/run/motd.screenfetch

exit 0
```
4. **Salve e feche o arquivo:**
   Pressione `CTRL + X`, depois `Y` e `Enter` para salvar e sair do editor.
5. **Torne o script executável:**
   Execute o seguinte comando para tornar o script executável:

   ```bash
   sudo chmod +x /etc/update-motd.d/99-screenfetch
   ```
6. **Teste o script:**
   Execute o script manualmente para verificar se ele funciona corretamente:

   ```bash
   /etc/update-motd.d/99-screenfetch
   ```

   Isso deve gerar a saída do screenfetch no terminal.
7. **Verifique o arquivo de saída:**
   Verifique o conteúdo do arquivo `/var/run/motd.screenfetch` para garantir que a saída do screenfetch foi gerada corretamente:

   ```bash
   cat /var/run/motd.screenfetch
   ```

   Isso deve exibir a saída do screenfetch.
8. **Adicione o script ao MOTD:**
   O script já está configurado para ser executado automaticamente no login SSH, pois está localizado em `/etc/update-motd.d/`. No entanto, você pode verificar se o serviço `motd` está habilitado:

   ```bash
   sudo systemctl status motd
   ```

   Se não estiver habilitado, você pode habilitá-lo com:

   ```bash
   sudo systemctl enable motd
   ```
9. **Verifique as permissões:**
   Certifique-se de que as permissões do script e do arquivo de saída estejam corretas:

   ```bash
   ls -l /etc/update-motd.d/99-screenfetch
   ls -l /var/run/motd.screenfetch
   ```
   As permissões recomendadas são:
   - `/etc/update-motd.d/99-screenfetch`: `755` (rwxr-xr-x)
   - `/var/run/motd.screenfetch`: `644` (rw-r--r--)
10. **Verifique o arquivo de configuração do SSH:**
    Certifique-se de que o arquivo de configuração do SSH (`/etc/ssh/sshd_config`) tenha a seguinte linha:

    ```bash
    PrintMotd yes
    ```

    Isso garante que o MOTD seja exibido após o login SSH.
11. **Reinicie o serviço SSH:**
    Após fazer alterações no arquivo de configuração do SSH, reinicie o serviço SSH para aplicar as alterações:

    ```bash
    sudo systemctl restart ssh
    ```
12. **Verifique o funcionamento:**
    Faça login via SSH novamente e verifique se a saída do screenfetch é exibida corretamente.
    ```bash
    ssh user@your_server_ip
    ```
    Você deve ver a saída do screenfetch na mensagem do dia (MOTD) após o login.
13. **Verifique o arquivo de saída:**
    Após o login, você pode verificar o conteúdo do arquivo `/var/run/motd.screenfetch` para ver a saída do screenfetch:

    ```bash
    cat /var/run/motd.screenfetch
    ```
    Isso deve exibir a saída do screenfetch.
14. **Limpeza:**
    Se você quiser limpar o arquivo de saída após cada login, adicione o seguinte comando ao final do script:

    ```bash
    rm -f /var/run/motd.screenfetch_done
    ```

    Isso garante que o script seja executado novamente na próxima vez que você fizer login.
15. **Verifique o funcionamento:**
    Faça login via SSH novamente e verifique se a saída do screenfetch é exibida corretamente.

```bash
ssh user@your_server_ip
```
# alternativa simples
```bash
sudo apt install screenfetch
```
```bash
sudo nano /etc/update-motd.d/99-screenfetch
```
```bash
#!/bin/bash
#!/bin/sh
if [ -f /usr/bin/screenfetch ]; then screenfetch; fi
```
```bash
sudo chmod +x /etc/update-motd.d/99-screenfetch
```
```bash
sudo nano /etc/ssh/sshd_config
```
```bash
PrintMotd yes
```
```bash
sudo systemctl restart ssh
```
```bash
ssh user@your_server_ip
```
```bash
cat /var/run/motd.screenfetch
```
```bash
rm -f /var/run/motd.screenfetch_done
```
```bash
ssh user@your_server_ip
```

## Conclusão
Agora você deve ter a saída do `screenfetch` exibida na mensagem do dia (MOTD) após o login SSH no Debian. Isso fornece uma visão rápida do sistema e suas informações relevantes.
## links utils
- [Debian Wiki - MOTD](https://wiki.debian.org/MOTD)
- [Debian Wiki - Screenfetch](https://wiki.debian.org/Screenfetch)
- [Debian Wiki - SSH](https://wiki.debian.org/SSH)
- [Debian Wiki - Neofetch](https://wiki.debian.org/Neofetch)
- [Debian Wiki - Update-motd](https://wiki.debian.org/Update-motd)
- [Debian Wiki - Update-motd.d](https://wiki.debian.org/Update-motd.d)
- [Debian Wiki - Update-motd.d/99-screenfetch](https://wiki.debian.org/Update-motd.d/99-screenfetch)
- [Debian Wiki - Update-motd.d/99-neofetch](https://wiki.debian.org/Update-motd.d/99-neofetch)
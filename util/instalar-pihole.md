# Instalação do Pi-hole no Ubuntu

A instalação do Pi-hole no Ubuntu usando o script oficial é bastante direta. Aqui estão os passos:

## Pré-requisitos:

* **Acesso root ou sudo:** Você precisará de privilégios de administrador para instalar o Pi-hole.
* **Conexão com a internet:** O script de instalação baixa os componentes necessários.
* **Um sistema Ubuntu suportado:** O Pi-hole funciona melhor em sistemas Ubuntu Server, mas também pode ser instalado em versões desktop.

## Passos de Instalação:

1. **Abra um terminal.**

2. **Baixe e execute o script de instalação usando curl:**

   ```bash
   curl -sSL https://install.pi-hole.net | bash


Alternativamente, você pode usar wget:

wget -O basic-install.sh https://install.pi-hole.net
sudo bash basic-install.sh


Siga as instruções na tela: O instalador irá guiá-lo pelo processo. Algumas decisões importantes que você precisará tomar incluem:

Interface de rede: Selecione a interface de rede que o Pi-hole deve usar (geralmente eth0 ou wlan0).

Servidor upstream de DNS: Escolha um servidor upstream de DNS (por exemplo, Google DNS, Cloudflare DNS, OpenDNS, etc.). Você pode especificar servidores personalizados também.

Bloquear listas: Você pode optar por usar as listas de bloqueio padrão ou fornecer suas próprias listas.

Endereço IP estático (recomendado): Configure um endereço IP estático para o seu Pi-hole para evitar que o endereço IP mude e interrompa o serviço.

Anote a senha administrativa da web: O instalador irá gerar uma senha aleatória para a interface web. Anote-a, pois você precisará dela para acessar as configurações do Pi-hole.

Configure seu roteador (ou DHCP server) para usar o Pi-hole como servidor DNS: Esta é a etapa mais crucial. Acesse as configurações do seu roteador e altere as configurações de DNS para apontar para o endereço IP do seu Pi-hole. Isso garantirá que todo o tráfego de rede na sua rede local seja filtrado pelo Pi-hole.

Acesso à interface web:

Após a instalação, você pode acessar a interface web do Pi-hole em http://<endereco_ip_pi-hole>/admin ou http://pi.hole/admin. Use a senha administrativa que você anotou durante a instalação.

Pós-Instalação:

Atualizações: Mantenha o Pi-hole e suas listas de bloqueio atualizados executando o seguinte comando no terminal:



Whitelisting/Blacklisting: Você pode adicionar domínios à whitelist (permitir) ou blacklist (bloquear) através da interface web.

Documentação: Consulte a documentação oficial do Pi-hole para obter mais informações e opções de configuração: https://docs.pi-hole.net/

Com esses passos, você terá o Pi-hole instalado e funcionando em seu sistema Ubuntu, bloqueando anúncios e rastreadores em sua rede local.


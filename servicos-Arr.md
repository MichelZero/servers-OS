# Gerenciamento de mídia com os serviços "*Arr"

## Usando Docker dentro de uma VM (Altamente Recomendado)


O que são os Serviços *Arr (também conhecidos como Servarr)?

Os serviços *Arr são um conjunto de ferramentas de automação, cada uma focada em um tipo de mídia, projetadas para monitorar, buscar e organizar conteúdo digital. O nome "Arr" vem do final do nome de cada aplicação (Sonarr, Radarr, etc.).

Eles funcionam como "gerentes" inteligentes para seus downloads:

Você diz o que quer: Por exemplo, você adiciona uma série de TV ao Sonarr.

Eles monitoram: O Sonarr fica de olho em fontes de conteúdo (indexadores de torrents ou Usenet) por novos episódios daquela série.

Eles buscam e enviam para download: Quando um novo episódio é encontrado, o Sonarr o envia para seu cliente de download (como qBittorrent ou SABnzbd).

Eles organizam: Depois que o download termina, o Sonarr pega o arquivo, o renomeia para um formato limpo e o move para a pasta correta da sua biblioteca de mídia (a mesma que você usa no Jellyfin/Plex).

Os principais serviços são:

Sonarr: Para séries de TV.

Radarr: Para filmes.

Lidarr: Para músicas.

Readarr: Para livros (eBooks e audiobooks).

Prowlarr: Para gerenciar e sincronizar as configurações dos seus indexadores (as fontes de conteúdo) entre todos os outros *Arrs. É altamente recomendado começar por ele.

Como Criar um Contêiner para os Serviços *Arr no Proxmox

Existem duas abordagens principais para rodar esses serviços no Proxmox. A Abordagem 2 (usando Docker) é a mais recomendada hoje em dia por sua simplicidade e facilidade de manutenção.

Abordagem 1: Usando Contêineres LXC Individuais (Mais Tradicional)

Neste método, você cria um contêiner LXC para cada serviço *Arr. É uma boa maneira de aprender como os serviços funcionam individualmente.

Vantagens:

Isolamento completo entre os serviços.

Usa recursos de forma muito eficiente.

Desvantagens:

Configuração mais manual e repetitiva.

Atualizações precisam ser feitas dentro de cada contêiner.

Passos para criar um LXC para o Radarr (repita para os outros):

Crie o Contêiner LXC:

Na interface do Proxmox, clique em "Create CT".

Dê um nome (ex: radarr-ct).

Use um template de Ubuntu ou Debian.

Aloque recursos (ex: 1 CPU, 512MB RAM, 8GB de disco é um bom começo).

Configure a rede.

Finalize a criação.

Acesse o Console do Contêiner:

Inicie o contêiner e abra o console.

Instale o Radarr:

Primeiro, atualize o sistema:

```Bash
apt update && apt upgrade -y
```

Instale as dependências necessárias:

```code
apt install curl sqlite3 -y
```

Baixe e instale o Radarr (consulte o site oficial do Radarr para o comando de download mais recente, mas geralmente é algo assim):

```code
curl -L -o Radarr.develop.tar.gz https://radarr.servarr.com/v1/update/develop/updatefile?os=linux&runtime=netcore&arch=x64
tar -xvzf Radarr.develop.tar.gz
mv Radarr /opt
```

Crie um usuário para rodar o serviço e dê as permissões:

```Bash
useradd -m -s /bin/bash radarr
chown -R radarr:radarr /opt/Radarr
```

Configure para rodar como um serviço (crie um arquivo .service em /etc/systemd/system/) para que ele inicie com o contêiner.

Como você pode ver, é um processo bastante manual. Por isso, a comunidade de homelab criou soluções mais simples.

Abordagem 2: Usando Docker dentro de uma VM (Altamente Recomendado)

Este é o método mais popular, moderno e fácil. Você cria uma única Máquina Virtual, instala o Docker nela e gerencia todos os seus serviços *Arr (e outros) com um único arquivo de configuração.

Vantagens:

Extremamente fácil de gerenciar: Um único arquivo (docker-compose.yml) define toda a sua pilha de serviços.

Atualizações simples: Atualizar um serviço é tão fácil quanto mudar um número de versão e rodar um comando.

Comunidade enorme: Inúmeros exemplos e tutoriais disponíveis.

*Passos para criar a pilha Arr com Docker:

Crie uma VM para o Docker:

Crie uma VM no Proxmox (ex: docker-vm).

Instale um sistema operacional leve, como Debian ou Ubuntu Server.

Aloque recursos (ex: 2 CPUs, 2GB RAM, 20GB de disco é um bom começo).

Instale o Docker e o Docker Compose na VM:

Acesse a VM via SSH ou console.

Siga o guia oficial do Docker para instalar o Docker Engine e o plugin Docker Compose no seu sistema operacional. O comando geralmente é um script de conveniência:

```Bash
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

Crie um arquivo docker-compose.yml:

Crie um diretório para sua configuração, por exemplo: mkdir servarr && cd servarr.

Crie o arquivo: nano docker-compose.yml.

Cole uma configuração parecida com a de baixo. Este é um exemplo básico para começar:

```Yaml
version: "3.8"
services:
  prowlarr:
    image: lscr.io/linuxserver/prowlarr:latest
    container_name: prowlarr
    environment:
      - PUID=1000 # ID do seu usuário
      - PGID=1000 # ID do seu grupo
      - TZ=America/Sao_Paulo # Seu fuso horário
    volumes:
      - ./prowlarr-config:/config # Pasta para configuração
    ports:
      - "9696:9696" # Porta de acesso
    restart: unless-stopped

  radarr:
    image: lscr.io/linuxserver/radarr:latest
    container_name: radarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=America/Sao_Paulo
    volumes:
      - ./radarr-config:/config
      - /caminho/para/sua/biblioteca/de/filmes:/movies # IMPORTANTE: Aponte para sua biblioteca
      - /caminho/para/sua/pasta/de/downloads:/downloads # IMPORTANTE: Aponte para a pasta de downloads
    ports:
      - "7878:7878"
    restart: unless-stopped

  # Adicione Sonarr, Lidarr, etc., seguindo o mesmo padrão...

```

Atenção:

Volumes: Os volumes são cruciais. A linha - /caminho/para/sua/biblioteca/de/filmes:/movies "mapeia" uma pasta do seu servidor (a parte da esquerda) para dentro do contêiner (a parte da direita). Você precisa ajustar esses caminhos para as suas pastas reais de mídia e downloads.

PUID e PGID: Representam o usuário que será dono dos arquivos. Rode o comando id seu_usuario no terminal da VM para obter esses valores e use-os no arquivo.

Inicie os serviços:

No mesmo diretório onde está seu arquivo docker-compose.yml, rode:

```Bash
docker-compose up -d
```

O -d faz com que os contêineres rodem em segundo plano.

Agora, você pode acessar cada serviço pelo IP da sua VM seguido da porta que você definiu (ex: http://IP_DA_VM:7878 para acessar o Radarr).

Comece com Prowlarr, configure seus indexadores nele e depois configure os outros *Arrs para usar o Prowlarr. Isso economizará muito tempo

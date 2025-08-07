# Como ativar o BTH no MikroTik

apenas para a vrsão 7.12->+

leia: https://mikrotik.com/bth/

Passo 1: A Verificação Mais Importante - Você tem um IP Público? (Verificar CGNAT)

Este é o passo decisivo. Se você não tiver um IP público, o método de redirecionamento de portas não vai funcionar.

Acesse seu MikroTik (via WinBox ou WebFig).

No menu, vá para IP > DHCP Client. Encontre a linha correspondente à sua interface de internet (geralmente ether1 ou pppoe-out1). Anote o endereço IP que aparece lá.

Agora, em um computador na sua rede, acesse um site como "meuip.com.br" ou "whatismyip.com".

Compare os dois IPs:

Se os IPs forem IGUAIS: Ótimo! Você tem um IP público e pode prosseguir com o Passo 2.

Se os IPs forem DIFERENTES: Você está atrás de um CGNAT (Carrier-Grade NAT). Isso significa que seu provedor compartilha um único IP público entre vários clientes. Neste caso, o redirecionamento de portas NÃO VAI FUNCIONAR. Pule diretamente para a seção "Plano B: O que fazer se você tem CGNAT" no final.

Passo 2: Configurar um DNS Dinâmico (DDNS)

Seu IP público, mesmo sendo seu, provavelmente muda de tempos em tempos. Para não ter que decorar um novo IP a cada vez, usamos um serviço de DDNS, que lhe dá um "nome" fixo (ex: minhacasa.ddns.net).

O MikroTik tem um serviço de DDNS gratuito e já integrado!

No MikroTik, vá para IP > Cloud.

Marque a caixa "DDNS Enabled".

Clique em Apply.

Aguarde alguns segundos. O campo "Public Address" mostrará seu IP, e o campo "DNS Name" mostrará seu nome de acesso, algo como xxxxxxxxxxxx.sn.mynetname.net. Anote este nome! Este será o seu endereço para acessar sua rede de fora.

Passo 3: Criar a Regra de Redirecionamento de Porta (Port Forwarding / DST-NAT)

Agora vamos dizer ao MikroTik: "Quando uma conexão chegar da internet na porta 8006, envie-a para o Proxmox no IP 192.168.0.20".

(Nota: Vou assumir que sua rede local no MikroTik está configurada na faixa 192.168.0.x. Se estiver na faixa padrão 192.168.88.x, o Proxmox precisa ter um IP nessa mesma faixa para que a comunicação funcione).

No MikroTik, vá para IP > Firewall.

Abra a aba NAT.

Clique no botão + para adicionar uma nova regra.

Na janela que abrir, preencha a aba General:

Chain: dstnat (Destination NAT - pois o destino do pacote será alterado).

Protocol: 6 (tcp) (A interface web do Proxmox usa TCP).

Dst. Port: 8006 (A porta externa que você vai usar para acessar).

In. Interface: Selecione sua interface de internet (WAN), geralmente ether1 ou pppoe-out1.

Agora, mude para a aba Action:

Action: dst-nat

To Addresses: 192.168.0.20 (O IP interno do seu Proxmox).

To Ports: 8006 (A porta interna do serviço no Proxmox).

Clique em OK. Arraste esta regra para o topo da lista de NAT para garantir que ela seja processada primeiro.

Passo 4: Testando o Acesso

Agora, de fora da sua rede (por exemplo, usando o 4G/5G do seu celular), abra um navegador e acesse:

https://SEU_DNS_NAME:8006

Substitua SEU_DNS_NAME pelo nome que você anotou no Passo 2. Exemplo:

https://12345678abcd.sn.mynetname.net:8006

Se tudo deu certo, a página de login do seu Proxmox deverá aparecer!

🚨 Plano B: O que fazer se você tem CGNAT

Se a verificação no Passo 1 mostrou que você está em CGNAT, não se preocupe. Você ainda pode acessar sua rede, mas usando métodos diferentes que "furam" o bloqueio do CGNAT. A melhor e mais segura opção é uma VPN.

Solução Recomendada: Usar WireGuard (VPN) no MikroTik

Seu hAP ax3 tem suporte nativo para WireGuard, uma VPN moderna, rápida e segura.

Configure o servidor WireGuard no seu MikroTik: Você criará uma "interface" WireGuard no roteador.

Crie um "Peer" (um perfil de cliente) no MikroTik: Este perfil será para o seu celular ou notebook que vai acessar a rede remotamente.

Instale o aplicativo WireGuard no seu celular/notebook: E configure-o usando os dados do peer que você criou (pode ser via QR Code).

Quando você ativa a VPN no seu celular, ele cria um túnel seguro diretamente para o seu MikroTik. Seu celular passa a se comportar como se estivesse fisicamente na sua rede local. Você poderá simplesmente abrir o navegador e digitar https://192.168.0.20:8006 para acessar o Proxmox.

Vantagens desta abordagem:

Funciona com CGNAT.

MUITO mais seguro: Você não expõe nenhuma porta do seu Proxmox diretamente para a internet. A única porta aberta é a da VPN.

Acesso total: Você acessa não só o Proxmox, mas qualquer outro dispositivo da sua rede.

Existem muitos tutoriais online sobre como configurar o WireGuard no MikroTik. É a forma mais profissional e segura de fazer o que você quer.

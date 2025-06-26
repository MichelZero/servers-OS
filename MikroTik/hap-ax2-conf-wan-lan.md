Claro! Configurar um MikroTik hAP ax2 pode parecer complexo no início, mas seguindo os passos corretos, o processo se torna bastante lógico. O RouterOS (sistema operacional da MikroTik) oferece duas maneiras principais de configuração: uma super rápida (Quick Set) e outra manual, que dá mais controle e é ótima para aprender.

Vamos cobrir as duas.

Pré-requisitos: Acesso Inicial

Antes de tudo, você precisa acessar o roteador.

Conexão Física:

Ligue o hAP ax2 na tomada.

Conecte um cabo de rede do seu computador a uma das portas LAN (geralmente da ether2 à ether5). Não conecte na porta ether1 por enquanto, pois ela será a nossa porta WAN (internet).

Acesso ao Roteador:

Via Web (WebFig): Abra seu navegador e acesse o endereço padrão: http://192.168.88.1.

Via WinBox: Esta é a ferramenta recomendada. Baixe o WinBox no site da MikroTik. Ao abri-lo, ele deve encontrar seu roteador na aba "Neighbors". Clique no endereço MAC para conectar.

Login Padrão: O usuário é admin e a senha é em branco.

Ao acessar pela primeira vez, o roteador mostrará uma tela com a configuração padrão. Você pode mantê-la ou removê-la para começar do zero. Para este guia, vamos assumir que você está partindo da configuração padrão.

Método 1: A Rota Fácil e Rápida (Quick Set)

Para 90% dos usuários domésticos, o "Quick Set" é suficiente e resolve tudo em 2 minutos.

No menu à esquerda (seja no WebFig ou WinBox), clique em Quick Set.

A tela que abrirá terá tudo o que você precisa para uma configuração básica.

Na tela do Quick Set, configure o seguinte:

Mode: Mantenha em Home AP ou WISP AP.

Internet (WAN):

Address Acquisition: Aqui você define como seu roteador recebe internet do seu provedor.

Automatic (DHCP): A mais comum. Use esta se seu provedor (Vivo Fibra, Claro/NET, etc.) entrega o IP automaticamente via cabo de rede.

PPPoE: Use esta se seu provedor exige um usuário e senha para conectar (comum em ADSL ou algumas redes de fibra de bairro). Você precisará preencher os campos PPPoE User e PPPoE Password.

Static: Use se seu provedor te forneceu um endereço de IP, máscara de sub-rede, gateway e DNS fixos. Você precisará preencher todos esses campos manualmente.

Local Network (LAN):

IP Address: 192.168.88.1. É o endereço do seu roteador. Pode deixar o padrão.

DHCP Server: Mantenha marcado. Isso fará com que o roteador distribua IPs automaticamente para seus dispositivos (celulares, PCs, etc.).

NAT: Mantenha marcado. É essencial para que os dispositivos da sua rede local possam acessar a internet.

Wireless (Wi-Fi):

Network Name (SSID): O nome da sua rede Wi-Fi (ex: "MinhaCasa_WiFi").

Frequency: Pode deixar em auto. O hAP ax2 é dual-band.

Band: Selecione 2GHz-B/G/N/AX e 5GHz-A/N/AC/AX para máxima compatibilidade.

Country: Muito importante! Selecione brazil. Isso ajusta os canais e a potência de transmissão para as regulações brasileiras, otimizando o desempenho.

WiFi Password: Crie uma senha forte para sua rede Wi-Fi.

System:

Password: Extremamente importante! Crie uma senha forte para acessar o roteador. Não deixe em branco.

Clique em Apply ou OK. Pronto! Sua rede WAN e LAN já estão configuradas. Conecte o cabo do seu provedor de internet na porta ether1 e teste a conexão.

Método 2: A Rota Completa (Configuração Manual)

Este método te dá controle total e ensina como o RouterOS funciona. É ideal se você quer uma configuração personalizada ou se removeu a configuração padrão.

Passo 0: Resetar (Opcional, mas recomendado para aprender)
Se quiser começar do zero, vá em System -> Reset Configuration, marque a opção No Default Configuration e clique em Reset Configuration. O roteador irá reiniciar. Você precisará se reconectar via WinBox pelo endereço MAC.

Parte 1: Configurando a WAN (Internet)

A porta ether1 será nossa WAN.

Cenário A: Internet via DHCP (Mais comum)

Vá em IP -> DHCP Client.

Clique no botão + (Adicionar).

Na nova janela, selecione a Interface: ether1.

Deixe as outras opções como estão e clique em OK.

Em poucos segundos, o status deve mudar para "bound" e você verá o IP que seu provedor te deu.

Cenário B: Internet via PPPoE

Vá em PPP.

Na aba Interface, clique no + e escolha PPPoE Client.

Na aba General, selecione a Interface: ether1.

Na aba Dial Out, preencha User e Password com as credenciais do seu provedor.

Marque as caixas Use Peer DNS e Add Default Route.

Clique em OK.

Parte 2: Configurando a LAN (Sua Rede Local)

Vamos agrupar as portas LAN e o Wi-Fi em uma única rede usando uma "Bridge".

Criar a Bridge:

Vá em Bridge.

Na aba Bridge, clique no +. Dê um nome, como bridge-lan, e clique em OK.

Adicionar Portas à Bridge:

Ainda em Bridge, vá para a aba Ports.

Clique no + para adicionar cada porta que fará parte da sua rede local:

Interface: ether2, Bridge: bridge-lan. Clique em OK.

Repita para ether3, ether4, ether5.

Repita para as interfaces sem fio: wlan1 (2.4GHz) e wlan2 (5GHz).

Definir um IP para a LAN:

Vá em IP -> Addresses.

Clique no +.

Em Address, digite o IP da sua rede, por exemplo: 192.168.88.1/24. A parte /24 é a máscara de rede.

Em Interface, selecione a bridge que criamos: bridge-lan.

Clique em OK.

Criar um Servidor DHCP (Para distribuir IPs na LAN):

Vá em IP -> DHCP Server.

Clique no botão DHCP Setup.

DHCP Server Interface: selecione bridge-lan e clique em Next.

DHCP Address Space: 192.168.88.0/24. Apenas confirme e clique em Next.

Gateway for DHCP Network: 192.168.88.1. Confirme e clique em Next.

Addresses to Give Out: 192.168.88.2-192.168.88.254. É o intervalo de IPs para seus dispositivos. Confirme e Next.

DNS Servers: Você pode usar o próprio roteador (192.168.88.1) ou servidores públicos como 8.8.8.8 e 1.1.1.1. Next.

Lease Time: Pode deixar o padrão. Next.

Pronto! A configuração do DHCP está completa.

Parte 3: Firewall (NAT) - Permitindo a Saída para a Internet

Isso é crucial. Sem o NAT, seus dispositivos na LAN não conseguem se comunicar com a internet.

Vá em IP -> Firewall.

Vá para a aba NAT.

Clique no +.

Na aba General:

Chain: srcnat.

Out. Interface: ether1 (ou a interface pppoe-out1 se você usa PPPoE).

Na aba Action:

Action: masquerade.

Clique em OK.

Parte 4: Configurando o Wi-Fi

Criar um Perfil de Segurança:

Vá em Wireless.

Vá para a aba Security Profiles.

Clique no + para criar um novo perfil.

Name: perfil-wpa2-wpa3.

Mode: dynamic keys.

Authentication Types: Marque WPA2 PSK e WPA3 PSK.

Nos campos WPA2 Pre-Shared Key e WPA3 Pre-Shared Key, digite a senha forte que você escolheu para o seu Wi-Fi.

Clique em OK.

Configurar as Interfaces Wi-Fi:

Ainda em Wireless, vá para a aba WiFi Interfaces.

Dê um duplo-clique em wlan1 (2.4GHz).

Na aba Wireless:

Mode: ap bridge.

SSID: O nome da sua rede (ex: "MinhaRede_2.4G").

Security Profile: Selecione o perfil que criamos (perfil-wpa2-wpa3).

Country: brazil.

Clique em OK.

Agora, faça o mesmo para wlan2 (5GHz). Você pode usar o mesmo SSID para que os dispositivos escolham a melhor banda, ou um SSID diferente (ex: "MinhaRede_5G") para forçar a conexão.

Clique em Enable (o botão com um "tick" azul) nas interfaces wlan1 e wlan2 se elas estiverem desativadas.

Verificação Final e Dicas

Teste a Conexão: No WinBox/WebFig, vá em Tools -> Ping e tente pingar um endereço externo, como 8.8.8.8. Se receber respostas, sua WAN está funcionando.

Conecte um Dispositivo: Conecte seu computador ou celular na rede Wi-Fi ou em uma das portas LAN (ether2-ether5). Verifique se ele recebe um IP (ex: 192.168.88.254) e se consegue navegar na internet.

Atualize o Sistema: Vá em System -> Packages -> Check for Updates -> Download&Install. Manter o roteador atualizado é vital para segurança e performance.

Atualize o Firmware: Vá em System -> RouterBOARD -> Upgrade.

Faça um Backup: Depois de tudo configurado e funcionando, vá em Files -> Backup para salvar sua configuração.

Pronto! Seu MikroTik hAP ax2 está configurado com uma base sólida e segura para sua rede.
Com certeza! Esta é uma configuração excelente e muito comum para o hAP ax2, aproveitando bem seus recursos. Vamos criar um guia passo a passo, começando do zero para garantir que não haja conflitos.

O método "Quick Set" não é adequado para esta configuração por causa da necessidade de uma rede de visitas isolada. Faremos tudo manualmente, o que lhe dará controle total e segurança.

Objetivo Final

WAN: ether1 conectada ao provedor, recebendo IP Dinâmico (DHCP).

LAN Principal (Moradores):

Rede Wi-Fi 5GHz ("Casa_5G").

Rede Wi-Fi 2.4GHz ("Casa_2.4G").

Portas ether2, ether3, ether4, ether5.

Sub-rede: 192.168.88.0/24.

LAN Secundária (Visitas):

Rede Wi-Fi 2.4GHz ("Visitas").

Totalmente isolada da LAN Principal.

Sub-rede: 192.168.99.0/24.

Serviços: DHCP Server para ambas as redes e NAT para acesso à internet.

Passo 0: Acesso Inicial e Reset

Conecte-se: Conecte seu computador a uma das portas LAN (ex: ether2) e acesse o roteador via WinBox (recomendado) ou pelo IP 192.168.88.1. Login: admin, senha em branco.

Reset para um Início Limpo: Para evitar qualquer problema com a configuração padrão, vamos zerar o roteador.

Vá em System -> Reset Configuration.

Marque a caixa No Default Configuration.

Clique em Reset Configuration e confirme.

O roteador irá reiniciar. Após o reinício, conecte-se novamente via WinBox usando o endereço MAC (listado na aba Neighbors).

Passo 1: Configuração da WAN (Internet)

Vamos dizer ao roteador para pedir um IP ao seu provedor pela porta ether1.

Vá em IP -> DHCP Client.

Clique no botão + (Adicionar).

Na janela que abrir, na opção Interface, selecione ether1.

Deixe as outras opções padrão (especialmente Add Default Route=yes).

Clique em OK.

Em alguns segundos, o status deve mudar para "bound" e você verá o IP que o seu provedor lhe forneceu. Sua internet no roteador já está funcionando.

Passo 2: Criando as Redes Locais (Bridges)

Precisamos de duas "redes" lógicas separadas: uma para os moradores e outra para as visitas. A melhor forma de fazer isso é com Bridges.

Criar a Bridge dos Moradores:

Vá em Bridge.

Na aba Bridge, clique em +.

Em Name, digite bridge-moradores.

Clique em OK.

Criar a Bridge das Visitas:

Clique em + novamente.

Em Name, digite bridge-visitas.

Clique em OK.

Passo 3: Atribuindo Portas às Bridges

Agora vamos colocar as portas físicas e as futuras redes Wi-Fi dentro de suas respectivas bridges.

Vá para a aba Ports dentro do menu Bridge.

Adicionar Portas à bridge-moradores: Clique no + e adicione uma por uma:

Interface: ether2, Bridge: bridge-moradores -> OK

Interface: ether3, Bridge: bridge-moradores -> OK

Interface: ether4, Bridge: bridge-moradores -> OK

Interface: ether5, Bridge: bridge-moradores -> OK

(As interfaces Wi-Fi dos moradores serão adicionadas mais tarde)

As portas ether4 e ether5 agora fazem parte da rede dos moradores. Ao conectar seus switches TP-Link nelas, eles simplesmente estenderão essa rede, e os dispositivos conectados a eles receberão IPs do MikroTik.

Passo 4: Configurando IPs e DHCP Servers

Cada bridge precisa de um endereço IP (gateway) e um servidor DHCP para distribuir IPs aos dispositivos conectados.

IP para a Rede dos Moradores:

Vá em IP -> Addresses.

Clique em +.

Address: 192.168.88.1/24

Interface: bridge-moradores

Clique em OK.

IP para a Rede de Visitas:

Clique em + novamente.

Address: 192.168.99.1/24

Interface: bridge-visitas

Clique em OK.

DHCP Server para os Moradores:

Vá em IP -> DHCP Server.

Clique no botão DHCP Setup.

DHCP Server Interface: bridge-moradores. Clique em Next.

Siga o assistente clicando em Next em todas as telas até o final. Ele usará as configurações de IP que já definimos.

DHCP Server para as Visitas:

Clique em DHCP Setup novamente.

DHCP Server Interface: bridge-visitas. Clique em Next.

Siga o assistente clicando em Next em todas as telas até o final.

Passo 5: Configurando as 3 Redes Wi-Fi

Esta é a parte principal. Vamos criar as senhas primeiro e depois as redes. O hAP ax2 tem duas rádios: wlan1 (2.4GHz) e wlan2 (5GHz).

Criar Perfis de Segurança (Senhas):

Vá em Wireless, na aba Security Profiles.

Clique em +. Crie o perfil para os moradores:

Name: sec-moradores

Mode: dynamic keys

Authentication Types: Marque WPA2 PSK e WPA3 PSK.

Em WPA2 Pre-Shared Key, digite a senha da rede dos moradores.

Clique em OK.

Clique em + novamente. Crie o perfil para as visitas:

Name: sec-visitas

Mode: dynamic keys

Authentication Types: Marque WPA2 PSK.

Em WPA2 Pre-Shared Key, digite a senha da rede de visitas.

Clique em OK.

Configurar as Interfaces Wi-Fi:

Vá para a aba WiFi Interfaces.

Rede Moradores 5GHz (wlan2):

Dê um duplo clique em wlan2.

Na aba Wireless:

Mode: ap bridge

SSID: Casa_5G (ou o nome que preferir)

Security Profile: sec-moradores

Country: brazil (Muito importante!)

Na aba WDS: WDS Mode: dynamic, WDS Default Bridge: bridge-moradores.

Clique em OK. Volte para a lista de interfaces e clique no "tick" azul para ativar (Enable) a wlan2.

Rede Moradores 2.4GHz (wlan1):

Dê um duplo clique em wlan1.

Na aba Wireless, configure da mesma forma: Mode: ap bridge, SSID: Casa_2.4G, Security Profile: sec-moradores, Country: brazil.

Na aba WDS: WDS Mode: dynamic, WDS Default Bridge: bridge-moradores.

Clique em OK. Ative a wlan1.

Rede Visitas 2.4GHz (Virtual AP):

Vamos criar uma segunda rede "virtual" no rádio de 2.4GHz.

Clique no + e escolha Virtual.

Na aba Wireless:

Name: wlan3-visitas (ou qualquer nome para identificar)

Master Interface: wlan1

SSID: Visitas

Security Profile: sec-visitas

Clique em OK.

Adicionar as Interfaces Wi-Fi às Bridges Corretas:

Agora, vamos garantir que cada Wi-Fi esteja na sua rede lógica.

Vá em Bridge, na aba Ports.

Clique em +: Interface: wlan1, Bridge: bridge-moradores -> OK

Clique em +: Interface: wlan2, Bridge: bridge-moradores -> OK

Clique em +: Interface: wlan3-visitas, Bridge: bridge-visitas -> OK

Step 6: Firewall (NAT e Isolação de Visitas)

Este é o passo final e crucial para a segurança.

Configurar NAT (Acesso à Internet):

Vá em IP -> Firewall.

Na aba NAT, clique em +.

Na aba General:

Chain: srcnat

Out. Interface: ether1

Na aba Action:

Action: masquerade

Clique em OK. Agora todos os seus dispositivos podem acessar a internet.

Isolar a Rede de Visitas (Regras de Firewall):

Vá para a aba Filter Rules em IP -> Firewall.

Regra 1: Permitir que visitas acessem a internet.

Clique em +.

Chain: forward

In. Interface: bridge-visitas

Out. Interface: ether1

Na aba Action, Action: accept.

Adicione um comentário (aba Comment): Permite Internet para Visitas. Clique em OK.

Regra 2: Bloquear visitas de acessarem a rede dos moradores.

Clique em +.

Chain: forward

In. Interface: bridge-visitas

Dst. Address: 192.168.88.0/24 (a rede dos moradores)

Na aba Action, Action: drop.

Adicione um comentário: Bloqueia acesso Visitas -> Moradores. Clique em OK.

Regra 3 (Opcional, mas recomendado): Bloquear visitas de acessarem o próprio roteador.

Clique em +.

Chain: input

In. Interface: bridge-visitas

Na aba Action, Action: drop.

Adicione um comentário: Bloqueia acesso de Visitas ao Roteador. Clique em OK.

Ordem das Regras: Arraste as regras que você criou para o topo da lista (ou pelo menos acima de qualquer regra geral de "drop" ou "accept"). A ordem importa no firewall.

Verificação Final

Conecte um dispositivo (celular ou PC) a uma das redes dos moradores (Casa_5G ou Casa_2.4G). Verifique se ele recebe um IP na faixa 192.168.88.x e se consegue navegar na internet.

Conecte outro dispositivo à rede Visitas. Verifique se ele recebe um IP na faixa 192.168.99.x e se navega na internet.

Teste o isolamento: Do dispositivo na rede Visitas, tente acessar (pingar) o IP de um dispositivo na rede dos moradores. A conexão deve falhar.

Crie uma senha de administrador! Vá em System -> Users, clique no usuário admin e em Password para definir uma senha forte.

Faça um backup! Vá em Files -> Backup e salve sua configuração.

Pronto! Seu hAP ax2 está configurado de forma robusta, segura e exatamente como você pediu.
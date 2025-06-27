Excelente! Criar um script para automatizar a configuração é a maneira mais eficiente e precisa de implantar as mesmas regras em um roteador.

Abaixo estão o script completo e as instruções detalhadas de como executá-lo no seu hAP ax2.

O Script de Configuração (config.rsc)

Copie todo o código abaixo e salve-o em um arquivo de texto simples no seu computador. Nomeie o arquivo como config.rsc.

⚠️ Atenção: Antes de usar, edite as seções marcadas com ### EDITAR AQUI ### para definir suas próprias senhas e nomes de rede.

```mikrotik
# =================================================================
# SCRIPT DE CONFIGURACAO MIKROTIK HAP-AX2
# OBJETIVO: WAN DHCP, 3x Wi-Fi (2 Morador, 1 Visita Isolada)
# =================================================================

# --- ETAPA 1: CRIANDO AS BRIDGES (REDES LÓGICAS) ---
/interface bridge
add name=bridge-moradores comment="Bridge para rede principal (Moradores)"
add name=bridge-visitas comment="Bridge para rede de visitas (Isolada)"

# --- ETAPA 2: CONFIGURANDO AS SENHAS DO WI-FI ---
/interface wireless security-profiles
# ### EDITAR AQUI ### - Defina a senha para a rede dos moradores
add name=sec-moradores mode=dynamic-keys authentication-types=wpa2-psk,wpa3-psk wpa2-pre-shared-key="SUA_SENHA_MORADORES" wpa3-pre-shared-key="SUA_SENHA_MORADORES" comment="Seguranca para rede principal"
# ### EDITAR AQUI ### - Defina a senha para a rede de visitas
add name=sec-visitas mode=dynamic-keys authentication-types=wpa2-psk wpa2-pre-shared-key="SUA_SENHA_VISITAS" comment="Seguranca para rede de visitas"

# --- ETAPA 3: CONFIGURANDO AS INTERFACES WI-FI ---
/interface wireless
# ### EDITAR AQUI ### - Defina os nomes (SSID) das suas redes Wi-Fi
set [ find default-name=wlan1 ] ssid="Casa_2.4G" security-profile=sec-moradores country=brazil mode=ap-bridge disabled=no comment="Wi-Fi 2.4GHz para Moradores"
set [ find default-name=wlan2 ] ssid="Casa_5G" security-profile=sec-moradores country=brazil mode=ap-bridge disabled=no comment="Wi-Fi 5GHz para Moradores"
# Criação da interface virtual para visitas
add name=wlan3-visitas master-interface=wlan1 ssid="Visitas" security-profile=sec-visitas disabled=no comment="Wi-Fi 2.4GHz para Visitas"

# --- ETAPA 4: ADICIONANDO PORTAS E WI-FI ÀS BRIDGES ---
/interface bridge port
# Adiciona todas as portas físicas e Wi-Fi dos moradores à bridge principal
add bridge=bridge-moradores interface=ether2
add bridge=bridge-moradores interface=ether3
add bridge=bridge-moradores interface=ether4 comment="Conexao para Switch TP-Link 1"
add bridge=bridge-moradores interface=ether5 comment="Conexao para Switch TP-Link 2"
add bridge=bridge-moradores interface=wlan1
add bridge=bridge-moradores interface=wlan2
# Adiciona a rede Wi-Fi de visitas à sua bridge isolada
add bridge=bridge-visitas interface=wlan3-visitas

# --- ETAPA 5: CONFIGURANDO ENDEREÇOS IP PARA AS REDES ---
/ip address
add address=192.168.88.1/24 interface=bridge-moradores comment="Gateway da rede Moradores"
add address=192.168.99.1/24 interface=bridge-visitas comment="Gateway da rede Visitas"

# --- ETAPA 6: CONFIGURANDO O SERVIDOR DHCP PARA CADA REDE ---
# DHCP para Moradores
/ip pool
add name=pool-moradores ranges=192.168.88.10-192.168.88.254
/ip dhcp-server
add name=dhcp-moradores interface=bridge-moradores address-pool=pool-moradores lease-time=1d disabled=no
/ip dhcp-server network
add address=192.168.88.0/24 gateway=192.168.88.1 dns-server=192.168.88.1,8.8.8.8,1.1.1.1

# DHCP para Visitas
/ip pool
add name=pool-visitas ranges=192.168.99.10-192.168.99.254
/ip dhcp-server
add name=dhcp-visitas interface=bridge-visitas address-pool=pool-visitas lease-time=1d disabled=no
/ip dhcp-server network
add address=192.168.99.0/24 gateway=192.168.99.1 dns-server=8.8.8.8,1.1.1.1

# --- ETAPA 7: CONFIGURANDO A WAN (INTERNET) ---
/ip dhcp-client
add interface=ether1 disabled=no comment="Conexao WAN com a operadora"

# --- ETAPA 8: CONFIGURANDO O FIREWALL (NAT E ISOLAMENTO) ---
/ip firewall nat
# Regra de Masquerade para permitir que as redes internas acessem a internet
add chain=srcnat action=masquerade out-interface=ether1 comment="NAT para toda a rede"

/ip firewall filter
# Regra para permitir que a rede de visitas acesse a internet
add action=accept chain=forward in-interface=bridge-visitas out-interface=ether1 comment="Permite Internet para Visitas"
# Regra para BLOQUEAR a rede de visitas de acessar a rede dos moradores
add action=drop chain=forward in-interface=bridge-visitas dst-address=192.168.88.0/24 comment="BLOQUEIA Visitas -> Moradores"
# Regra para BLOQUEAR a rede de visitas de acessar a interface de gerenciamento do roteador
add action=drop chain=input in-interface=bridge-visitas comment="BLOQUEIA acesso de Visitas ao Roteador"

# --- ETAPA 9: CONFIGURAÇÕES FINAIS DO SISTEMA ---
# ### EDITAR AQUI ### - Defina um nome para seu roteador e uma senha FORTE de administrador
/system identity
set name="MikroTik-Casa"
/user
set [ find name=admin ] password="SUA_SENHA_FORTE_DE_ADMIN"

# --- FIM DO SCRIPT ---
/system reboot
# O roteador irá reiniciar após a aplicação do script.
```

Como Rodar o Script no hAP ax2

Existem duas maneiras fáceis de fazer isso. A Método 2 é a mais recomendada.

Pré-requisito OBRIGATÓRIO: Resetar o Roteador

Para que o script funcione perfeitamente, o roteador deve estar com as configurações de fábrica zeradas.

Conecte seu computador a uma porta LAN (ex: ether2) e acesse o roteador via WinBox.

No menu, vá em System -> Reset Configuration.

Marque a caixa No Default Configuration.

Clique em Reset Configuration e confirme.

O roteador vai reiniciar. Após alguns minutos, ele aparecerá novamente no WinBox (na aba Neighbors). Conecte-se a ele clicando no endereço MAC, pois ele não terá mais um IP.

Método 1: Copiar e Colar no Terminal

Abra o arquivo config.rsc que você editou e salvou.

Selecione e copie (Ctrl+C) todo o conteúdo do script.

No WinBox, abra um terminal clicando em New Terminal no menu à esquerda.

Clique com o botão direito dentro da janela do terminal e selecione Paste.

O script será executado linha por linha. É normal que sua conexão via WinBox caia por um instante quando os IPs são definidos.

A última linha do script (/system reboot) irá reiniciar o roteador. Após o reinício, ele estará pronto para uso.

Método 2: Upload e Importação (Recomendado)

Este método é mais seguro e evita problemas de formatação com o "copiar e colar".

Após resetar o roteador e se reconectar pelo endereço MAC, abra o menu Files no WinBox.

Arraste o arquivo config.rsc (que você editou e salvou) da sua área de trabalho para dentro da janela File List do WinBox. Ele será enviado para o roteador.

Agora, abra o New Terminal.

Digite o seguinte comando no terminal e pressione Enter:

Generated mikrotik
/import file-name=config.rsc
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Mikrotik
IGNORE_WHEN_COPYING_END

O roteador irá ler o arquivo e executar todos os comandos. Você verá a mensagem "Script file loaded and executed successfully" e, em seguida, ele será reiniciado.

O Que Fazer Depois?

Conecte o cabo do seu provedor de internet na porta ether1.

Conecte seus switches TP-Link nas portas ether4 e ether5.

Conecte-se às suas novas redes Wi-Fi ("Casa_2.4G", "Casa_5G", "Visitas") com as senhas que você definiu.

Teste se todos os dispositivos recebem IP e têm acesso à internet.

Faça um backup! Depois de confirmar que tudo está funcionando, vá em Files -> Backup, crie um backup e baixe-o para o seu computador.

Seu hAP ax2 agora está configurado de forma profissional, segura e totalmente automatizada
# =================================================================
# SCRIPT DE CONFIGURACAO MIKROTIK HAP-AX2
# =================================================================

# ### EDITE AS SENHAS E NOMES DE REDE ABAIXO ###
/system identity set name="MikroTik-Casa"
/user set [ find name=admin ] password="SUA_SENHA_FORTE_DE_ADMIN"

/interface bridge
add name=bridge-moradores
add name=bridge-visitas

/interface wireless security-profiles
add name=sec-moradores mode=dynamic-keys authentication-types=wpa2-psk,wpa3-psk wpa2-pre-shared-key="SUA_SENHA_MORADORES" wpa3-pre-shared-key="SUA_SENHA_MORADORES"
add name=sec-visitas mode=dynamic-keys authentication-types=wpa2-psk wpa2-pre-shared-key="SUA_SENHA_VISITAS"

/interface wireless
set [ find default-name=wlan1 ] ssid="Casa_2.4G" security-profile=sec-moradores country=brazil mode=ap-bridge disabled=no
set [ find default-name=wlan2 ] ssid="Casa_5G" security-profile=sec-moradores country=brazil mode=ap-bridge disabled=no
add name=wlan3-visitas master-interface=wlan1 ssid="Visitas" security-profile=sec-visitas disabled=no

/interface bridge port
add bridge=bridge-moradores interface=ether2
add bridge=bridge-moradores interface=ether3
add bridge=bridge-moradores interface=ether4
add bridge=bridge-moradores interface=ether5
add bridge=bridge-moradores interface=wlan1
add bridge=bridge-moradores interface=wlan2
add bridge=bridge-visitas interface=wlan3-visitas

/ip address
add address=192.168.88.1/24 interface=bridge-moradores comment="Gateway Moradores"
add address=192.168.99.1/24 interface=bridge-visitas comment="Gateway Visitas"

/ip pool
add name=pool-moradores ranges=192.168.88.10-192.168.88.254
add name=pool-visitas ranges=192.168.99.10-192.168.99.254

/ip dhcp-server
add name=dhcp-moradores interface=bridge-moradores address-pool=pool-moradores disabled=no
add name=dhcp-visitas interface=bridge-visitas address-pool=pool-visitas disabled=no

/ip dhcp-server network
add address=192.168.88.0/24 gateway=192.168.88.1 dns-server=8.8.8.8,1.1.1.1
add address=192.168.99.0/24 gateway=192.168.99.1 dns-server=8.8.8.8,1.1.1.1

/ip dhcp-client
add interface=ether1 disabled=no

/ip firewall nat
add chain=srcnat action=masquerade out-interface=ether1 comment="NAT para acesso a internet"

/ip firewall filter
add action=accept chain=forward in-interface=bridge-visitas out-interface=ether1 comment="Permite Internet para Visitas"
add action=drop chain=forward in-interface=bridge-visitas dst-address=192.168.88.0/24 comment="BLOQUEIA Visitas -> Moradores"
add action=drop chain=input in-interface=bridge-visitas comment="BLOQUEIA acesso de Visitas ao Roteador"

/system reboot

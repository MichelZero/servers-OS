Port 22
ListenAddress 0.0.0.0
Protocol 2
HostKey /etc/ssh/ssh_host_rsa_key
HostKey /etc/ssh/ssh_host_ecdsa_key
HostKey /etc/ssh/ssh_host_ed25519_key

# Autenticação
PermitRootLogin no  # Desabilitar login direto do root
PasswordAuthentication no  # Desabilitar autenticação por senha (recomenda-se usar chaves SSH)
PubkeyAuthentication yes # Habilitar autenticação por chave pública
AuthorizedKeysFile .ssh/authorized_keys

# Segurança
MaxAuthTries 3  # Limitar tentativas de autenticação
ClientAliveInterval 60  # Enviar keep-alive a cada 60 segundos
ClientAliveCountMax 3  # Desconectar após 3 keep-alives perdidos (180 segundos total)
LoginGraceTime 30  # Tempo máximo para autenticar

# Outros
X11Forwarding no
AllowTcpForwarding no

# Ciphers and MACs (escolha ciphers e MACs seguros)
Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr,aes128-ctr
MACs hmac-sha2-512,hmac-sha2-256,umac-128@openssh.com

UsePAM yes
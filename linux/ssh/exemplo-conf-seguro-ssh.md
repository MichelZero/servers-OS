# Exemplo de configuração segura do SSH
### Este é um exemplo de configuração do OpenSSH que prioriza a segurança.
Localize o arquivo de configuração do SSH, geralmente em /etc/ssh/sshd_config
e faça um backup antes de editar.
 Para aplicar as alterações, reinicie o serviço SSH após editar o arquivo.

```bash
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
MaxSessions 2  # Limitar o número de sessões SSH por conexão
PermitEmptyPasswords no  # Desabilitar senhas vazias
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

```
### Notas:
- **Desabilitar login root**: Isso impede que o usuário root faça login diretamente, forçando o uso de um usuário normal com privilégios elevados.
- **Desabilitar autenticação por senha**: Isso força o uso de chaves SSH, que são mais seguras.
- **Limitar tentativas de autenticação**: Isso ajuda a prevenir ataques de força bruta.
- **Desabilitar senhas vazias**: Isso impede que usuários com senhas vazias façam login.
- **Configurações de keep-alive**: Isso ajuda a desconectar sessões inativas e libera recursos do servidor.
- **Ciphers e MACs**: Escolha algoritmos de criptografia e MACs seguros. A lista acima é um exemplo, mas você deve verificar quais estão disponíveis na sua versão do OpenSSH.
- **UsePAM**: Habilitar o uso do PAM (Pluggable Authentication Module) para autenticação adicional.
### Lembre-se de testar a nova configuração antes de desconectar, para garantir que você não fique trancado fora do servidor.
# Como trocar o nome da máquina Linux

Trocar o nome de uma máquina Linux envolve modificar alguns arquivos e configurações. Aqui estão os passos, com diferentes métodos dependendo da sua distribuição:

## Método 1: Usando `hostnamectl` (Systemd - maioria das distribuições modernas)

Este é o método recomendado para a maioria das distribuições Linux modernas que usam systemd.

1. **Verifique o nome atual:**
   ```bash
   hostnamectl status
    ```

Defina o novo nome (como root ou usando sudo):
 ```bash
   sudo hostnamectl set-hostname novo-nome
   ```

Substitua novo-nome pelo nome desejado. Evite usar caracteres especiais, espaços e letras maiúsculas.

Verifique a alteração:
 ```bash
   hostnamectl status
   ```
2. **Reinicie a máquina:**
   Embora o comando acima aplique a mudança imediatamente, uma reinicialização é recomendada para garantir que todas as configurações sejam carregadas corretamente.
3. **Verifique novamente:**
    Após a reinicialização, use o comando `hostname` ou `hostnamectl status` para verificar se o novo nome foi aplicado corretamente.

## Método 2: Editando arquivos de configuração (para sistemas sem systemd)
Se o seu sistema não utiliza systemd, você precisará editar alguns arquivos manualmente.
1. **Verifique o nome atual:**
   ```bash
   hostname
   ```

Edite o arquivo /etc/hostname:
```bash
   sudo nano /etc/hostname
```

e


Substitua o conteúdo atual pelo novo nome da máquina.

Edite o arquivo /etc/hosts:
```bash
   sudo nano /etc/hosts
```

O arquivo /etc/hosts contém mapeamentos de endereços IP para nomes de host. É importante atualizar este arquivo para garantir que o novo nome da máquina funcione corretamente em sua rede local.




Reinicie a máquina ou use os comandos a seguir para aplicar as alterações:
 ```bash
sudo hostname novo-nome  # Aplica a mudança temporariamente
sudo /etc/init.d/hostname.sh start # Reinicia o serviço de hostname (se disponível)
 ```

Nome de domínio totalmente qualificado (FQDN): Para definir o FQDN, use o comando hostnamectl set-hostname nome-da-maquina.dominio.com. Você também precisará configurar o DNS corretamente.

Reinicialização: Embora os comandos acima apliquem a mudança imediatamente, uma reinicialização é recomendada para garantir que todas as configurações sejam carregadas corretamente.

Permissões: Você precisa de privilégios de root (ou usar sudo) para alterar o nome da máquina.

Distribuições específicas: Algumas distribuições podem ter métodos ou arquivos de configuração ligeiramente diferentes. Consulte a documentação da sua distribuição para obter detalhes específicos.

Após a reinicialização (se aplicável), o novo nome da máquina será usado. Verifique com o comando hostname ou hostnamectl status.


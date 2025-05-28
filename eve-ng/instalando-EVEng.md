# Instalando o EVE-NG Community Edition no VirtualBox

O EVE-NG (em suas versões Community e Professional) não é instalado diretamente dentro do VirtualBox. Ele roda dentro de uma máquina virtual, geralmente Ubuntu Server.  Este guia mostra como instalar a versão Community (gratuita).

## Passos:

1. **Baixar a Imagem ISO do Ubuntu Server:** Acesse o site oficial do Ubuntu e baixe a versão LTS do Ubuntu Server (recomendado).  A versão desktop também funciona, mas o server é mais leve.

2. **Criar uma Máquina Virtual no VirtualBox:**

    * Abra o VirtualBox.
    * Clique em "Novo".
    * Nome da VM: `EVE-NG` (ou similar)
    * Tipo: `Linux`
    * Versão: `Ubuntu (64-bit)`
    * RAM: 4GB (mínimo), 8GB (recomendado) ou mais.
    * Disco rígido: Criar um disco virtual agora.
    * Tipo de arquivo: `VDI (VirtualBox Disk Image)`
    * Armazenamento: `Alocação dinâmica` (recomendado)
    * Tamanho: 40GB (mínimo), mais se necessário.

3. **Configurar a Máquina Virtual:**

    * Selecione a VM e clique em "Configurações".
    * *Sistema > Processador:* Aumente os núcleos virtuais se possível.
    * *Rede > Adaptador 1:* `Rede em Ponte` (Bridged Adapter).
    * *Armazenamento > Controladora: IDE:* Adicione a imagem ISO do Ubuntu Server.

4. **Instalar o Ubuntu Server:**

    * Inicie a VM.
    * Siga as instruções de instalação do Ubuntu Server.
    * Configure um usuário e senha.

5. **Instalar o EVE-NG dentro do Ubuntu Server:**

    * Acesse o terminal da VM.
    * Execute os comandos:

        ```bash
        wget -O eve-ng-community.sh https://raw.githubusercontent.com/eve-ng/eve-ng/master/install.sh
        sudo bash eve-ng-community.sh
        ```

    * Siga as instruções do script.

6. **Acessar o EVE-NG:**

    * Após a instalação, acesse a interface web pelo navegador: `http://<endereco_ip_da_vm>` (porta 80).  Descubra o endereço IP com `ip addr` no terminal da VM.

## Considerações:

* **Recursos do Host:**  Certifique-se de que seu computador tenha recursos suficientes.
* **Rede em Ponte:** Essencial para a comunicação da VM com a rede.
* **Versão Community:** Gratuita, mas com algumas limitações.
* **Documentação Oficial:** Consulte a documentação do EVE-NG para mais informações.


Este processo pode parecer complexo, mas seguindo os passos atentamente você conseguirá instalar o EVE-NG no VirtualBox.  A documentação oficial é a melhor fonte de informação.
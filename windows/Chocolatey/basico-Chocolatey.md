# Chocolatey Cheat Sheet

Este guia rápido cobre os comandos mais comuns e úteis do gerenciador de pacotes Chocolatey para Windows.

## Instalação do Chocolatey:
1. **Abra o PowerShell como Administrador.**
2. **Execute o seguinte comando:**
   ```powershell
   Get-ExecutionPolicy
   ```
    Se o resultado for `Restricted`, execute:
    ```powershell
    Set-ExecutionPolicy AllSigned
    ```
    Se o resultado for `RemoteSigned`, não é necessário alterar.

3. **Execute o seguinte comando:**
   ```powershell
   Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
   ```
4. **Verifique a instalação:**
   ```powershell
    choco --version
    ```

## Gerenciamento de Pacotes:
* **Atualizar o Chocolatey:** `choco upgrade chocolatey`

* **procurando pacotes:** `choco list -lo` (local only)
* **procurando na web** [https://community.chocolatey.org/packages](https://community.chocolatey.org/packages)
* **Instalar um pacote:** `choco install <nome_do_pacote>` (Ex: `choco install googlechrome`)
    * Múltiplos pacotes: `choco install <pacote1> <pacote2> <pacote3>`
    * Versão específica: `choco install <nome_do_pacote> --version <numero_da_versão>`
    * Parâmetros do instalador: `choco install <nome_do_pacote> --params "<parâmetros>"` (Ex: `/quiet`)
    * Confirmar instalação: `choco install <nome_do_pacote> -y` (suprime prompts)
* **Desinstalar um pacote:** `choco uninstall <nome_do_pacote>`
* **Atualizar um pacote:** `choco upgrade <nome_do_pacote>`
    * Todos os pacotes: `choco upgrade all -y`
* **Listar pacotes instalados:** `choco list -lo` (local only)
* **Buscar um pacote:** `choco search <nome_do_pacote>` ou `choco search <palavra_chave>`
* **Exibir informações sobre um pacote:** `choco info <nome_do_pacote>`


## Fontes (Repositories):

* **Listar fontes:** `choco source list`
* **Adicionar uma fonte (oficialmente desencorajado, use o comando `source add` do provedor da fonte):** `choco source add -n <nome> -s <url> -p <prioridade>` (prioridade menor = maior precedência)
* **Remover uma fonte (oficialmente desencorajado, use o comando `source remove` do provedor da fonte):** `choco source remove <nome>`
* **Desabilitar uma fonte:** `choco source disable <nome>`
* **Habilitar uma fonte:** `choco source enable <nome>`


## Outras Opções Úteis:

* **Versão do Chocolatey:** `choco --version`
* **Ajuda:** `choco -h` ou `choco <comando> -h` (Ex: `choco install -h`)
* **Modo verbose (mais detalhes):** `choco -v` ou `choco <comando> -v`
* **Forçar reinstalação:** `choco install <nome_do_pacote> --force`
* **Ignorar checksum:** `choco install <nome_do_pacote> --ignore-checksums` (use com cautela)
* **Limpar cache:** `choco cleanup all` (libera espaço em disco)
* **Instalar como administrador (se necessário):** Use `choco install <pacote> -y --run-as-administrator`


## Recursos Adicionais:

* **Chocolatey GUI:** Interface gráfica para gerenciar pacotes.
* **Pacotes de comunidade:** [https://community.chocolatey.org/packages](https://community.chocolatey.org/packages)
* **Documentação oficial:** [https://docs.chocolatey.org/](https://docs.chocolatey.org/)


## Exemplos Avançados:

* **Instalar Google Chrome em modo silencioso com Chocolatey:** `choco install googlechrome -y --params "/silent"`
* **Atualizar todos os pacotes e confirmar todas as prompts:** `choco upgrade all -y`


## Dicas:

* Use `-y` para evitar prompts e automatizar instalações.
* Verifique a documentação do pacote para parâmetros específicos de instalação.
* Cuidado com pacotes de fontes não confiáveis.


Este Cheat Sheet fornece um resumo dos comandos mais usados no Chocolatey. A documentação oficial oferece informações mais detalhadas e atualizadas.

## Links Úteis:
* [Chocolatey - Site Oficial](https://chocolatey.org/)
* [Chocolatey - Documentação](https://docs.chocolatey.org/)
* [Chocolatey - Repositório de Pacotes](https://community.chocolatey.org/packages)
* [Chocolatey - GitHub]
# Winget Cheat Sheet

Este guia rápido cobre os comandos mais comuns e úteis do Windows Package Manager (winget).

## Gerenciamento de Pacotes:

* **Instalar um pacote:** `winget install <nome_do_pacote>`  (Ex: `winget install vscode`)
    * Usar ID: `winget install <id_do_pacote>` (Mais preciso)
    * Versão específica: `winget install <nome_do_pacote> --version <numero_da_versão>`
    * Fonte específica: `winget install <nome_do_pacote> --source <nome_da_fonte>`
* **Desinstalar um pacote:** `winget uninstall <nome_do_pacote>`
* **Atualizar um pacote:** `winget upgrade <nome_do_pacote>`
    * lista de pacotes atualizáveis: `winget upgrade`
    * Todos os pacotes: `winget upgrade --all`
* **Reinstalar um pacote:** `winget reinstall <nome_do_pacote>`
* **Atualizar o winget:** `winget upgrade --all --source winget`
* **Listar pacotes instalados:** `winget list`
* **Buscar um pacote:** `winget search <nome_do_pacote>` ou `winget search <palavra_chave>`
* **Exibir informações sobre um pacote:** `winget show <nome_do_pacote>`


## Fontes:

* **Listar fontes:** `winget source list`
* **Adicionar uma fonte:** `winget source add -n <nome> -a <url>`
* **Remover uma fonte:** `winget source remove <nome>`
* **Atualizar fontes:** `winget source update`
* **Exportar fontes:** `winget source export > fontes.json`
* **Importar fontes:** `winget source import -i fontes.json`


## Outras Opções Úteis:

* **Versão do Winget:** `winget --version`
* **Ajuda:** `winget --help`  ou `winget <comando> --help` (Ex: `winget install --help`)
* **Modo silencioso (sem prompts):**  Adicione `-h` ou `--silent` ao comando (Ex: `winget install vscode -h`)
* **Modo verbose (mais detalhes):** Adicione `-v` ou `--verbose` ao comando
* **Local de instalação:** Use `--location` para especificar o local de instalação (Ex: `winget install <pacote> --location D:\Programas`)
* **Aceitar termos de licença automaticamente:** Use `--accept-package-agreements` para aceitar automaticamente os termos de licença do software durante a instalação.
* **Instalar a partir de um arquivo:** `winget install -m <caminho_do_arquivo.msixbundle>` (ou outros formatos suportados)
* **Hash para verificação:** Use `--sha256 <hash>` para verificar a integridade do pacote durante a instalação.
* **Validar um manifesto:** `winget validate <caminho_do_manifesto.yaml>`


## Exemplos Avançados:

* **Instalar a versão mais recente do 7-Zip da fonte winget:** `winget install 7zip --source winget`
* **Atualizar todos os pacotes da fonte msstore:** `winget upgrade --all --source msstore`
* **Buscar por pacotes relacionados a "python" e instalar o primeiro resultado:** `winget search python | select-string -pattern python3 -context 0,2 | winget install` (Requer PowerShell)


## Dicas:

* Use aspas duplas para nomes de pacotes com espaços.
* Utilize o ID do pacote para garantir a instalação do software correto.
* Mantenha suas fontes atualizadas para acessar os pacotes mais recentes.
* Explore as opções de cada comando com `winget <comando> --help`.


Este Cheat Sheet fornece um resumo dos comandos mais usados no winget.  A documentação oficial da Microsoft oferece informações mais detalhadas e atualizadas.

## Links Úteis:
* **Documentação do Winget:** Consulte a [documentação oficial do Windows Package Manager](https://docs.microsoft.com/en-us/windows/package-manager/winget/) para aprender mais sobre os comandos e funcionalidades disponíveis
* **GitHub do Winget:** Acesse o [repositório oficial do GitHub]
# Como Fazer Backup de Suas Máquinas (Distribuições) no WSL2
* *Autor: Michel*
* *Data: 15/06/2025*
* *Categoria: terminal*

Fazer backups regulares das suas distribuições WSL2 é uma prática essencial para proteger seus dados, configurações e ambiente de desenvolvimento. Felizmente, o próprio WSL fornece ferramentas de linha de comando que tornam esse processo simples e eficiente.

O método principal utiliza os comandos `wsl --export` para criar o backup e `wsl --import` para restaurá-lo.

### Pré-requisitos

Ter o WSL2 instalado e uma ou mais distribuições Linux configuradas.

Acesso ao PowerShell ou ao Prompt de Comando (CMD) do Windows.
Antes de fazer o backup, você precisa saber o nome exato da distribuição que deseja salvar.

Abra o PowerShell ou o CMD e execute o seguinte comando:

**Passo 1:** Listar as Distribuições Instaladas

```bash
wsl --list --verbose
```
A saída será algo parecido com isto:

```plaintext
NAME            STATE           VERSION
* Ubuntu-22.04    Running         2
  docker-desktop  Running         2
```
#### ou a forma abreviada
```bash
wsl -l -v
```
![alt text](image.png)



Anote o nome da distribuição que você quer fazer o backup. Neste exemplo, usaremos a Ubuntu-22.04.

Dica: Para garantir a consistência dos dados, é uma boa prática desligar a distribuição antes de exportá-la. Você pode desligar todas as instâncias do WSL com `wsl --shutdown` ou uma específica com `wsl --terminate <NomeDaDistro>`.

**Passo 2:** Fazer o Backup (Exportar a Distribuição)

O comando `wsl --export` cria um arquivo .tar (um arquivo compactado) que contém todo o sistema de arquivos da sua distribuição.

```bash
wsl --export <NomeDaDistro> <Caminho\Para\O\Arquivo.tar>
```
onde:
- `<NomeDaDistro>`: O nome da distribuição que você identificou no Passo 1.
- `<Caminho\Para\O\Arquivo.tar>`: O local no seu sistema Windows onde o arquivo de backup será salvo. É importante dar a extensão .tar ao arquivo.


**Exemplo Prático**

Vamos exportar a distribuição Ubuntu-22.04 para uma pasta `D:\Backups\WSL`.

Primeiro, desligue a distro (opcional, mas recomendado):

```powershell
wsl --terminate Ubuntu-22.04
```

Agora, execute o comando de exportação:

```powershell
wsl --export Ubuntu-22.04 "D:\Backups\WSL\ubuntu-2204-backup.tar"
```

Aguarde o processo terminar. Dependendo do tamanho da sua distribuição, isso pode levar vários minutos. Ao final, você terá um arquivo ubuntu-2204-backup.tar no local especificado. Este é o seu backup completo!

**Passo 3:** Restaurar o Backup (Importar a Distribuição)


Se você precisar restaurar seu ambiente em um novo computador ou após um problema, use o comando `wsl --import`. Ele permite que você restaure o backup como uma nova distribuição, com um novo nome e em um local específico.
```powershell
wsl --import <NovoNomeParaDistro> <LocalDeInstalacao> <Caminho\Do\Arquivo.tar>
```
onde:

- `<NovoNomeParaDistro>`: O nome que a sua distribuição restaurada terá. Pode ser o mesmo nome original ou um novo.

- `<LocalDeInstalacao>`: A pasta no Windows onde os arquivos da nova distribuição serão armazenados. É recomendado usar uma pasta dedicada, por exemplo `C:\wsl_dists\ubuntu-restaurada`.

- `<Caminho\Do\Arquivo.tar>`: O caminho para o seu arquivo de backup .tar.

**Exemplo Prático**

Vamos restaurar o backup ubuntu-2204-backup.tar como uma nova distribuição chamada Ubuntu-Restaurada.

```powershell
wsl --import Ubuntu-Restaurada "C:\wsl_dists\ubuntu-restaurada" "D:\Backups\WSL\ubuntu-2204-backup.tar"
```
Aguarde o processo de importação. Ele criará uma nova distribuição WSL com o nome especificado e restaurará todo o conteúdo do backup.

Após a conclusão, se você executar `wsl -l -v` novamente, verá sua nova distro na lista:

```plaintext
NAME                 STATE           VERSION
* Ubuntu-22.04         Stopped         2
  Ubuntu-Restaurada    Stopped         2
  docker-desktop       Running         2
```
Atenção: Configurando o Usuário Padrão Após a Restauração

Um detalhe importante é que, ao importar uma distribuição, o WSL a define para logar com o usuário root por padrão, e não com seu usuário pessoal. Para corrigir isso, siga estes passos:

Inicie a nova distribuição:

```powershell
wsl -d Ubuntu-Restaurada
```
Você será logado como root. Para definir seu usuário padrão, você precisa editar o arquivo de configuração do WSL.

Dentro do terminal da distribuição (você estará como root), crie ou edite o arquivo /etc/wsl.conf com seu editor preferido (nano, vim, etc.):

```bash
nano /etc/wsl.conf
```


Adicione as seguintes linhas, substituindo seu-usuario pelo seu nome de usuário original na distro:

```ini
[user]
default = seu-usuario
```

Salve o arquivo (Ctrl+O e Enter no nano) e saia (Ctrl+X).

Volte ao PowerShell/CMD e desligue a distribuição para que a alteração tenha efeito:

```powershell
wsl --terminate Ubuntu-Restaurada
```

Agora, ao iniciar `wsl -d Ubuntu-Restaurada`, você fará login com seu usuário padrão, assim como na original.

## Seção Bônus: Automatizando o Backup com PowerShell

Você pode criar um script simples em PowerShell para automatizar o processo e adicionar a data ao nome do arquivo.

Crie um arquivo chamado backup-wsl.ps1.
Abra o Bloco de Notas ou qualquer editor de texto e cole o seguinte código nele:

```powershell
# --- Configurações ---
# Nome da distribuição WSL a ser copiada
$distroName = "Ubuntu-22.04"

# Pasta de destino para os backups no Windows
$backupPath = "D:\Backups\WSL"

# --- Lógica do Script ---
# Cria o diretório de backup se ele não existir
if (-not (Test-Path -Path $backupPath)) {
    New-Item -ItemType Directory -Path $backupPath
    Write-Host "Pasta de backup criada em: $backupPath"
}

# Formata a data para incluir no nome do arquivo (ex: 2023-10-27)
$timestamp = Get-Date -Format "yyyy-MM-dd"

# Monta o nome completo do arquivo de backup
$backupFile = "$($backupPath)\$($distroName)-backup-$($timestamp).tar"

Write-Host "Iniciando backup da distro '$distroName'..."
Write-Host "Destino: $backupFile"

# Desliga a distro para garantir a consistência (recomendado)
wsl --terminate $distroName
Start-Sleep -Seconds 3 # Pequena pausa para garantir o desligamento

# Executa o comando de exportação
wsl --export $distroName $backupFile

# Verifica se o backup foi bem-sucedido
if ($?) {
    Write-Host "Backup concluído com sucesso!" -ForegroundColor Green
} else {
    Write-Host "Ocorreu um erro durante o backup." -ForegroundColor Red
}
```

Para executar o script, abra o PowerShell, navegue até a pasta onde salvou o arquivo e execute:

```powershell
.\backup-wsl.ps1
```

Nota: Pode ser necessário alterar a política de execução de scripts do PowerShell. Para permitir a execução de scripts locais, use o comando: Set-ExecutionPolicy RemoteSigned -Scope Process.

## Links Úteis
- [Documentação Oficial do WSL](https://docs.microsoft.com/pt-br/windows/wsl/)
- [GitHub - WSL](https://github.com/microsoft/WSL)  
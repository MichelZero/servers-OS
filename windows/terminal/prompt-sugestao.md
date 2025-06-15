
* *Autor: Michel*
* *Data: 15/06/2025*
* *Categoria: terminal*

para o perfil no powershell do exemplo abaixo, você precisa instalar o Oh My Posh e o Terminal-Icons.

![alt text](image-2.png)

### abra o PowerShell como administrador e execute os seguintes comandos:
```powershell
# Para abrir com o VS Code
code $PROFILE

# Ou para abrir com o Bloco de Notas
notepad $PROFILE
```
cole o seguinte código (abaixo) no arquivo aberto e salve:
depois, feche e reabra o PowerShell para aplicar as mudanças.

```powershell
# --- Configuração do Chocolatey ---
# Habilita o auto-completar para o 'choco'. É uma boa prática manter isso no topo.
$ChocolateyProfile = "$env:ChocolateyInstall\helpers\chocolateyProfile.psm1"
if (Test-Path($ChocolateyProfile)) {
  Import-Module "$ChocolateyProfile"
}


# --- Módulos Principais ---
# Importa os módulos para melhorar a experiência do terminal.
# Terminal-Icons é preferível sobre Get-ChildItemColor por ser mais moderno.
Import-Module -Name Terminal-Icons
Import-Module -Name PSReadLine
Import-Module -Name posh-git


# --- Configuração do Prompt (Oh My Posh) ---
# Inicializa o Oh My Posh usando um caminho absoluto para o tema, garantindo que ele sempre funcione.
# $PSScriptRoot é a pasta onde este arquivo de perfil está salvo (ex: C:\Users\SeuNome\Documents\PowerShell).
oh-my-posh init pwsh --config "$PSScriptRoot\temas-oh-my-posh\clean-detailed.omp.json" | Invoke-Expression


# --- Configurações do PSReadLine (Edição e Histórico) ---
Set-PSReadLineOption -MaximumHistoryCount 20000
Set-PSReadLineKeyHandler -Key Tab -Function MenuComplete

# Configura o PSReadLine para salvar/carregar o histórico automaticamente.
# Este método é mais moderno e seguro, salvando os comandos à medida que são executados.
Set-PSReadLineOption -HistorySaveStyle SaveIncrementally
Set-PSReadLineOption -HistorySavePath (Join-Path ([Environment]::GetFolderPath('UserProfile')) ".ps_history")

# Configura as setas para cima/baixo para pesquisar no histórico
Set-PSReadLineOption -HistorySearchCursorMovesToEnd
Set-PSReadLineKeyHandler -Key UpArrow -Function HistorySearchBackward
Set-PSReadlineKeyHandler -Key DownArrow -Function HistorySearchForward

# Ativa as dicas e previsões de comando com base no histórico
Set-PSReadLineOption -ShowToolTips
Set-PSReadLineOption -PredictionSource History


# --- Aliases e Funções Customizadas ---
# Aliases para comandos comuns de outros sistemas
Set-Alias -Name which -Value Get-Command -Option AllScope
Set-Alias -Name open -Value Invoke-Item -Option AllScope

# Funções para diferentes formatos de listagem de arquivos
function ll { Get-ChildItem | Format-Table }
function la { Get-ChildItem | Format-Wide }
function lb { Get-ChildItem | Format-List }

# Substitui o 'ls' padrão para usar a função 'la' (listagem em colunas)
# -Force é necessário para sobrescrever o alias padrão
Set-Alias -Name ls -Value la -Force -Option AllScope
Set-Alias -Name l -Value lb -Option AllScope

Write-Host "Perfil do PowerShell carregado com sucesso!" -ForegroundColor Green
```
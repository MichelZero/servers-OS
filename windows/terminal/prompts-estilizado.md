# Como usar prompts estilizados como Oh My Posh
description: Aprenda a instalar, configurar e personalizar o `Oh My Posh`
* *Autor: Michel*
* *Data: 15/06/2025*
* *Categoria: terminal*



Usar um prompt estilizado como o `Oh My Posh` transforma seu terminal de uma simples linha de comando para um painel de informações poderoso e visualmente agradável.

Vou te guiar pelo processo completo: o que é, por que usar, como instalar, configurar e personalizar.

O que é o `Oh My Posh`?

`Oh My Posh` é um motor de temas para o seu prompt de comando. Ele permite que você customize completamente a aparência e as informações exibidas no seu terminal (como PowerShell, Bash, Zsh, etc.).

**Principais Benefícios:**

- **Informação Rápida:** Mostra o status do Git (branch, modificações), a versão de linguagens (Node, Python), o status do último comando (sucesso/erro) e muito mais.

- **Contexto Visual:** Ajuda a saber instantaneamente em qual pasta você está, em qual ambiente de nuvem (Azure, AWS), ou em qual contêiner Docker.

- **Estética:** Deixa seu terminal com uma aparência moderna e personalizada, o que torna o trabalho mais agradável.

- **Multiplataforma:** Funciona no Windows, macOS e Linux, em diversos shells.

**Passo 1: Pré-requisitos** - A Fonte Certa (Nerd Fonts)

Este é o passo mais importante e a causa da maioria dos problemas. Para que os ícones (como o símbolo do Git, da pasta, do Python, etc.) apareçam corretamente, você precisa de uma fonte que os contenha. Essas fontes são chamadas de Nerd Fonts.

**Escolha e Baixe uma Nerd Font:**

Acesse o site oficial: Nerd Fonts [https://www.nerdfonts.com/](https://www.nerdfonts.com/).
Escolha uma fonte que você goste. As Nerd Fonts são versões modificadas de fontes populares, adicionando ícones e símbolos úteis para desenvolvedores.

Algumas fontes populares são: FiraCode Nerd Font, MesloLGM Nerd Font, Hack Nerd Font.

Baixe a fonte de sua escolha (geralmente um arquivo .zip).

**Instale a Fonte:**

**Windows:** Descompacte o arquivo e selecione todos os arquivos de fonte (.ttf ou .otf). Clique com o botão direito e escolha "Instalar para todos os usuários".

**macOS:** Descompacte e dê um duplo clique em cada arquivo de fonte para abrir o "Catálogo de Fontes" e clique em "Instalar Fonte".

**Linux:** Descompacte e copie os arquivos de fonte para o diretório ~/.local/share/fonts ou /usr/share/fonts. Depois, rode o comando fc-cache -fv no terminal para atualizar o cache de fontes.

**Configure seu Terminal para Usar a Nerd Font:**

**Windows Terminal:** Vá em Configurações (Ctrl + ,), selecione o perfil que você usa (ex: "PowerShell"), vá para a aba Aparência e, em "Tipo de fonte", escolha a Nerd Font que você instalou (ex: FiraCode NF).

**Visual Studio Code:** Vá em File > Preferences > Settings (Ctrl + ,), procure por Terminal Font Family e altere para o nome da sua Nerd Font (ex: 'FiraCode Nerd Font').

**iTerm2 (macOS):** Vá em Preferences > Profiles > Text > Font e selecione a sua Nerd Font.

**Passo 2:** Instalar o Oh My Posh

A instalação varia conforme seu sistema operacional e shell.

Para Windows (com PowerShell e Winget)

O método mais fácil é usar o winget. Abra o PowerShell como Administrador e rode:
```powershell
winget install JanDeDobbeleer.OhMyPosh
```

Para macOS ou Linux (com Homebrew)
Se você usa o Homebrew, o processo é bem simples. Abra o terminal e rode:

```bash
brew install oh-my-posh
```
Para Windows (com Chocolatey)

Se você prefere usar o Chocolatey, abra o PowerShell como Administrador e rode:

```powershell
choco install oh-my-posh
```
Se você não tiver o Homebrew, instale-o primeiro. Depois, rode:

```bash
brew install oh-my-posh
```

**Passo 3:** Configurar o seu Shell para usar o Oh My Posh

A instalação apenas disponibiliza o comando, mas não ativa o prompt. Você precisa editar o arquivo de perfil do seu shell.

Abra seu arquivo de perfil:

PowerShell (Windows): No PowerShell, digite 
```powershell
notepad $PROFILE
```
Se o arquivo não existir, o PowerShell perguntará se você quer criá-lo. Diga que sim.

```bash
Zsh (macOS/Linux): Use nano ~/.zshrc ou code ~/.zshrc.

Bash (Linux/macOS): Use nano ~/.bashrc ou nano ~/.bash_profile.
```

Adicione a linha de inicialização:
Copie e cole a linha correspondente ao seu shell no final do arquivo de perfil.

Para PowerShell:
```powershell
oh-my-posh init pwsh | Invoke-Expression
```

Para Zsh:
```bash
eval "$(oh-my-posh init zsh)"
```

Para Bash:

```bash
eval "$(oh-my-posh init bash)"
```
Salve e feche o arquivo.
Agora, você precisa recarregar o perfil para aplicar as mudanças.

Recarregue seu perfil:
Feche e reabra seu terminal, ou rode um dos seguintes comandos:

PowerShell: .$PROFILE

Zsh: source ~/.zshrc

Bash: source ~/.bashrc

Se tudo deu certo, você já verá um prompt estilizado! O tema padrão é o `jandedert.omp.json`.

**Passo 4:** Escolher e Customizar um Tema

O Oh My Posh vem com dezenas de temas prontos.

Veja os Temas Disponíveis:
Rode este comando para ver o caminho da pasta de temas:

```bash
oh-my-posh get-themes
```

Isso listará todos os arquivos .json de temas. Você pode pré-visualizá-los na documentação oficial.

Mude para um Novo Tema:
Para mudar de tema, você precisa especificar o caminho do arquivo do tema na linha de inicialização do seu perfil.

Por exemplo, para usar o tema atomic.omp.json:

PowerShell (no seu $PROFILE):

```powershell
oh-my-posh init pwsh --config 'C:\Users\SEU_USUARIO\AppData\Local\Programs\oh-my-posh\themes\atomic.omp.json' | Invoke-Expression
```

Dica: Você pode usar a variável $POSH_THEMES_PATH para facilitar:

```powershell
oh-my-posh init pwsh --config "$POSH_THEMES_PATH/atomic.omp.json" | Invoke-Expression
```

Dica: Com Homebrew no macOS, o caminho costuma ser $(brew --prefix oh-my-posh)/themes/atomic.omp.json

Crie seu Próprio Tema (Avançado):
A melhor forma de criar seu tema é copiar um existente e modificá-lo.

Copie um arquivo .json da pasta de temas para um local seu (ex: ~/meu-tema.omp.json).

Edite o arquivo JSON. A documentação sobre configuração é excelente para entender como adicionar, remover ou modificar "segmentos" (como Git, path, etc.).

Aponte o --config para o seu novo arquivo de tema.

Entendendo os Símbolos do Prompt

Um prompt bem configurado te dá informações valiosas:

C:\Users\Nome\Projeto: O caminho atual.

 main: O ícone do Git () e o nome da branch (main).

✔: O último comando foi executado com sucesso. Se falhar, aparecerá um ✘ vermelho.

~ ou *: Há arquivos modificados no repositório Git.

+: Há arquivos novos (staged).

⇡: Seu branch local está à frente do remoto (commits para dar push).

⇣: Seu branch local está atrás do remoto (commits para dar pull).

 18.12.0: A versão do Node.js ativa na pasta.

🐍 3.9.7: A versão do Python ativa.

Resolução de Problemas Comuns

"Aparecem quadrados ▯ ou símbolos estranhos no meu terminal!"

Causa: Você não configurou a Nerd Font corretamente no seu terminal.

Solução: Volte ao Passo 1 e garanta que a fonte instalada está selecionada como a fonte padrão do seu terminal.

"Meu prompt ficou lento para carregar."

Causa: Alguns segmentos (como status de nuvem ou pacotes) podem demorar para carregar.

Solução: Edite seu tema e remova os segmentos que você não precisa ou ative o cache conforme a documentação do Oh My Posh.

"Como atualizo o Oh My Posh?"

Windows (Winget): winget upgrade JanDeDobbeleer.OhMyPosh

macOS/Linux (Homebrew): brew upgrade oh-my-posh

Comece com um tema pronto que você goste e, aos poucos, personalize-o para atender exatamente às suas necessidades. É uma ferramenta que, uma vez configurada, melhora muito a experiência de desenvolvimento.

**link util:**
- [Documentação Oficial do Oh My Posh](https://ohmyposh.dev/docs/)  
- [Repositório no GitHub](https://github.com/JanDeDobbeleer/oh-my-posh)
# Configurações recomendadas para `.bashrc`

O arquivo `.bashrc` é executado toda vez que um novo terminal interativo é aberto. Ele permite personalizar o ambiente de shell do usuário.

## Exemplos de configurações

### 1. Alias úteis
Os aliases são atalhos para comandos mais longos. Eles ajudam a economizar tempo e digitação. Aqui estão alguns exemplos comuns:

```bash
alias ll='ls -lah'
alias gs='git status'
alias ..='cd ..'
```

```bash
# Habilitar cores para o ls
alias ls='ls --color=auto'
```

### 2. Variáveis de ambiente
Deixando o ambiente mais amigável e funcional. definindo o editor padrão, tamanho do histórico e adicionando um diretório ao PATH.
O exemplo abaixo define o editor padrão como `nano`, aumenta o tamanho do histórico para 10.000 comandos e adiciona um diretório `bin` no diretório home ao PATH.
Não inserir o diretório `bin` do sistema, pois pode causar problemas de segurança.
Para evitar que seja inserido no histórico linhas duplicadas, o comando `HISTCONTROL` é utilizado, além de ignorar linhas que começam com espaço. Também é possível definir o tamanho máximo do arquivo de histórico.
```bash
export EDITOR=nano
export HISTSIZE=10000
export HISTFILESIZE=20000
export HISTCONTROL=ignoredups:erasedups:ignoreboth
export PATH="$HOME/bin:$PATH"
```

### 3. Prompt personalizado (PS1)
```bash
export PS1="\u@\h:\w\$ "
```

### 3.1. seta variavel de ambiente para o Debian chroot
Se você estiver usando o Debian e quiser mostrar o nome do chroot no prompt, adicione a seguinte linha:
```bash
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi
```
### 3.2. xterm-color
Se você estiver usando um terminal que suporta cores, pode adicionar a seguinte linha para habilitar cores no prompt:
```bash
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac
```

### 3.3. para um prompt colorido 
```bash
# descomente para um prompt colorido, se o terminal tiver essa opção; desativado
# desativado por padrão para não distrair o usuário: o foco em uma janela de terminal
# deve estar na saída dos comandos, não no prompt
#force_color_prompt=yes
```

#### 3.3.1. Prompt colorido
Para um prompt mais colorido, você pode usar códigos de cor ANSI. Aqui está um exemplo:
```bash
# Prompt colorido
# \[\e[0;32m\] - Verde
# \[\e[0;34m\] - Azul
# \[\e[0;33m\] - Amarelo
# \[\e[0m\] - Resetar cor
# export PS1="\[\e[0;32m\]\u@\h\[\e[0m\]:\[\e[0;34m\]\w\[\e[0m\]\$ "


if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
  # nos temos que suportam cores, mas não sabemos se o terminal  
  # Temos suporte a cores; suponha que seja compatível com Ecma-48
  # (ISO/IEC-6429). (A falta desse suporte é extremamente rara, e tal
  # caso tenderia a suportar setf em vez de setaf.)
	 color_prompt=yes
   else
	 color_prompt=
   fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    #PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
	#  ┌─
	PS1="\e[01;31m┌─[\e[01;36m\u\e[01;31m]─\e[01;31m[\e[01;37m\h\e[01;31m]─\e[01;31m[\e[01;35m\d\e[01;31m]─\e[01;31m[\e[01;32m\t\e[01;31m]─\e[01;31m[\e[01;33m\w\e[01;31m]:\e[01;31m\n\e[01;31m└──\e[01;36m >>> \e[01;31m\$ \e[00m"
    ;;
*)
    ;;
esac

```

#### 3.3.2. ativar suporte a cores no terminal

```bash
# ativar suporte a cores para ls e também adicionar aliases úteis
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    alias dir='dir --color=auto'
    alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

```

### 4. Ativação de ambientes virtuais automaticamente (opcional)
Se você utiliza ambientes virtuais Python, pode adicionar um trecho para ativar automaticamente o ambiente virtual ao abrir o terminal. Isso é útil se você sempre trabalha em um projeto específico.
```bash
if [ -f "$HOME/.venv/bin/activate" ]; then
  source "$HOME/.venv/bin/activate"
fi
```

### 5. Comandos para melhorar a experiência

* `histappend` faz com que o histórico do terminal seja salvo ao invés de sobrescrito.
* `autocd` permite que você mude de diretório apenas digitando o nome do diretório.
* `checkwinsize` atualiza o tamanho da janela do terminal após redimensioná-la.
* `globstar` permite o uso de `**` para recursão em diretórios.
```bash
# Habilitar histappend, autocd, checkwinsize e globstar

shopt -s histappend
shopt -s autocd
shopt -s checkwinsize
shopt -s globstar

```




## Observações

- Sempre faça backup do `.bashrc` antes de editar.
- Após alterações, use `source ~/.bashrc` para aplicar as mudanças.
- Personalize conforme suas necessidades e ferramentas favoritas.
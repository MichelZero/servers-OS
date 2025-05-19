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

### 4. Ativação de ambientes virtuais automaticamente (opcional)
Se você utiliza ambientes virtuais Python, pode adicionar um trecho para ativar automaticamente o ambiente virtual ao abrir o terminal. Isso é útil se você sempre trabalha em um projeto específico.
```bash
if [ -f "$HOME/.venv/bin/activate" ]; then
  source "$HOME/.venv/bin/activate"
fi
```

### 5. Comandos para melhorar a experiência
**histappend** e **autocd**:
* `histappend` faz com que o histórico do terminal seja salvo ao invés de sobrescrito.
* `autocd` permite que você mude de diretório apenas digitando o nome do diretório.
```bash
# Habilitar histappend e autocd

shopt -s histappend
shopt -s autocd
```


## Observações

- Sempre faça backup do `.bashrc` antes de editar.
- Após alterações, use `source ~/.bashrc` para aplicar as mudanças.
- Personalize conforme suas necessidades e ferramentas favoritas.
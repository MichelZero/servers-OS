# Configurações recomendadas para `.bashrc`

O arquivo `.bashrc` é executado toda vez que um novo terminal interativo é aberto. Ele permite personalizar o ambiente de shell do usuário.

## Exemplos de configurações

### 1. Alias úteis
```bash
alias ll='ls -lah'
alias gs='git status'
alias ..='cd ..'
```

### 2. Variáveis de ambiente
```bash
export EDITOR=nano
export HISTSIZE=10000
export PATH="$HOME/bin:$PATH"
```

### 3. Prompt personalizado (PS1)
```bash
export PS1="\u@\h:\w\$ "
```

### 4. Ativação de ambientes virtuais automaticamente (opcional)
```bash
if [ -f "$HOME/.venv/bin/activate" ]; then
  source "$HOME/.venv/bin/activate"
fi
```

### 5. Comandos para melhorar a experiência
```bash
shopt -s histappend
shopt -s autocd
```

## Observações

- Sempre faça backup do `.bashrc` antes de editar.
- Após alterações, use `source ~/.bashrc` para aplicar as mudanças.
- Personalize conforme suas necessidades e ferramentas favoritas.
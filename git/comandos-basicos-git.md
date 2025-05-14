# Git Cheat Sheet

Este guia rápido cobre os comandos Git mais comuns para o fluxo de trabalho diário.

## Configuração Inicial:

* `git config --global user.name "Seu Nome"`: Configura seu nome de usuário.
* `git config --global user.email "seu.email@exemplo.com"`: Configura seu email.
* `git config --global core.editor "seu_editor"`: Configura seu editor de texto preferido (ex: vim, nano, code).


## Criando Repositórios:

* `git init`: Inicializa um novo repositório Git no diretório atual.
* `git clone <url_do_repositorio>`: Clona um repositório existente.


## Status e Informações:

* `git status`: Mostra o status do repositório (arquivos modificados, adicionados, etc.).
* `git log`: Mostra o histórico de commits.
* `git diff`: Mostra as diferenças entre arquivos modificados e a última versão commitada.
* `git show <commit_hash>`: Mostra informações sobre um commit específico.
* `git branch`: Lista as branches locais.
* `git branch -a`: Lista todas as branches (locais e remotas).
* `git remote -v`: Lista os repositórios remotos configurados.


## Trabalhando com Arquivos:

* `git add <arquivo>`: Adiciona um arquivo ao staging area (preparando para o commit).
* `git add .`: Adiciona todos os arquivos modificados ao staging area.
* `git reset <arquivo>`: Remove um arquivo do staging area.
* `git checkout -- <arquivo>`: Descarta as alterações em um arquivo, voltando à última versão commitada.


## Commits:

* `git commit -m "Mensagem do commit"`: Cria um novo commit com as alterações no staging area.
* `git commit -a -m "Mensagem do commit"`: Adiciona todos os arquivos modificados ao staging area e cria um commit (atalho).
* `git commit --amend`: Modifica o último commit (útil para corrigir mensagens ou adicionar arquivos esquecidos).


## Branches:

* `git checkout -b <nome_da_branch>`: Cria uma nova branch e muda para ela.
* `git checkout <nome_da_branch>`: Muda para uma branch existente.
* `git merge <nome_da_branch>`: Mescla a branch especificada na branch atual.
* `git branch -d <nome_da_branch>`: Deleta uma branch local.


## Repositórios Remotos:

* `git remote add origin <url_do_repositorio>`: Adiciona um repositório remoto chamado "origin".
* `git push -u origin <nome_da_branch>`: Envia as alterações locais para o repositório remoto (e configura o tracking da branch).
* `git push`: Envia as alterações locais para o repositório remoto.
* `git pull`: Baixa as alterações do repositório remoto e mescla na branch atual.
* `git fetch`: Baixa as alterações do repositório remoto sem mesclar.
* `git clone <url_do_repositorio>`: Clona um repositório remoto.


## Desfazendo Alterações (com cuidado!):

* `git revert <commit_hash>`: Cria um novo commit que desfaz as alterações de um commit específico.
* `git reset --hard <commit_hash>`: Reverte o repositório para um commit específico, descartando todas as alterações posteriores (**perigoso!**).


## Stashing:

* `git stash`: Salva temporariamente as alterações não commitadas.
* `git stash pop`: Aplica as alterações salvas mais recentemente e remove-as da stash.
* `git stash list`: Lista as alterações salvas na stash.


## Ignorando Arquivos:

Crie um arquivo `.gitignore` na raiz do seu projeto e liste os arquivos e diretórios que você deseja que o Git ignore (ex: arquivos temporários, compilados, etc.).



Este cheat sheet fornece um ponto de partida para o uso do Git.  Explore a documentação oficial do Git para mais informações e comandos avançados. Lembre-se de praticar regularmente para se familiarizar com os comandos e o fluxo de trabalho do Git.

## Links Úteis:
* [Documentação Oficial do Git](https://git-scm.com/doc)
* [GitHub Guides](https://guides.github.com/)
* [Git Cheat Sheet - GitHub](https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf)
* [Git Cheat Sheet - Atlassian](https://www.atlassian.com/git/tutorials/cheat-sheet)
* [Git Cheat Sheet - Git Tower](https://www.git-tower.com/blog/git-cheat-sheet/)
* [Git Cheat Sheet - GitKraken](https://www.gitkraken.com/learn/git/git-cheat-sheet)
* [Git Cheat Sheet - GitHub Desktop](https://desktop.github.com/)
* [Git Cheat Sheet - GitLab](https://docs.gitlab.com/ee/topics/gitlab_flow.html)
* [Git Cheat Sheet - Bitbucket](https://www.atlassian.com/git/tutorials/cheat-sheet)

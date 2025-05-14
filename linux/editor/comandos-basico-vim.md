# Comandos Básicos do Vim para Criar e Editar Arquivos

**Criando um novo arquivo:**

* **`vim <nome_do_arquivo>`**: Este comando cria um novo arquivo com o nome especificado, ou abre o arquivo se ele já existir.  Por exemplo: `vim meu_arquivo.txt`

**Modos do Vim:**

O Vim possui diversos modos, sendo os principais:

* **Modo Normal (Normal Mode):**  O modo inicial do Vim.  Neste modo, você navega pelo arquivo, usa comandos de edição e entra em outros modos.
* **Modo Inserção (Insert Mode):**  Neste modo, você insere texto no arquivo.
* **Modo Visual (Visual Mode):** Permite selecionar texto visualmente para aplicar comandos.
* **Modo Comando (Command-Line Mode):**  Usado para executar comandos, como salvar, sair e buscar.


## Comandos no Modo Normal:

* **Navegação:**
    * **`h`**: Esquerda
    * **`j`**: Baixo
    * **`k`**: Cima
    * **`l`**: Direita
    * **`w`**: Próxima palavra
    * **`b`**: Palavra anterior
    * **`0`**: Início da linha
    * **`$`**: Fim da linha
    * **`gg`**: Início do arquivo
    * **`G`**: Fim do arquivo
* **Inserção:**
    * **`i`**: Inserir antes do cursor
    * **`a`**: Inserir depois do cursor
    * **`o`**: Inserir uma nova linha abaixo da atual
    * **`O`**: Inserir uma nova linha acima da atual
* **Exclusão:**
    * **`x`**: Apaga o caractere sob o cursor
    * **`dd`**: Apaga a linha atual
    * **`dw`**: Apaga a palavra atual
* **Desfazer/Refazer:**
    * **`u`**: Desfazer
    * **`Ctrl + r`**: Refazer
* **Copiar/Colar (Usando o registrador sem nome ""):**
    * **`yy`**: Copiar a linha atual
    * **`p`**: Colar após o cursor
    * **`P`**: Colar antes do cursor

## Entrando em outros modos:

* **Modo Inserção:** Pressione **`i`**, **`a`**, **`o`** ou **`O`** (veja acima).
* **Modo Comando:** Pressione **`:`**.

## Comandos no Modo Comando:

* **`:w`**: Salvar o arquivo
* **`:wq`**: Salvar e sair
* **`:q!`**: Sair sem salvar (descarta as alterações)
* **`:q`**: Sair (se nenhuma alteração foi feita)
* **`:x`**: Salvar e sair (mesmo que `:wq`)
* **`/texto`**: Buscar por "texto"
* **`:n`**: Próxima ocorrência da busca
* **`:N`**: Ocorrência anterior da busca


## Saindo do Modo Inserção:

Pressione **`Esc`**.


## Exemplo de Edição:

1. Criar um arquivo: `vim meu_arquivo.txt`
2. Entrar no modo de inserção: `i`
3. Escrever texto:  `Este é meu arquivo de teste.`
4. Sair do modo de inserção: `Esc`
5. Salvar e sair: `:wq`


Este é um guia básico com os comandos mais comuns. O Vim possui uma vasta gama de comandos e recursos. Explore a documentação do Vim (`:help` dentro do Vim) para aprender mais.  A prática consistente é fundamental para dominar o editor.

## Links Úteis:
* [Documentação do Vim](https://www.vim.org/docs.php)
* [Vim Cheat Sheet](https://vim.rtorr.com/)
* [Vim Adventures](https://vim-adventures.com/): Jogo para aprender Vim de forma divertida.
* [Vim Tutor](https://www.openvim.com/): Tutorial interativo online para aprender os fundamentos do Vim.
* [Vim Wiki](https://vim.fandom.com/wiki/Vim_Tips_Wiki): Uma coleção de dicas e truques para o Vim.
* [Vim Awesome](https://vimawesome.com/): Um diretório de plugins para o Vim.
* [Vimcasts](http://vimcasts.org/): Vídeos e tutoriais sobre o Vim.
* [Vim Cheat Sheet - GitHub](https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf)
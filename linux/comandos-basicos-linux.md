# Comandos Linux para o dia a dia:

Aqui estão os principais comandos Linux, organizados por grupos para facilitar o uso diário:

**1. Navegação e Manipulação de Arquivos/Diretórios:**

* `pwd`: Mostra o diretório atual (Print Working Directory).
* `cd`: Muda o diretório (Change Directory). Exemplos:
    * `cd ..`: Volta um diretório.
    * `cd /`: Vai para o diretório raiz.
    * `cd ~`: Vai para o diretório home do usuário.
    * `cd -`: Volta para o diretório anterior.
* `ls`: Lista arquivos e diretórios. Opções úteis:
    * `ls -l`: Lista em formato longo (permissões, tamanho, data, etc.).
    * `ls -a`: Lista arquivos ocultos também.
    * `ls -h`: Mostra tamanhos em formato legível (KB, MB, GB).
    * `ls -t`: Ordena por data de modificação.
    * `ls -R`: Lista recursivamente diretórios e subdiretórios.
    * `ls -d *`: Lista apenas diretórios.
* `alias`: Cria um atalho para um comando. Exemplo: 
    * `alias ll='ls -la'` (cria um atalho `ll` para `ls -la`).
* `unalias`: Remove um atalho criado com `alias`. Exemplo: 
    * `unalias ll` (remove o atalho `ll`).
* `mkdir`: Cria um novo diretório (Make Directory). Exemplo: `mkdir nova_pasta`
* `rmdir`: Remove um diretório vazio (Remove Directory). Exemplo: `rmdir pasta_vazia`
* `rm`: Remove arquivos ou diretórios (Remove). Opções úteis:
    * `rm -r`: Remove recursivamente diretórios e seu conteúdo.
    * `rm -f`: Remove sem pedir confirmação (force).
    * `rm -v`: Mostra os arquivos sendo removidos (verbose).
    * `rm -rf`: Remove diretórios e arquivos sem pedir confirmação (cuidado!).
    * `rm -i`: Remove interativamente, pedindo confirmação para cada arquivo.
* `cp`: Copia arquivos ou diretórios (Copy). Exemplo: `cp arquivo.txt novo_arquivo.txt`
* `mv`: Move ou renomeia arquivos ou diretórios (Move). Exemplos:
    * `mv arquivo.txt novo_nome.txt`: Renomeia o arquivo.
    * `mv arquivo.txt /caminho/para/outra/pasta/`: Move o arquivo.
* `touch`: Cria um arquivo vazio ou atualiza a data de modificação de um arquivo existente. Exemplo: `touch meu_arquivo.txt`

* `tar`: Compacta ou descompacta arquivos. Exemplos:
    * `tar -cvf arquivo.tar pasta/`: Cria um arquivo tar da pasta.
    * `tar -xvf arquivo.tar`: Extrai o conteúdo do arquivo tar.
    * `tar -czvf arquivo.tar.gz pasta/`: Cria um arquivo tar.gz (compactado).
    * `tar -xzvf arquivo.tar.gz`: Extrai o conteúdo do arquivo tar.gz.
* `cat`: Mostra o conteúdo de um arquivo (Concatenate). Exemplo: `cat arquivo.txt`
* `less`: Mostra o conteúdo de um arquivo com paginação (navegação com setas). Exemplo: `less arquivo.txt`
* `head`: Mostra as primeiras linhas de um arquivo. Exemplo: `head -n 10 arquivo.txt` (mostra as 10 primeiras linhas).
* `tail`: Mostra as últimas linhas de um arquivo. Exemplo: `tail -n 5 arquivo.txt` (mostra as 5 últimas linhas) - `tail -f arquivo.txt` segue o arquivo em tempo real.
* `find`: Procura arquivos e diretórios.  Exemplo: `find . -name "meu_arquivo*"` (procura arquivos que começam com "meu_arquivo" no diretório atual).
* `locate`: Procura arquivos pelo nome (requer banco de dados atualizado com `updatedb`). Exemplo: `locate meu_arquivo`

**2. Gerenciamento de Processos:**

* `ps`: Lista os processos em execução. Opções úteis:
    * `ps aux`: Lista todos os processos de todos os usuários.
* `top`: Mostra os processos em execução em tempo real, ordenados por uso de recursos.
* `kill`: Encerra um processo. Exemplo: `kill <PID>` (onde `<PID>` é o ID do processo).
* `killall`: Encerra processos pelo nome. Exemplo: `killall firefox`

**3. Permissões e Usuários:**

* `chmod`: Muda as permissões de arquivos e diretórios (Change Mode). Exemplo: `chmod 755 meu_script.sh` (dá permissão de execução ao proprietário, leitura e execução ao grupo e outros).
* `chown`: Muda o proprietário de um arquivo ou diretório (Change Owner). Exemplo: `chown usuario:grupo arquivo.txt`
* `sudo`: Executa um comando como superusuário (root). Exemplo: `sudo apt update`
* `su`: Muda para outro usuário. Exemplo: `su usuario`

**4. Rede:**

* `ping`: Testa a conectividade com um host. Exemplo: `ping google.com`
* `ip a`: Mostra as interfaces de rede e seus endereços IP.
* `ssh`: Conecta a um servidor remoto via SSH. Exemplo: `ssh usuario@servidor`
* `wget`: Baixa arquivos da internet. Exemplo: `wget http://example.com/arquivo.zip`
* `curl`: Transfere dados de ou para um servidor, usando vários protocolos. Exemplo: `curl http://example.com`

**5. Sistema:**

* `uname`: Mostra informações sobre o sistema. Exemplo: `uname -a`
* `df`: Mostra o espaço em disco disponível (Disk Free). Exemplo: `df -h` (mostra em formato legível).
* `du`: Mostra o espaço em disco usado por arquivos e diretórios (Disk Usage). Exemplo: `du -sh *` (mostra o tamanho de cada arquivo/diretório no diretório atual em formato legível).
* `free`: Mostra a memória RAM disponível. Exemplo: `free -h` (mostra em formato legível).
* `date`: Mostra a data e hora atuais.
* `cal`: Mostra o calendário.
* `clear`: Limpa o terminal.
* `history`: Mostra o histórico de comandos.
* `shutdown`: Desliga ou reinicia o sistema.  Exemplos:  `sudo shutdown -h now` (desliga imediatamente), `sudo shutdown -r now` (reinicia imediatamente), `sudo shutdown -h +10` (desliga em 10 minutos).
* `reboot`: Reinicia o sistema.
* `uptime`: Mostra há quanto tempo o sistema está ligado.
* `whoami`: Mostra o nome do usuário atual.
* `hostname`: Mostra o nome do host do sistema.



**6. Manipulação de Texto:**

* `grep`: Procura por padrões em arquivos de texto. Exemplo: `grep "palavra_chave" arquivo.txt`
* `sed`: Editor de fluxo (Stream Editor) para manipular texto. Exemplo: `sed 's/palavra_antiga/palavra_nova/g' arquivo.txt` (substitui todas as ocorrências de "palavra_antiga" por "palavra_nova").
* `awk`: Linguagem de programação para processamento de texto.
* `cut`: Extrai seções de cada linha de um arquivo. Exemplo: `cut -d "," -f 1 arquivo.csv` (extrai a primeira coluna de um arquivo CSV delimitado por vírgulas).


Lembre-se que a maioria dos comandos aceitam opções (flags) que modificam seu comportamento. Use o comando `man <comando>` (manual) para obter informações detalhadas sobre qualquer comando e suas opções. Por exemplo, `man ls` mostrará o manual do comando `ls`.


Este é apenas um resumo dos comandos mais comuns.  Há muitos outros comandos úteis disponíveis no Linux.  Explore e aprenda mais à medida que for usando o sistema!

## Links Úteis:
* [Linux Command Line Basics](https://linuxjourney.com/)
* [Linux Command Cheat Sheet](https://www.cheatography.com/davechild/cheat-sheets/linux-command-line-cheat-sheet/)
* [Linux Documentation Project](https://www.tldp.org/)
* [Linux Command Line for Beginners](https://www.codecademy.com/learn/learn-the-command-line)
* [Linux Command Line Tutorial](https://ryanstutorials.net/linuxtutorial/)
* [Linux Command Line and Shell Scripting Bible](https://www.amazon.com/Linux-Command-Line-Shell-Scripting/dp/1119471628)
* [Linux Command Line Essentials](https://www.udemy.com/course/linux-command-line-essentials/)
* [Linux Command Line Basics Course](https://www.edx.org/course/linux-command-line-basics)
* [Linux Command Line Cheat Sheet PDF](https://www.linuxtrainingacademy.com/linux-command-line-cheat-sheet/)
* [Linux Command Line Cheat Sheet - Cheatography](https://cheatography.com/davechild/cheat-sheets/linux-command-line-cheat-sheet/)
* [Linux Command Line Cheat Sheet - OverAPI](https://overapi.com/linux)
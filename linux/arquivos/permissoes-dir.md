# Permissões de Diretórios no Linux

As permissões de diretórios no Linux controlam o acesso aos diretórios e aos arquivos contidos neles. Assim como as permissões de arquivos, elas são baseadas em três categorias de usuários: **proprietário**, **grupo** e **outros**, e três tipos de permissões: **leitura (`r`)**, **escrita (`w`)** e **execução (`x`)**. No entanto, o significado dessas permissões em diretórios é ligeiramente diferente:

* **Leitura (`r`):** Permite listar o *conteúdo* do diretório (usar o comando `ls`). Sem essa permissão, você não pode ver quais arquivos e subdiretórios estão presentes, mesmo que tenha permissão para acessá-los diretamente.

* **Escrita (`w`):** Permite criar, renomear, mover e excluir arquivos e subdiretórios *dentro* do diretório. Note que isso *não* concede automaticamente permissão para modificar os arquivos *existentes* dentro do diretório; as permissões de arquivo individuais ainda se aplicam.

* **Execução (`x`):** Permite *entrar* no diretório (usar o comando `cd`), tornando-o essencial para acessar subdiretórios e arquivos dentro dele, mesmo que você tenha permissão de leitura para ver o conteúdo ou permissão de escrita para modificar arquivos. Sem a permissão de execução, o diretório é inacessível.

## Exemplo:

Imagine um diretório com permissão `750` (`rwxr-x---`):

* O proprietário tem permissões totais (ler, escrever e executar).
* O grupo pode ler o conteúdo do diretório e entrar nele, mas não pode criar ou excluir arquivos.
* Outros usuários não têm nenhum acesso.

## Comandos:

Os mesmos comandos usados para permissões de arquivos também se aplicam a diretórios:

* `ls -l`: Mostra as permissões do diretório.
* `chmod`: Modifica as permissões. Ex: `chmod 755 /caminho/para/diretorio`
* `chown`: Muda o proprietário.
* `chgrp`: Muda o grupo.

## Considerações importantes:

* A permissão de execução (`x`) em um diretório é **crucial** para acessar seu conteúdo, independentemente das permissões de leitura ou escrita.
* As permissões de diretório atuam como uma "primeira camada" de segurança, enquanto as permissões de arquivo individuais oferecem um controle mais granular.
* Para acessar um arquivo dentro de um diretório, você precisa de permissão de execução em **todos** os diretórios do caminho, além das permissões de leitura no arquivo em si.

Compreender as permissões de diretório é essencial para gerenciar o acesso a arquivos e controlar a segurança do sistema Linux.
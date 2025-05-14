# Roteiro para Criação de um Repositório Git a partir do VS Code

Este roteiro descreve como criar um novo repositório Git a partir do VS Code e conectá-lo a um serviço remoto como o GitHub, GitLab ou Bitbucket.

## Pré-requisitos:

* **Git instalado e configurado:** Certifique-se de ter o Git instalado em seu sistema e que suas credenciais (nome de usuário e email) estejam configuradas globalmente.  Você pode verificar isso executando `git config --global -l` no terminal.
* **Conta em um serviço remoto (opcional, mas recomendado):** Crie uma conta no GitHub, GitLab, Bitbucket ou outro serviço similar se você planeja hospedar seu repositório remotamente.
* **VS Code com a extensão Git instalada:** O VS Code geralmente vem com suporte embutido ao Git, mas verifique se está ativo e funcionando corretamente.

## Passos:

1. **Abra a pasta do projeto no VS Code:** Abra a pasta que contém os arquivos do seu projeto no VS Code.  Se você ainda não tem um projeto, crie uma nova pasta e abra-a.

2. **Inicialize o repositório Git:**
    * Clique no ícone do controle de versão (ícone de ramificação) na barra lateral do VS Code.
    * Clique no botão "Inicializar Repositório" (geralmente um ícone com um sinal de "+" e a palavra "Git"). Isso executará `git init` na pasta do projeto.

3. **Adicione seus arquivos (staging):**
    * Após inicializar o repositório, os arquivos do seu projeto aparecerão na seção "Alterações" do controle de versão.
    * Clique no sinal "+" ao lado de cada arquivo que você deseja adicionar ao seu primeiro commit.  Isso executará `git add <arquivo>`.  Você também pode usar o "+" no topo da seção "Alterações" para adicionar todos os arquivos modificados (`git add .`).

4. **Crie seu primeiro commit:**
    * Na caixa de mensagem de commit, escreva uma mensagem descritiva para o seu commit (ex: "Commit inicial").
    * Clique no ícone de verificação para criar o commit.  Isso executará `git commit -m "Sua mensagem"`.

5. **Crie um repositório remoto (no GitHub, por exemplo):**
    * Acesse o seu serviço de hospedagem Git (GitHub, GitLab, etc.) e crie um novo repositório vazio.  **Não** inicialize o repositório com um README ou `.gitignore` neste momento, pois você já tem um repositório local.
    * Copie a URL do repositório remoto (geralmente na forma `https://github.com/usuario/repositorio.git` ou `git@github.com:usuario/repositorio.git`).

6. **Conecte seu repositório local ao remoto:**
    * Volte ao VS Code e abra o terminal integrado (View > Terminal).
    * Execute o seguinte comando para adicionar o remoto: `git remote add origin <url_do_repositorio_remoto>`.  Substitua `<url_do_repositorio_remoto>` pela URL que você copiou na etapa anterior.

7. **Envie seu código para o repositório remoto:**
    * Execute o comando `git push -u origin main` (ou `git push -u origin master`, dependendo do nome da sua branch principal). O argumento `-u` configura o tracking da branch, para que você possa usar `git push` e `git pull` sem especificar a branch nas próximas vezes.

## Passos Adicionais (Opcional):

* **Criar um arquivo `.gitignore`:** Crie um arquivo `.gitignore` na raiz do seu projeto para especificar arquivos e pastas que você deseja que o Git ignore (ex: arquivos temporários, compilados, etc.).
* **Configurar outras branches:** Crie novas branches para desenvolver funcionalidades isoladas usando `git checkout -b <nome_da_branch>`.

## Dicas:

* Utilize a interface gráfica do VS Code para gerenciar seus commits, branches e mudanças.  É uma maneira intuitiva de interagir com o Git sem precisar usar comandos no terminal o tempo todo.
* Faça commits frequentes e com mensagens descritivas para manter um histórico claro e organizado do seu projeto.
* Explore as outras funcionalidades do Git integradas ao VS Code, como comparação de versões, resolução de conflitos de merge e visualização do histórico do repositório.


Este roteiro fornece um guia básico para criar um repositório Git a partir do VS Code.  À medida que você se familiarizar com o Git, explore os comandos e recursos mais avançados para otimizar seu fluxo de trabalho.

## Links Úteis:
* **Documentação do Git:** Consulte a [documentação oficial do Git](https://git-scm.com/doc) para aprender mais sobre os comandos e funcionalidades disponíveis.
* **Documentação do VS Code:** Consulte a [documentação oficial do VS Code](https://code.visualstudio.com/docs) para aprender mais sobre as funcionalidades e extensões disponíveis.
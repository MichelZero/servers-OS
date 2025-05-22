# Redefinindo a senha do root no Debian via GRUB

Este guia explica como redefinir a senha do root no Debian usando o GRUB.

## Passos

1. **Acesse o menu do GRUB:** Durante a inicialização, pressione repetidamente a tecla `Shift` (ou `Esc`) para interromper o processo e exibir o menu do GRUB. Se você vir o logotipo do seu distribuidor, pode ser necessário manter pressionada a tecla `Shift` imediatamente após ligar o computador.

2. **Selecione a entrada correta:** No menu do GRUB, escolha a entrada do kernel desejado (geralmente a primeira opção, a padrão).

3. **Edite os parâmetros de inicialização:** Pressione `e` para editar os parâmetros da entrada selecionada.

4. **Encontre a linha `linux`:** Procure a linha que começa com `linux` (ou `linuxefi` em sistemas UEFI). Esta linha contém os parâmetros do kernel.

5. **Adicione `rw init=/bin/bash`:** No final da linha `linux`, após os parâmetros existentes, adicione `rw init=/bin/bash`. Certifique-se de haver um espaço entre o último parâmetro e a adição.  Este comando inicializa o sistema em modo single-user com permissões de leitura e escrita, executando o bash como processo inicial.

    * **Explicação dos parâmetros:**
        * `rw`: Monta a partição root em modo leitura/escrita.
        * `init=/bin/bash`: Substitui o processo de inicialização padrão pelo bash, dando acesso total ao sistema como root sem senha.

6. **Inicialize com os parâmetros modificados:** Pressione `Ctrl+x` ou `F10` para inicializar com os parâmetros modificados.

7. **Remonte a partição root com permissões de escrita (se necessário):**  Em alguns casos, o sistema de arquivos raiz pode ser montado como somente leitura, mesmo após adicionar `rw`. Se você receber um erro de sistema de arquivos somente leitura, execute:

    ```bash
    mount -o remount,rw /
    ```

8. **Altere a senha do root:** Agora você estará em um shell como root. Execute:

    ```bash
    passwd
    ```

    Digite a nova senha duas vezes.

9. **Redefina SELinux (se aplicável):** Se o SELinux estiver ativo, execute:

    ```bash
    touch /.autorelabel
    ```

10. **Reinicie o sistema:** Execute:

    ```bash
    exec /sbin/init
    ```

    ou

    ```bash
    reboot
    ```

Agora você pode fazer login como root com a nova senha.


## Importante

* **Anote a nova senha em local seguro.**
* **Este método concede acesso irrestrito ao sistema. Use com responsabilidade.**


## Observações

Este processo funciona na maioria das versões do Debian. Pequenas variações podem existir dependendo da versão do GRUB e da distribuição. Consulte a documentação oficial do Debian para instruções mais precisas para sua versão específica.

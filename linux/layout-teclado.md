# Como trocar o layout do teclado no Ubuntu

Existem diversas maneiras de trocar o layout do teclado no Ubuntu, tanto graficamente quanto pelo terminal. Aqui estão as opções mais comuns:

## Método 1: Configurações (Recomendado)

Este é o método mais simples e recomendado para a maioria dos usuários.

1. **Abra as Configurações do sistema:** Clique no ícone de engrenagem no canto superior direito da tela ou procure por "Configurações" no menu de aplicativos.

2. **Navegue até "Região e Idioma":**  Na janela de Configurações, clique em "Região e Idioma" na barra lateral.

3. **Clique no sinal de "+" (Adicionar uma entrada):**  Na seção "Fontes de Entrada", clique no botão "+".

4. **Selecione o idioma e layout desejado:**  Procure pelo idioma desejado e selecione o layout específico do teclado. Por exemplo, para português do Brasil ABNT2, selecione "Português (Brasil)" e depois "Português (Brasil, ABNT2)".

5. **Remova o layout antigo (opcional):** Se desejar remover o layout anterior, clique nos três pontos verticais ao lado do layout antigo e selecione "Remover".

6. **Teste o novo layout:**  Abra um editor de texto ou qualquer campo de entrada de texto para testar o novo layout.


## Método 2: Terminal (para scripts ou acesso remoto)

Você também pode usar o comando `setxkbmap` no terminal para alterar o layout do teclado.

1. **Abra um terminal.**

2. **Use o comando `setxkbmap` para definir o novo layout:**  A sintaxe básica é `setxkbmap <layout>`.  Por exemplo, para português do Brasil ABNT2:

  ```bash
   setxkbmap br abnt2
  ```

Para português de Portugal:
```bash
setxkbmap pt
```

Para inglês dos EUA:
```bash
setxkbmap us
```
3. **Verifique o layout atual:**  Você pode verificar o layout atual com o comando:

```bash
setxkbmap -query
```




Observações:

Persistência: O método do terminal altera o layout apenas para a sessão atual. Para tornar a mudança permanente, você precisará adicionar o comando setxkbmap ao seu arquivo ~/.profile ou ~/.bashrc.

Variantes: O comando setxkbmap possui diversas opções para configurar variantes de layout, modelos de teclado e outras opções avançadas. Consulte a página de manual (man setxkbmap) para mais informações.

Tecla de atalho: Após configurar os layouts desejados, você pode alternar entre eles usando a tecla Super + Espaço ou Alt + Shift. A combinação de teclas pode variar dependendo da sua configuração. Você pode configurar atalhos personalizados nas Configurações do Sistema, em "Teclado" > "Atalhos" > "Digitação".

Com esses métodos, você pode facilmente configurar e alternar entre diferentes layouts de teclado no Ubuntu.

## Método 3: Arquivo de Configuração (Avançado)
Se você deseja configurar o layout do teclado de forma mais avançada, pode editar o arquivo de configuração do teclado.
1. **Abra um terminal.**
2. **Edite o arquivo de configuração do teclado:**
   ```bash
   sudo nano /etc/default/keyboard
   ```  
3. **Altere a linha `XKBLAYOUT` para o layout desejado:**
    Por exemplo, para português do Brasil ABNT2, modifique a linha para:
    ```bash
    XKBLAYOUT="br"
    ```
    Para português de Portugal:
    ```bash
    XKBLAYOUT="pt"
    ```
    Para inglês dos EUA:
    ```bash
    XKBLAYOUT="us"
    ```

4. **Salve e saia do editor:** Pressione `Ctrl + O` para salvar e `Ctrl + X` para sair do nano.
5. **Reinicie o serviço de teclado:**
   ```bash
   sudo dpkg-reconfigure keyboard-configuration
   ```
6. **Reinicie o computador ou faça logout e login novamente para aplicar as mudanças.**
## Método 4: Usando o GNOME Tweaks (para usuários do GNOME) 
Se você estiver usando o ambiente de desktop GNOME, pode usar o GNOME Tweaks para gerenciar layouts de teclado.
1. **Instale o GNOME Tweaks (se ainda não estiver instalado):**
   ```bash
   sudo apt install gnome-tweaks
   ```
2. **Abra o GNOME Tweaks.**
3. **Vá para a seção "Teclado e Mouse".**
4. **Clique em "Fontes de Entrada".**
5. **Adicione ou remova layouts de teclado conforme necessário.** Você pode adicionar novos layouts clicando no botão "+" e selecionando o layout desejado.
## Método 5: Usando o comando `localectl` (para sistemas com systemd)
Se você estiver usando um sistema com systemd, pode usar o comando `localectl` para definir o layout do teclado.  
1. **Abra um terminal.**
2. **Use o comando `localectl` para definir o layout do teclado:**
   ```bash
   sudo localectl set-keymap br
   ```
   Para português de Portugal:
   ```bash
   sudo localectl set-keymap pt
   ```
   Para inglês dos EUA:
   ```bash
   sudo localectl set-keymap us
   ```
3. **Verifique o layout atual:**
   ```bash  
    localectl status
    ``` 
## Conclusão
Esses são os métodos mais comuns para trocar o layout do teclado no Ubuntu. O método recomendado é usar as Configurações do sistema, pois é mais fácil e intuitivo. No entanto, os outros métodos são úteis em situações específicas, como quando você precisa automatizar a configuração ou está trabalhando em um ambiente sem interface gráfica. Escolha o método que melhor se adapta às suas necessidades.

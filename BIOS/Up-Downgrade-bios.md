# Como fazer downgrade ou regravar a BIOS em notebooks Acer (Insyde)

* *Autor: Michel*
* *Data: 04/06/2025*
* *Categoria: BIOS*
* *Leia tudo o artigo ou assista o vídeo: [Como fazer downgrade ou regravar a BIOS em notebooks Acer (Insyde)](https://youtu.be/9xb4sRgpuy8?si=m6aov9bswMtTywgt)*
título: "Como fazer downgrade ou regravar a BIOS em notebooks Acer (Insyde)"

Recentemente, encontrei um vídeo que explica como fazer downgrade ou regravar a BIOS em notebooks Acer que utilizam BIOS Insyde. O vídeo é focado em um modelo Predator, mas o processo é similar para outros modelos com a mesma BIOS.
* link: "https://youtu.be/9xb4sRgpuy8?si=m6aov9bswMtTywgt"

tags: ["BIOS", "Acer", "Insyde", "Downgrade", "Regravação"]

**Resumo do vídeo:**
O vídeo explica como realizar o downgrade ou regravar a BIOS em notebooks Acer que utilizam BIOS Insyde, focando em um modelo Predator, mas ressaltando que o processo é similar para outros modelos com a mesma BIOS.

**Resumo do processo de downgrade/regravação da BIOS Acer (Insyde):**

1.  **Baixar a BIOS Desejada:**
    *   Acesse o site oficial de suporte da Acer.
    *   Identifique seu dispositivo (pelo número de série, SNID ou modelo).
    *   Na seção de "BIOS/Firmware", baixe a versão da BIOS para a qual você deseja fazer o downgrade ou a mesma versão que você já tem, caso queira apenas regravar. O arquivo geralmente virá em formato `.zip`.

2.  **Preparar os Arquivos (Desabilitar a Verificação de Versão):**
    *   **Extrair o Executável:** O arquivo `.zip` baixado conterá um arquivo executável (ex: `BIOS_114_Formal.exe`). Extraia este executável.
    *   **Acessar os Arquivos Internos do Executável:**
        *   **Com WinRAR (Método Fácil):** Clique com o botão direito no arquivo `.exe` da BIOS e escolha a opção "Extract to "BIOS_XXX\\"" (onde XXX é a versão da BIOS). Isso criará uma pasta com todos os arquivos internos do atualizador.
        *   **Sem WinRAR (Método Alternativo):**
            *   Execute o arquivo `.exe` da BIOS. Ele fará uma extração temporária.
            *   Abra o "Executar" (Windows + R) e digite `%temp%` e pressione Enter. Isso abrirá a pasta de arquivos temporários.
            *   Ordene os arquivos por "Data de modificação". A pasta mais recente criada durante a execução do utilitário da BIOS conterá os arquivos necessários. Copie esta pasta para um local de fácil acesso (ex: Disco C:).
  * Agora você terá uma pasta com os arquivos necessários para o downgrade ou regravação da BIOS.        
    *   **Modificar o Arquivo `platform.ini`:**
        *   Dentro da pasta com os arquivos extraídos (seja pelo WinRAR ou pela pasta Temp), localize e abra o arquivo `platform.ini` com um editor de texto (como o Bloco de Notas).
        *   Procure pela linha `[Bios_Version_Check]` ou similar (pode ser encontrado usando Ctrl+F e buscando por "Bios Version Check").
        *   Abaixo desta seção, haverá uma linha como `Flag=2`.
        *   **Altere o valor de `Flag=2` para `Flag=0`.**
        *   Salve o arquivo `platform.ini`.

3.  **Executar a Atualização/Downgrade:**
    *   Dentro da pasta onde você modificou o `platform.ini`, localize e execute o arquivo principal do utilitário de flash da BIOS (geralmente algo como `H2OFFT-Wx64.exe` ou similar, o mesmo que seria executado para uma atualização normal).
    *   Como a verificação de versão foi desabilitada (`Flag=0`), o utilitário agora permitirá que você instale a versão da BIOS contida nos arquivos, mesmo que seja a mesma ou uma anterior.
    *   Siga as instruções na tela. O computador será reiniciado e o processo de flash da BIOS começará.
    *   **Importante:** Durante o processo de flash, não desligue o computador. As ventoinhas podem operar em velocidade máxima.

4.  **Conclusão:**
    *   Após a conclusão do flash, o computador será reiniciado normalmente com a versão da BIOS que você instalou.

**Pontos Importantes Mencionados no Vídeo:**

*   O utilitário padrão da BIOS Insyde bloqueia o downgrade ou a regravação da mesma versão, mostrando um erro. A modificação no `platform.ini` contorna essa verificação.
*   Atualizar/Downgradar a BIOS é um procedimento arriscado. Faça por sua conta e risco e certifique-se de que a energia não será interrompida durante o processo.
*   O vídeo mostra o processo para um Acer Predator, mas a lógica se aplica a outros notebooks Acer com BIOS Insyde.

Este resumo cobre os passos essenciais demonstrados no vídeo para realizar o downgrade ou regravação da BIOS.
# Como encontrar a chave de licença do Windows pelo terminal (Python)

Você pode executar comandos do terminal em um script Python usando o módulo `subprocess`. Esta é a maneira moderna e recomendada de fazer isso.

Aqui estão exemplos de como executar os comandos para obter a chave do Windows, tanto a versão do Prompt de Comando (CMD) quanto a do PowerShell:

```python
import subprocess
import platform

def get_windows_product_key_cmd():
    """
    Tenta obter a chave do produto do Windows usando o comando WMIC (CMD).
    """
    try:
        # O comando WMIC pode precisar de shell=True para funcionar corretamente em alguns casos
        # ou para interpretar o comando como uma string única.
        # No entanto, seja cauteloso com shell=True se o comando vier de uma entrada não confiável.
        # Aqui, o comando é fixo, então o risco é menor.
        command = "wmic path softwarelicensingservice get OA3xOriginalProductKey"
        result = subprocess.run(command, capture_output=True, text=True, shell=True, check=True)
        
        # O output do wmic geralmente tem um cabeçalho e depois a chave, com espaços extras
        output_lines = result.stdout.strip().split('\n')
        
        # A primeira linha é o cabeçalho "OA3xOriginalProductKey", a segunda é a chave (se existir)
        if len(output_lines) > 1:
            product_key = output_lines[1].strip()
            if product_key: # Verifica se a chave não está vazia
                return product_key
            else:
                return "Chave não encontrada (output vazio após cabeçalho)."
        else:
            return "Chave não encontrada ou formato de output inesperado."
            
    except subprocess.CalledProcessError as e:
        # Ocorre se o comando retornar um código de erro (não zero)
        # check=True faz com que essa exceção seja levantada automaticamente
        return f"Erro ao executar comando CMD: {e.stderr or e.stdout or str(e)}"
    except FileNotFoundError:
        # Ocorre se 'wmic' não for encontrado no PATH
        return "Erro: Comando 'wmic' não encontrado. Verifique se está no PATH do sistema."
    except Exception as e:
        return f"Ocorreu um erro inesperado (CMD): {str(e)}"

def get_windows_product_key_powershell():
    """
    Tenta obter a chave do produto do Windows usando um comando PowerShell.
    """
    try:
        # Comando PowerShell para obter a chave (Get-CimInstance é mais moderno)
        command = [
            "powershell",
            "-NoProfile", # Não carrega o perfil do PowerShell
            "-Command",
            "Get-CimInstance -ClassName SoftwareLicensingService | Select-Object -ExpandProperty OA3xOriginalProductKey"
        ]
        # Alternativa usando Get-WmiObject (mais antigo):
        # command = [
        #     "powershell",
        #     "-NoProfile",
        #     "-Command",
        #     "(Get-WmiObject -query 'select * from SoftwareLicensingService').OA3xOriginalProductKey"
        # ]
        
        # shell=False é o padrão e mais seguro quando o comando é uma lista.
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        
        product_key = result.stdout.strip()
        if product_key:
            return product_key
        else:
            return "Chave não encontrada (output vazio do PowerShell)."
            
    except subprocess.CalledProcessError as e:
        return f"Erro ao executar comando PowerShell: {e.stderr or e.stdout or str(e)}"
    except FileNotFoundError:
        return "Erro: Comando 'powershell' não encontrado. Verifique se está no PATH do sistema."
    except Exception as e:
        return f"Ocorreu um erro inesperado (PowerShell): {str(e)}"

if __name__ == "__main__":
    if platform.system() != "Windows":
        print("Este script é projetado para ser executado apenas no Windows.")
    else:
        print("Tentando obter a chave do produto do Windows...\n")

        print("--- Usando o método CMD (wmic) ---")
        key_cmd = get_windows_product_key_cmd()
        if "Erro" in key_cmd or "não encontrada" in key_cmd:
            print(f"Resultado: {key_cmd}")
        else:
            print(f"Chave do Produto (CMD): {key_cmd}")
        print("-" * 30)

        print("\n--- Usando o método PowerShell ---")
        key_ps = get_windows_product_key_powershell()
        if "Erro" in key_ps or "não encontrada" in key_ps:
            print(f"Resultado: {key_ps}")
        else:
            print(f"Chave do Produto (PowerShell): {key_ps}")
        print("-" * 30)

        print("\nNotas importantes:")
        print("- Este script pode precisar ser executado com privilégios de administrador.")
        print("- Se nenhuma chave for exibida, você pode ter uma licença digital vinculada à sua conta Microsoft,")
        print("  ou a chave não está armazenada no firmware de uma forma que esses comandos possam ler.")
        print("- As chaves recuperadas são geralmente chaves OEM embutidas no firmware.")
```


## Explicação do código:

1.  **`import subprocess`**: Importa o módulo necessário para executar processos externos (comandos do terminal).
2.  **`import platform`**: Usado para verificar se o script está rodando no sistema operacional Windows, já que os comandos são específicos para ele.
3.  **`get_windows_product_key_cmd()`**:
    *   Define o comando `wmic path softwarelicensingservice get OA3xOriginalProductKey` como uma string. Este é o comando do Prompt de Comando (CMD).
    *   **`subprocess.run(...)`**: Executa o comando.
        *   `command`: A string do comando a ser executada.
        *   `capture_output=True`: Indica que queremos capturar a saída padrão (`stdout`) e o erro padrão (`stderr`) do comando.
        *   `text=True`: Decodifica a saída de bytes para uma string (texto) automaticamente.
        *   `shell=True`: Permite que o interpretador de comandos do sistema (shell) processe o comando. Para comandos simples como uma string única, especialmente com `wmic`, isso pode ser necessário ou mais conveniente. **Cuidado:** Usar `shell=True` com entradas não confiáveis pode ser um risco de segurança (injeção de shell). Como o comando aqui é fixo e interno, o risco é mínimo.
        *   `check=True`: Se o comando executado retornar um código de saída diferente de zero (indicando um erro), uma exceção `subprocess.CalledProcessError` será levantada automaticamente. Isso simplifica a verificação de erros.
    *   O `stdout` (saída padrão) do `wmic` geralmente inclui um cabeçalho ("OA3xOriginalProductKey") e depois a chave, muitas vezes com espaços extras. O código divide a saída por linhas, pega a segunda linha (a chave, se existir) e remove espaços em branco.
    *   Blocos `try...except` são usados para capturar e tratar possíveis erros:
        *   `subprocess.CalledProcessError`: Se o comando falhar.
        *   `FileNotFoundError`: Se o executável `wmic` não for encontrado.
        *   `Exception`: Para qualquer outro erro inesperado.
4.  **`get_windows_product_key_powershell()`**:
    *   Define o comando PowerShell como uma lista de strings: `["powershell", "-NoProfile", "-Command", "Get-CimInstance -ClassName SoftwareLicensingService | Select-Object -ExpandProperty OA3xOriginalProductKey"]`.
        *   `"powershell"`: O executável do PowerShell.
        *   `"-NoProfile"`: Impede o PowerShell de carregar o perfil do usuário, o que pode tornar a execução mais rápida e evitar efeitos colaterais de scripts de perfil.
        *   `"-Command"`: Indica que a string seguinte é um comando a ser executado pelo PowerShell.
        *   `"Get-CimInstance ..."`: O comando PowerShell real para obter a chave. `Get-CimInstance` é a forma mais moderna comparada ao `Get-WmiObject`.
    *   **`subprocess.run(...)`**: Executa o comando.
        *   Quando o `command` é uma lista, `shell=False` é o padrão e a prática recomendada por segurança, pois evita a interpretação do shell.
        *   Os outros parâmetros (`capture_output`, `text`, `check`) funcionam da mesma forma que na função CMD.
    *   A saída do PowerShell para este comando específico geralmente é apenas a chave, então um `.strip()` para remover espaços em branco no início/fim é suficiente.
    *   Os blocos `try...except` são semelhantes, tratando erros específicos do PowerShell ou se o `powershell` não for encontrado.
5.  **`if __name__ == "__main__":`**:
    *   Este bloco padrão em Python garante que o código dentro dele só seja executado quando o script é rodado diretamente (por exemplo, `python nome_do_script.py`), e não quando o script é importado como um módulo em outro script.
    *   Primeiro, verifica se o sistema operacional é "Windows" usando `platform.system()`.
    *   Se for Windows, ele chama ambas as funções (`get_windows_product_key_cmd` e `get_windows_product_key_powershell`) e imprime os resultados ou mensagens de erro.
    *   Inclui notas importantes para o usuário sobre privilégios de administrador e a natureza das chaves recuperadas (geralmente OEM).
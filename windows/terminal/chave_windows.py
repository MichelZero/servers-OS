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
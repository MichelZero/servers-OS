# Como Ativar a Virtualização Aninhada (Nested VT-x/AMD-V)

Ativar a virtualização aninhada (Nested VT-x/AMD-V) permite executar um hipervisor dentro de uma máquina virtual.  Este guia fornece passos gerais, mas a implementação exata pode variar dependendo do seu sistema operacional e hipervisor.

## 1. Verifique a Compatibilidade do Processador

Antes de começar, verifique se o seu processador suporta virtualização aninhada:

* **Intel:** Procure por "Intel VT-x with Extended Page Tables (EPT)" ou "Intel VT-x and Extended Page Tables" nas especificações.
* **AMD:** Procure por "AMD-V with Rapid Virtualization Indexing (RVI)" ou "AMD Nested Virtualization" nas especificações.

Se o seu processador não suportar essas tecnologias, a virtualização aninhada não será possível.

## 2. Habilite a Virtualização no BIOS/UEFI

* Reinicie o computador e entre na configuração do BIOS/UEFI (geralmente pressionando Del, F2, F10, F12, ou Esc durante a inicialização).
* Procure por opções relacionadas à virtualização (ex: Intel Virtualization Technology (VT-x), AMD Virtualization (AMD-V), SVM Mode).
* **Ative (Enable)** essas opções.
* Salve as alterações e reinicie o computador.

## 3. Habilite a Virtualização Aninhada no Hipervisor

Após habilitar a virtualização no BIOS, ative-a no seu software de hipervisor:

**Hyper-V (Windows):**

1. Abra o PowerShell como administrador.
2. Execute: `Set-VMProcessor -VMName <Nome da VM> -ExposeVirtualizationExtensions $true` (substitua `<Nome da VM>`).

**VMware Workstation/Player:**

1. Desligue a máquina virtual.
2. Edite o arquivo .vmx da máquina virtual.
3. Adicione as seguintes linhas:
    * `hypervisor.cpuid.v0 = "FALSE"`
    * `mce.enable = "TRUE"`
    * `vhv.enable = "TRUE"` (apenas para VMware Workstation no Windows 10/11)

**VirtualBox:**

1. Desligue a máquina virtual.
2. Execute no terminal: `VBoxManage modifyvm <Nome da VM> --nested-hw-virt on` (substitua `<Nome da VM>`).

## 4. Instale o Sistema Operacional Convidado

Após habilitar a virtualização aninhada, instale um sistema operacional na máquina virtual e, em seguida, instale um hipervisor *dentro* desse sistema para criar uma máquina virtual aninhada.


## Observações Importantes

* A virtualização aninhada pode impactar o desempenho.
* Mantenha os drivers e softwares do hipervisor atualizados.
* Consulte a documentação do seu hipervisor para obter instruções detalhadas e opções de configuração.
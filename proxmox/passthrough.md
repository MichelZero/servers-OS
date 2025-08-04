# Configurando Passthrough de iGPU AMD no Proxmox (pve-lab01)

Este guia detalha o processo de configuração do passthrough de uma GPU integrada (iGPU) de uma APU AMD (como um Ryzen 7 5825U) para uma máquina virtual no Proxmox.

AVISO IMPORTANTE: Este é um procedimento avançado. Garanta que você tenha acesso SSH ao seu servidor Proxmox durante todo o processo. Se algo der errado e você perder o vídeo do console, o SSH será sua única forma de acesso para corrigir o problema.

Visão Geral do Processo

O objetivo é impedir que o host Proxmox inicialize a iGPU para seu próprio uso, deixando-a livre para ser "passada" diretamente para uma máquina virtual.

O processo consiste em 4 etapas principais:

Habilitar o IOMMU: Ativar a tecnologia que permite o passthrough de hardware.

Carregar os módulos VFIO: Usar os drivers corretos que irão "segurar" a GPU para a VM.

Identificar e Isolar a iGPU: Encontrar o endereço da GPU e impedir que o Proxmox a utilize.

Anexar a GPU à VM: Atribuir o dispositivo de hardware à máquina virtual desejada.

Passo 1: Habilitar o IOMMU no GRUB

Abra o Shell do seu nó pve (seja pela interface web ou via SSH).

Edite o arquivo de configuração do bootloader GRUB:

Generated bash
nano /etc/default/grub


Localize a linha que começa com GRUB_CMDLINE_LINUX_DEFAULT= e modifique-a para incluir os parâmetros necessários para AMD. A linha final deve ficar assim:

Generated code
GRUB_CMDLINE_LINUX_DEFAULT="quiet amd_iommu=on iommu=pt video=efifb:off"
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
IGNORE_WHEN_COPYING_END

amd_iommu=on: Habilita a tecnologia IOMMU da AMD.

iommu=pt: Ativa o modo "passthrough" para melhorar a performance.

video=efifb:off: Comando crucial para APUs. Impede o kernel de inicializar o framebuffer do UEFI, liberando a GPU e prevenindo a tela preta no monitor do host.

Salve o arquivo (Ctrl+X, depois Y, e Enter).

Atualize a configuração do GRUB para aplicar as mudanças:

Generated bash
update-grub
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Bash
IGNORE_WHEN_COPYING_END
Passo 2: Configurar os Módulos VFIO

Indique ao Proxmox para carregar os módulos necessários para o passthrough durante a inicialização:

Generated bash
nano /etc/modules
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Bash
IGNORE_WHEN_COPYING_END

Adicione as seguintes linhas no final do arquivo:

Generated code
vfio
vfio_iommu_type1
vfio_pci
vfio_virqfd
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
IGNORE_WHEN_COPYING_END

Salve o arquivo (Ctrl+X, Y, Enter).

Passo 3: Identificar, Isolar e "Blacklist" a iGPU

Encontre os IDs de hardware da sua iGPU e do seu dispositivo de áudio associado.

Generated bash
lspci -nn
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Bash
IGNORE_WHEN_COPYING_END

Procure por "VGA compatible controller" e "Audio device" da AMD. A saída será semelhante a esta:

Generated code
07:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Cezanne [1002:1681]
07:00.1 Audio device [0403]: Advanced Micro Devices, Inc. [AMD/ATI] Renoir Radeon High Definition Audio Controller [1002:1637]
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
IGNORE_WHEN_COPYING_END

Anote os IDs entre colchetes (ex: 1002:1681 e 1002:1637).

Crie um arquivo de configuração para dizer ao VFIO para capturar esses dispositivos.

Generated bash
nano /etc/modprobe.d/vfio.conf
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Bash
IGNORE_WHEN_COPYING_END

Adicione a linha abaixo, substituindo os IDs pelos que você encontrou no passo anterior.

Generated code
options vfio-pci ids=1002:1681,1002:1637
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
IGNORE_WHEN_COPYING_END

Impeça que os drivers gráficos padrão do Proxmox tentem usar a GPU, adicionando-os à "lista negra".

Generated bash
nano /etc/modprobe.d/blacklist.conf
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Bash
IGNORE_WHEN_COPYING_END

Adicione as seguintes linhas ao arquivo:

Generated code
blacklist amdgpu
blacklist radeon
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
IGNORE_WHEN_COPYING_END

Salve os arquivos e atualize a imagem do kernel inicial (initramfs):

Generated bash
update-initramfs -u
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Bash
IGNORE_WHEN_COPYING_END

Reinicie o servidor Proxmox.

Generated bash
reboot
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Bash
IGNORE_WHEN_COPYING_END
Passo 4: Verificar e Anexar a GPU à VM

Após a reinicialização, conecte-se via SSH e verifique se o driver vfio-pci está em uso pela GPU:

Generated bash
lspci -nnk
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Bash
IGNORE_WHEN_COPYING_END

A saída para os dispositivos da sua iGPU agora deve mostrar: Kernel driver in use: vfio-pci.

Se a verificação foi bem-sucedida, anexe a GPU a uma máquina virtual:

Selecione a VM (ela deve estar desligada).

Vá em Hardware -> Add -> PCI Device.

Em Device, selecione o dispositivo "VGA compatible controller" da AMD.

Marque a caixa Primary GPU.

Clique em Add.

Repita o processo, adicionando agora o Audio device da AMD (não precisa marcar Primary GPU para este).

Verifique as opções da VM:

Vá na aba Options da VM.

Certifique-se que o BIOS está configurado como OVMF (UEFI).

Inicie a VM. O sistema operacional convidado (Windows ou Linux) deverá agora detectar a GPU da AMD. Você precisará instalar os drivers gráficos oficiais da AMD dentro da VM para obter aceleração completa.
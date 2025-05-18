# Instalação do Linux

Este guia apresenta um passo a passo básico para instalar o sistema operacional Linux em um computador ou servidor.

## 1. Escolha da Distribuição

Existem diversas distribuições Linux, como Ubuntu, Debian, CentOS, Fedora, entre outras. Escolha a que melhor atende às suas necessidades.

## 2. Download da Imagem ISO

Acesse o site oficial da distribuição escolhida e faça o download da imagem ISO correspondente.

- [Ubuntu](https://ubuntu.com/download)
- [Debian](https://www.debian.org/distrib/)
- [Fedora](https://getfedora.org/)
- [CentOS](https://www.centos.org/download/)

## 3. Criação de Mídia de Instalação

Utilize um pendrive (mínimo 4GB) ou DVD para criar a mídia de instalação. Ferramentas recomendadas:

- [Rufus (Windows)](https://rufus.ie/)
- [balenaEtcher (Windows/Linux/Mac)](https://www.balena.io/etcher/)

## 4. Configuração da BIOS/UEFI

Reinicie o computador e acesse a BIOS/UEFI para configurar o boot pelo pendrive ou DVD.

## 5. Processo de Instalação

1. Inicie o computador pela mídia de instalação.
2. Siga as instruções do instalador gráfico ou em modo texto.
3. Defina idioma, fuso horário, layout do teclado e partições do disco.
4. Crie um usuário e defina a senha de administrador (root ou sudo).
5. Aguarde a conclusão da instalação e reinicie o sistema.

## 6. Pós-instalação

- Atualize o sistema:
  ```bash
  sudo apt update && sudo apt upgrade   # Para distribuições baseadas em Debian/Ubuntu
  sudo dnf update                      # Para Fedora
  sudo yum update                      # Para CentOS
  ```
- Instale drivers e softwares adicionais conforme necessário.

## Dicas

- Faça backup dos dados importantes antes de instalar.
- Consulte a documentação oficial da distribuição para detalhes específicos.

---

Sinta-se à vontade para sugerir melhorias neste guia!
